import subprocess
import paramiko
import logging
from optparse import OptionParser


def set_options():
    parser = OptionParser()
    
    parser.add_option("-m", "--mode", default="local",
        help="interaction mode: ssh or local [default: %default]")
    parser.add_option("-i", "--host", default="127.0.0.1",
        help="[required in ssh mode] host ip to connect to: [default: %default]")
    parser.add_option("-u", "--user", default="root",
        help="[required in ssh mode] username: [default: %default]")
    parser.add_option("-k", "--password", default="",
    	help="[required in ssh mode] user\'s password: [default: %default]")
    parser.add_option("-p", "--port", default=22,
        help="[required in ssh mode] specify port: [default: %default]")

    return parser.parse_args()[0]


def main():
    options = set_options()
    package_name = "apache2"

    logging.basicConfig(level = logging.INFO)
    logger = logging.getLogger("GetApache")

    if options.mode == "local":

        logger.info("Started")
        subprocess.call(["sudo", "apt-get", "install", package_name])
        logger.info("Started")

    elif options.mode == "ssh":
        
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=options.host, username=options.user, password=options.password, port=options.port)

        logger.info("Started")
    
        command = 'sudo -S apt-get -y install %s' % package_name
        stdin, stdout, stderr = client.exec_command(command)

        logger.info(stdout.read())
        logger.info("Closed")

        client.close()
    
    else: 
        print "wrong options: use -h to get help"


if __name__ == "__main__":
    main()
