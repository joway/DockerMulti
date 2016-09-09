import argparse

from utils import create_ssh_container, random_hostname, random_pwd, random_port

parser = argparse.ArgumentParser(description='Docker Multi SSH')
parser.add_argument('number', type=int,
                    help='The number of the ssh-server containers you want to created')

args = parser.parse_args()
count = args.number

ssh_servers = []
tmp_ports = set()
for i in range(0, count):
    port = random_port()
    while port in tmp_ports:
        port = random_port()
        tmp_ports.add(port)
    tmp_ports.add(port)

    ssh_servers.append({
        'hostname': random_hostname(),
        'password': random_pwd(),
        'ssh_port': port
    })

for server in ssh_servers:
    container = create_ssh_container(server['hostname'], server['password'], server['ssh_port'])
    container.start()
