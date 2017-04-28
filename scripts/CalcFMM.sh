SOURCEPATH=/data/vision/billf/object-properties/sound/sound/script
LIBPATH=/data/vision/billf/object-properties/sound/software/fmmlib3d-1.2/matlab
cd $SOURCEPATH
source ~/.bash_profile
bash /data/vision/billf/object-properties/sound/ztzhang/renew/re_new.sh
MATLAB=/afs/csail.mit.edu/common/matlab/2015a/bin/matlab
$MATLAB -nodisplay -nodesktop -nosplash -r "addpath('${SOURCEPATH}');addpath('${LIBPATH}'); FMMsolver('$1','$2'); quit"