# cat mass_add_dns.sh
#!/bin/bash


#TODO:
# make it work
# add validation
# add error handling

HOSTFILE=$1
IFS=$'\n'

for LINE in `cat $HOSTFILE`; do
         
        HOSTNAME=$(echo $LINE | awk '{print $1}')
        IP=$(echo $LINE | awk '{print $2}')
        CMD=$(echo $LINE | awk '{print $3}')
        DOMAIN=$(echo $HOSTNAME | rev | cut -d . -f1,2 | rev)
        HOST=$(echo $HOSTNAME | rev | cut -d . -f3- | rev)
        echo $HOST
        echo $IP
        echo $DOMAIN
        if [[ "$CMD" == "delete" ]]; then
            	./add_record.sh $HOST $IP $DOMAIN 1
	else 
		./add_record.sh $HOST $IP $DOMAIN
  	fi

done

