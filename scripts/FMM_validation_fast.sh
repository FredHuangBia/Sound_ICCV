SOURCECODE=/data/vision/billf/object-properties/sound
SOURCEPATH=/data/vision/billf/object-properties/sound/sound/script
LIBPATH=/data/vision/billf/object-properties/sound/software/fmmlib3d-1.2/matlab

bash ${SOURCECODE}/ztzhang/renew/re_new.sh
#echo $1
source ~/.bash_profile
HOSTNAME=hostname
python /data/vision/billf/object-properties/sound/sound/script/validate_precal_fast.py $1 $2 0 $HOSTNAME
echo finished calling
#echo $2
cd $SOURCEPATH
source ~/.bash_profile
CURPATH=/data/vision/billf/object-properties/sound/sound/validation/$1/mat-$2
FILEGENERATORS=${SOURCECODE}/sound/code/file_generators
#echo callingMatlab
#matlab -nodisplay -nodesktop -nosplash -r "addpath('${FILEGENERATORS}');BEMsolver('$CURPATH',0); quit"


#echo $2
cd $SOURCEPATH
bash ${SOURCECODE}/ztzhang/renew/re_new.sh
source ~/.bash_profile
MATLAB=/afs/csail.mit.edu/common/matlab/2015a/bin/matlab
CURPATH=/data/vision/billf/object-properties/sound/sound/validation/$1/mat-$2
$MATLAB -nodisplay -nodesktop -nosplash -r "addpath('${SOURCEPATH}');addpath('${LIBPATH}'); FMMsolver('$CURPATH',$3); quit"


cd $CURPATH
mkdir -p moments
cd moments
if [ -f "moments.pbuf" ]
then
    echo "FOUND!!!"
else
    GENMOMENTS=${SOURCECODE}/sound/code/ModalSound/build/bin/gen_moments
    ${GENMOMENTS} ../fastbem/input-%d.dat ../bem_result/output-%d.dat 0 29
fi