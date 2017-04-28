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


# Setting Directories
SOURCECODE=/data/vision/billf/object-properties/sound
ISOSTUFFER=${SOURCECODE}/sound/code/IsoStuffer/build/src/isostuffer
MODALSOUND=${SOURCECODE}/sound/code/ModalSound/build/bin
EXTMAT=${MODALSOUND}/extmat
GENMOMENTS=${MODALSOUND}/gen_moments
CLICKSYNTH=${MODALSOUND}/click_synth
FILEGENERATORS=${SOURCECODE}/sound/code/file_generators
BULLET=${SOURCECODE}/sound/bullet3/bin


###############    Simulation Part  ############################
################################################################

# Bullet Physics Simulation
echo -e "${GREEN}==>Bullet Physics Simulation${NC}" #| tee -a "$LOGFILE"
#cp bullet.input.dat ${BULLET}
#cp bullet.cfg ${BULLET}
#cd ${BULLET}
CURRENTDIR=`pwd`
${BULLET}/App_RigidBodyFromObjExampleGui_gmake_x64_release ${CURRENTDIR}/bullet.cfg ${CURRENTDIR}/bullet.input.dat | tee -a log.txt
#cd -
#mv ${BULLET}/collision_info.dat ./
#mv ${BULLET}/motion_info.dat ./

#################################################################

# Python Script to Process collision.dat
echo -e "${GREEN}==>Processing Collision Output${NC}" #| tee -a "$LOGFILE"
${FILEGENERATORS}/collision_info_modifier.py collision_info.dat motion_info.dat collision.dat motion.dat collision_motion.dat #| tee -a "$LOGFILE"
${FILEGENERATORS}/get_collision_info.py bullet.input.dat collision_motion.dat #| tee -a "$LOGFILE"

################################################################
echo -e "${GREEN}==>ALL DONE!${NC}"

exit 0
