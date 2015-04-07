#!/bin/bash

#including config file
source config_backup.conf
if [[ $? -ne 0 ]]; then
	exit 1
fi

#getting nfs public dir
mkdir cfg_backup
mount -rw "${NFS_NAMESERVER}:/public" cfg_backup

#compressing some config files and forwarding output to log file
logger -s "$(tar --absolute-names -cvpzf cfg_backup/cfg_backup-$(date +'%d-%m-%Y-%H-%M-%S').tar.gz /etc/resolv.conf /etc/network/interfaces)" 2>> /var/log/netcfg_backup/cfg.log

#sending log file content
mail -s "backup log" "${MAIL_ADDRESS}" < /var/log/netcfg_backup/cfg.log

#carving out old versions
BACKUP_LIST="$(ls cfg_backup | grep 'cfg_backup' | sort -r)"
COUNTER=$BACKUP_COPIES_TO_STORE
for LINE in $BACKUP_LIST; do
	if [[ $COUNTER -le 0 ]]; then
		rm -rf "cfg_backup/${LINE}"
	fi
	COUNTER=$[COUNTER-1]
done	

#cleaning up
umount cfg_backup
rm -rf cfg_backup
