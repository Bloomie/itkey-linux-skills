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
        if [[ "$(echo $LINE | awk '{print $3}')" == "delete" ]]; then
                CMD=1
        else 
                CMD=0
        fi
        DOMAIN=$(echo $HOSTNAME | rev | cut -d . -f1,2 | rev)
        HOST=$(echo $HOSTNAME | rev | cut -d . -f3- | rev)
        echo $HOST
        echo $IP
        echo $DOMAIN
        ./add_record.sh $HOST $IP $DOMAIN $CMD

done

