SOURCECODE=/data/vision/billf/object-properties/sound
bash ${SOURCECODE}/ztzhang/renew/re_new.sh
echo $1
source ~/.bash_profile
unset PYTHONPATH
python /data/vision/billf/object-properties/sound/sound/script/Gen_Sound_New.py -s $1