
INFO_FILE="info.txt"
HOUR_RUN_STOCK=09
MINUTE_RUN_STOCK=00

while [ 1 ]
do
    HOUR=`date +"%H"`
    MINUTE=`date +"%M"`
    DAY_OF_WEEK=`date +"%u"`
    NOT_UPDATE_FILE_NAME="notupdate"
    if [ -f "$NOT_UPDATE_FILE_NAME" ]
    then
        echo "$NOT_UPDATE_FILE_NAME found. So we don't do update."
    else
        if [ "$HOUR" == "$HOUR_RUN_STOCK" ] && [ "$MINUTE" == "$MINUTE_RUN_STOCK" ]; then
            date >> ${INFO_FILE}
            python main.py >> ${INFO_FILE}
        fi
    fi
    sleep 60
done
