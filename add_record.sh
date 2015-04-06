# cat add_record.sh
#!/bin/bash

HOST=$1
IP=$2
DOMAIN=$3
MODE=$4

RECORD="${HOST} IN A ${IP}"

# TODO:
# arg count check
# zonefile check
# validate ip
# add error handling

#checks args number
if [[ $# != 3 && $# != 4 ]]; then
	echo wrong args
	exit 1
fi

#checks if zone file exits
if [[ "$(ls | grep ${DOMAIN}.db)" == ""  ]]; then
	echo file not found
	exit 1
fi

if [ "$MODE" == "1" ]; then
        sed -i "" 's/'"$RECORD"'//g' ${DOMAIN}.db
elif [ "$(cat ${DOMAIN}.db | grep "${RECORD}")" == "" ]; then
	#checks if ip is valid
	echo "\n"$IP"\n"
 	if [[ ! $IP =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
 		echo wrong ip
 	     	exit 1
 	fi
 	OIFS=$IFS
 	IFS='.'
 	IP=($IP)
 	IFS=$OIFS
 	if [[ ${IP[0]} -gt 255 || ${IP[1]} -gt 255 || ${IP[2]} -gt 255 || ${IP[3]} -gt 255 ]]; then
                echo wrong ip
                exit 1
 	fi
        echo $RECORD >> ${DOMAIN}.db
fi

#service bind9 restart
