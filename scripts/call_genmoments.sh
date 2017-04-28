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
cd $1
pwd
mkdir -p moments
cd moments
pwd
MAXNUM=59 #`expr $count - 1`
${GENMOMENTS} ../fastbem/input-%d.dat ../bem_result/output-%d.dat 0 ${MAXNUM} | tee -a log.txt
cd ..
