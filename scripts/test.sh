usage() { echo -e "${YELLOW}Usage: $0 <-n object_name> <-d density> <-i obj_id>[-A alpha=1e-7] [-B beta=5.0]${NC}" 1>&2; exit 1;}

while getopts ":p:b:e:" opt; do
    case $opt in
		p) DIRPATH=$OPTARG;;
		b) BEGID=$OPTARG;;
		e) ENDID=$OPTARG;;
		\?) echo "Invalid option: -$OPTARG"
			usage;;
		:)  echo "Option -$OPTARG requires an argument."
			usage;;
    esac
done

echo $OBJNAME





SOURCECODE=/data/vision/billf/object-properties/sound
ISOSTUFFER=${SOURCECODE}/sound/code/IsoStuffer/build/src/isostuffer
MODALSOUND=${SOURCECODE}/sound/code/ModalSound/build/bin
EXTMAT=${MODALSOUND}/extmat
GENMOMENTS=${MODALSOUND}/gen_moments
CLICKSYNTH=${MODALSOUND}/click_synth
FILEGENERATORS=${SOURCECODE}/sound/code/file_generators
BULLET=${SOURCECODE}/sound/bullet3/bin

bash ${SOURCECODE}/ztzhang/renew/re_new.sh
source ~/.bash_profile
cd $DIRPATH
pwd
mkdir -p moments
cd moments
pwd
MAXNUM=59 #`expr $count - 1`
${GENMOMENTS} ../fastbem/input-%d.dat ../bem_result/output-%d.dat ${BEGID} ${MAXNUM} | tee -a log.txt
cd ..
