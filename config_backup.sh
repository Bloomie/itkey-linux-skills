#!/bin/bash

#including config file
source config_backup.conf || exit 1

#getting nfs public dir
mkdir cfg_backup
mount -rw "${NFS_NAMESERVER}:/public" cfg_backup

#compressing some config files and forwarding output to log file
logger -s "$(tar --absolute-names -cvpzf cfg_backup/cfg_backup-$(date +'%d-%m-%Y-%H-%M-%S').tar.gz /etc/resolv.conf /etc/network/interfaces)" 2>> /var/log/netcfg_backup/cfg.log

#sending log file content
mail -s "backup log" "${MAIL_ADDRESS}" < /var/log/netcfg_backup/cfg.log

#carving out old versions
COUNTER=$BACKUP_COPIES_TO_STORE
find cfg_backup/ -name "cfg_backup_*"  | sort -r |  tail +$[COUNTER+1] | xargs rm -rf

#cleaning up
umount cfg_backup
rm -rf cfg_backup
