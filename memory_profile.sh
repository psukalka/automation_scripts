#! /bin/bash
#TODO: Install mail utils first: sudo apt install mailutils
HOSTNAME=`hostname -i`
SERVICES=("analysis_daemon" "sync_daemon" "worker_daemon")
get_free_memory(){
	FREE_MEMORY=$(free -m | awk 'NR==2{printf "%.2f%%\t\t", $4*100/$2 }')
	echo "$FREE_MEMORY"
}
get_disk_usage(){
	DISK=$(df -h | awk '$NF=="/"{printf "%s\t\t", $5}')
	echo "$DISK"
}
get_cpu_usage(){
	CPU=$(top -bn1 | grep load | awk '{printf "%.2f%%\t\t\n", $(NF-2)}')
	echo "$CPU"
}
get_stats(){
        TIME=$(date +"%T")
        FREE_MEMORY=`get_free_memory`
        DISK=`get_disk_usage`
        CPU=`get_cpu_usage`
        echo "$TIME    $FREE_MEMORY    $DISK    $CPU"
}
print_stats(){
        FILE="/tmp/stats.$(date +%F)"
	echo `get_stats` >> $FILE
}
is_service_running(){
        STATUS=`ps -ef | grep $1 | grep -v grep`
        if [ $?  -ne "0" ]; then
            echo "$1 stopped on $HOSTNAME sandbox" | mail -s "$1 stopped on $HOSTNAME sandbox" pavansukalkar@sigtuple.com
        fi
}
COUNT=0
while [ true ]; do
	#echo "$TIME    $FREE_MEMORY    $DISK    $CPU"
	print_stats
	TIME=`date +%M`
	#Check disk usage only once an hour
	if [ $TIME -eq "41" ]; then
		DISK=`get_disk_usage`
		if [ $DISK > "90%" ]; then
			echo "Disk is almost full on $HOSTNAME sandbox. Current usage is $DISK" | mail -s "Disk is almost full on $HOSTNAME sandbox" pavansukalkar@sigtuple.com
		fi
	fi
	if [ $COUNT -eq 12 ]; then
	        for i in ${!SERVICES[@]}; do
        	        service=${SERVICES[$i]}
                	is_service_running $service
			sleep 2
        	done
		COUNT=0
	fi
	COUNT=$((COUNT+1))
	echo $COUNT
	sleep 5
done
