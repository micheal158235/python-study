#!/bin/sh

bool_flag=true

getSearchTyp()
{
    tFile="usr/local/exec/.parkingBox/.fix_info"
	tt=`grep "searchType" $tFile`
	for t in 1 2 3 1
	do
	        echo $tt | grep -q $tFile
			if [ $? == 0 ]
			then
			#        echo "searchType is" $t
			         return $t
		    fi
	done
	return 1
}

getSearchTyp
searchType=$?
pid=0
proc_num()
{
    num=`ps -ef | grep $1 | grep -v grep | wc -1`
	return $num
}
proc_id()
{
    pid=`ps -ef | grep $proc_name | grep -v grep | awk '{print $2}'`
}

while [ bool_flag=="true" ];do

    proc_num jsip_server
	number=$?
	if [ $number -eq 0 ]
	then
	        echo "jsip_server restart at : $restart_time" >> /mnt/storage/restart.log 2>&1
		cd /usr/local/exec/bin
		rm -f /usr/local/exec/bin/.user_list
		case $searchType in
		3)./jsip_server -L/mnt/storage -V -ws -c0300 >> /mnt/storage/jsip_server.log 2>&1&;;
		*)./jsip_server -L/mnt/storage -V -ws >> /mnt/storage/jsip_server.log 2>&1&;;
		esac
	fi
	
	proc_num BuzMain
	number=$?
	if [ $number -eq 0 ]
	then 
	    echo "BuzMain restart at : $restart_time" >> /mnt/storage/restart.log 2>&1
		cd /usr/local/exec/binEx/buzmain;
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
	    ./BuzMain >>/dev/null 2>&1&
	fi
	
	proc_num JSST.WebD.Host.dll
	number=$?
	if [ $number -eq 0 ]
	then
	    echo "JSST.WebD.Host.dll restart at : $restart_time" >> /mnt/storage/restart.log 2>&1
		cd /usr/local/exec/binEx/webd;
	./stop.sh
	    ./start.sh >>/dev/null 2>&1&
	fi
	
	if [ $searchType -eq 3]
	then
	    proc_num HD_LPR_Hi3536.out
		number=$?
		if [ $number -eq 0 ]
		then
		    echo "HD_LPR_Hi3536.out restart at : $restart_time" >> /mnt/storage/restart.log 2>&1
			#plate recognizer server
			cd /opt/car/
			./HD_LPR_Hi3536.out 0 40 1 > /mnt/storage/recognizer_server.log 2>&1 &
			cd -
		fi
	fi
	
	#proc_num httpd
	#number=$?
	#if [ $number -eq 0 ]
	#then
	#    echo "httpd restart at : $restart_time" >> /mnt/storage/restart.log 2>&1
	#    cd /usr/local/exec/bin;./httpd >> /mnt/storage/httpd.log 2>&1 &
	#fi
	
	proc_num main
	number=$?
	if [ $number -eq 0 ]
	then
	        restart_time=`date`
			echo "main restart at : $restart_time" >> /mnt/storage/restart.log 2>&1
			    killall -9 keep openRTSP hisibox
	    cd /usr/local/exec/bin; sleep 5 ;./main -qws >> /mnt/storage/main.log 2>&1 &
		touch /usr/local/exec/bin/.downflag
	fi
	
	proc_num pgConnectSvrApp
	number=$?
	if [ $number -eq 0 ]
	then 
	    echo "pgConnectSvrApp restart at : $restart_time" >> /mnt/storage/restart.log 2>&1
		cd /usr/local/exec/bin/pgConnectSvrApp; ./pgConnectSvrApp ./pgConnectSvr.cfg >> /mnt/storage/pgConnectsvr.log 2>&1 &
	fi
	
	if [ -f /usr/local/exec/ bin/.enable_cloud_server ]
	then
	    proc_num jsxmpp
		number=$?
		proc_num netService
		number1=$?
		
		if [ $number -eq 0] || [ $number -eq 0 ]
		then
		    killall -9 jsxmpp netService
			echo "jsxmpp restart at : $restart_time" >> /mnt/storage/restart.log 2>&1
			echo "netService restart at : $restart_time" >> /mnt/storage/restart.log 2>&1
			cd /usr/local/exec/bin
			./jsxmpp>>/mnt/storage/jsxmpp.log 2>&1 &
			./netService>>/mnt/storage/netService.log 2>&1 &
		fi
	fi
	
	sleep 5
done
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

































