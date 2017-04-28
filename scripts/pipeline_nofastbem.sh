#!/bin/bash
#set -x
set -e

######################## Color Settings ########################
RED='\033[1;31m'
GREEN='\033[1;32m'
BLUE='\033[1;34m'
YELLOW='\033[1;33m'
NC='\033[0m' 
################################################################

# Parsing Arguments
usage() { echo -e "${YELLOW}Usage: $0 <-n object_name> <-y young's_modulus> <-p poisson_ratio> <-d density> [-A alpha=1e-7] [-B beta=5.0] [-P parallel=1] [-F fps=60] [-D duration=5.0] [-R restitution=0.3] [-C collision_margin=0.002]${NC}" 1>&2; exit 1;}

while getopts ":n:y:p:d:x:y:z:A:B:P:F:D:R:C:S:G:r:l:" opt; do
    case $opt in
		n) OBJNAME=$OPTARG;;
		y) YOUNGSMODULUS=$OPTARG;;
		p) POISSONRATIO=$OPTARG;;
		d) DENSITY=$OPTARG;;
		A) ALPHA=$OPTARG;;
		B) BETA=$OPTARG;;
		P) PARALLEL=$OPTARG;;
		F) FPS=$OPTARG;;
		D) DURATION=$OPTARG;;
		R) RESTITUTION=$OPTARG;;
		C) COLLISIONMARGIN=$OPTARG;;
		S) SKIP_SIM=$OPTARG;;
		G) SKIP_GEN=$OPTARG;;
        r) R_ISO=$OPTARG;;
        l) L_ISO=$OPTARG;;
		\?) echo "Invalid option: -$OPTARG"
			usage;;
		:)  echo "Option -$OPTARG requires an argument."
			usage;;
    esac
done

# Setting Default Values
if [ -z ${ALPHA+x} ]
then
	ALPHA=1e-7
fi
if [ -z ${BETA+x} ]
then
	BETA=5.0
fi
if [ -z ${PARALLEL+x} ]
then
	PARALLEL=1
fi
if [ -z ${FPS+x} ]
then
	FPS=60
fi
if [ -z ${DURATION+x} ]
then
	DURATION=5.0
fi
if [ -z ${RESTITUTION+x} ]
then
	RESTITUTION=0.3
fi
if [ -z ${COLLISIONMARGIN+x} ]
then
	COLLISIONMARGIN=0.002
fi


# Setting Directories
SOURCECODE=/data/vision/billf/object-properties/sound
ISOSTUFFER=${SOURCECODE}/sound/code/IsoStuffer/build/src/isostuffer
MODALSOUND=${SOURCECODE}/sound/code/ModalSound/build/bin
EXTMAT=${MODALSOUND}/extmat
GENMOMENTS=${MODALSOUND}/gen_moments
CLICKSYNTH=${MODALSOUND}/click_synth
FILEGENERATORS=${SOURCECODE}/sound/code/file_generators
BULLET=${SOURCECODE}/sound/bullet3/bin
if [ -z ${SKIP_GEN+x} ]
then
# Enter Object Directory and Logging
cd $OBJNAME
LOGFILE="./SOUND.log"
if [ ! -f "${OBJNAME}.orig.obj" ]
then
	echo -e "${RED}ERROR:${NC} .obj file not found! Process terminates!" | tee "$LOGFILE"
	exit 3
fi

echo -e "${BLUE}Modal Analysis Starts${NC}" | tee "$LOGFILE"

################################################################

# IsoStuffer
echo -e "${GREEN}==>Creating Tetrahedral Mesh${NC}" | tee -a "$LOGFILE"
$ISOSTUFFER -R ${R_ISO} -L ${L_ISO} -M 7 -a 0.25 -b 0.42978 ${OBJNAME}.orig.obj ${OBJNAME}.tet | tee -a "$LOGFILE"

################################################################

# Extract Matrices
echo -e "${GREEN}==>Generating Stiffness/Mass Matrices${NC}" | tee -a "$LOGFILE"
$EXTMAT -f ${OBJNAME} -y ${YOUNGSMODULUS} -p ${POISSONRATIO} -m -k -g -s -d 1 | tee -a "$LOGFILE"

################################################################

# .ev File Generation
echo -e "${GREEN}==>Calculating Eigen-pairs${NC}" | tee -a "$LOGFILE"
#$FILEGENERATORS/spm_reader ${OBJNAME}.stiff.spm ${OBJNAME}.stiff.dat | tee -a "$LOGFILE"
#$FILEGENERATORS/spm_reader ${OBJNAME}.mass.spm ${OBJNAME}.mass.dat | tee -a "$LOGFILE"

# TODO: ev_generator frequency selection, it now chooses smallest 60 eigen-pairs
#cp ${FILEGENERATORS}/ev_generator60.m ./
#cp ${FILEGENERATORS}/readSPM.m ./
matlab -nodisplay -nodesktop -nosplash -r "addpath('${FILEGENERATORS}'); ev_generator60('${OBJNAME}', 60); quit" | tee -a "$LOGFILE"

################################################################

# .vmap File Generation
echo -e "${GREEN}==>Generating Vertex Mapping${NC}" | tee -a "$LOGFILE"
$FILEGENERATORS/vmap_generator ${OBJNAME}.geo.txt ${OBJNAME}.vmap

###############################################################

# Generating FastBEM Input by Matlab
echo -e "${GREEN}==>Generating FastBEM Input${NC}" | tee -a "$LOGFILE"
#cp ${FILEGENERATORS}/FastBEMInputGenerator.m ./
mkdir -p bem_input bem_result fastbem
#cp ../input.fmm ./fastbem/
currentdir=`pwd`
echo $currentdir
matlab -nodisplay -nodesktop -nosplash -r "addpath('${FILEGENERATORS}');BEMInputGenerator('${currentdir}', '${OBJNAME}', ${DENSITY}, ${ALPHA}, ${BETA}); quit" | tee -a "$LOGFILE"

################################################################

# Running FastBEM in Parallel Defined by PARALLEL
echo -e "${GREEN}==>Calling FMM_BEM Matlab Solver: ${NC}" | tee -a "$LOGFILE"
matlab -nodisplay -nodesktop -nosplash -r "addpath('${FILEGENERATORS}');BEMsolver('${currentdir}'); quit" | tee -a "$LOGFILE"

################################################################


# gen_moment
echo -e "${GREEN}==>Moment Generation: ${NC}" #| tee -a "$LOGFILE"
mkdir -p moments
cd moments
MAXNUM=59 #`expr $count - 1`
${GENMOMENTS} ../fastbem/input-%d.dat ../bem_result/output-%d.dat 0 ${MAXNUM} | tee -a "$LOGFILE"
cd ../

fi

###############    Simulation Part  ############################
################################################################

if [ -z ${SKIP_SIM+x} ]
then
# Bullet Physics Simulation
echo -e "${GREEN}==>Bullet Physics Simulation${NC}" #| tee -a "$LOGFILE"
#cp bullet.input.dat ${BULLET}
#cp bullet.cfg ${BULLET}
#cd ${BULLET}
CURRENTDIR=`pwd`
${BULLET}/App_RigidBodyFromObjExampleGui_gmake_x64_release ${CURRENTDIR}/bullet.cfg ${CURRENTDIR}/bullet.input.dat # | tee -a "$LOGFILE"
#cd -
#mv ${BULLET}/collision_info.dat ./
#mv ${BULLET}/motion_info.dat ./

#################################################################

# Python Script to Process collision.dat
echo -e "${GREEN}==>Processing Collision Output${NC}" #| tee -a "$LOGFILE"
${FILEGENERATORS}/collision_info_modifier.py collision_info.dat motion_info.dat collision.dat motion.dat collision_motion.dat #| tee -a "$LOGFILE"
${FILEGENERATORS}/get_collision_info.py bullet.input.dat collision_motion.dat #| tee -a "$LOGFILE"

################################################################

# Generating .ini File
echo -e "${GREEN}==>Creating Config File for Sound Generation${NC}" #| tee -a "$LOGFILE"
printf "[mesh]\n" > click_temp.ini
printf "surface_mesh = ${OBJNAME}.obj\nvertex_mapping = adddd\n\n[audio]\nuse_audio_device = false\ndevice = \nTS = 1.0\namplitude = 2.0\ncontinuous = true\n\n[gui]\ngui=false\n\n[transfer]\nmoments = moments/moments.pbuf\n\n[modal]\nshape = ${OBJNAME}.ev\ndensity = ${DENSITY}\nalpha = ${ALPHA}\nbeta = ${BETA}\nvtx_map = ${OBJNAME}.vmap\n\n[camera]\nx = 0\ny = 0\nz = 1\n\n[collisions]\n" >> click_temp.ini
cat click_temp.ini collision_output-1.dat > click.ini
rm click_temp.ini

################################################################

# click_synth
echo -e "${GREEN}==>Generating Continuous Audio (click_synth)${NC}" #| tee -a "$LOGFILE"
${CLICKSYNTH} click.ini | tee -a "$LOGFILE"
exit 0

################################################################

# TODO: blender API
echo -e "${GREEN}==>Blender Rendering${NC}" | tee -a "$LOGFILE"

################################################################

fi

cd ..
echo -e "${GREEN}All done!${NC}" | tee -a "$LOGFILE"
exit 0
