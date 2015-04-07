#!/bin/bash

#including config file
source config_backup.conf || exit 1
BACKUP_LOG_PATH="/var/log/netcfg_backup/cfg.log"
cp $BACKUP_LOG_PATH tmp
#getting nfs public dir
mkdir cfg_backup
logger -s "$(mount -rw "${NFS_NAMESERVER}:/public" cfg_backup || exit 1)" 2>> $BACKUP_LOG_PATH
#compressing some config files and forwarding output to log file
logger -s "$(tar --absolute-names -cvpzf cfg_backup/cfg_backup-$(date +'%d-%m-%Y-%H-%M-%S').tar.gz /etc/resolv.conf /etc/network/interfaces || exit 1)" 2>> $BACKUP_LOG_PATH

#carving out old versions
COUNTER=$BACKUP_COPIES_TO_STORE
find cfg_backup/ -name "cfg_backup_*"  | sort -r |  tail -n +$[COUNTER+1] | xargs rm -rf

#sending mail
diff $BACKUP_LOG_PATH tmp | mail -s "backup log" "${MAIL_ADDRESS}"

#cleaning up
umount cfg_backup
rm -rf cfg_backup
rm -rf tmp
