import subprocess
import paramiko
import logging
from optparse import OptionParser


logging.basicConfig(level = logging.INFO)
logger = logging.getLogger("GetApache")


def log(fn):
    def wrapper(*args, **kwargs):
        logger.info("Starting")
        return fn(*args, **kwargs)
    return wrapper



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


@log
def local_install(package_name):
    subprocess.call(["sudo", "apt-get", "install", package_name])


@log
def ssh_install(options, package_name):

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=options.host, username=options.user, password=options.password, port=options.port)

    command = 'sudo -S apt-get -y install %s' % package_name
    stdin, stdout, stderr = client.exec_command(command)
    logger.info(stdout.read())

    client.close()


def main():
    options = set_options()
    package_name = "apache2"

    if options.mode == "local":
        local_install(package_name)

    elif options.mode == "ssh":
        ssh_install(options, package_name)
    
    else: 
        logger.error("Invalid options, try --help")


if __name__ == "__main__":
    main()
