import random
import string

from container import Container

SSH_IMAGE = 'joway/docker-ssh'


def create_ssh_container(hostname, password=None, ssh_port=12222):
    if password:
        ENV = {'ROOT_PASS': password}
    else:
        ENV = None
    port_bindings = {
        22: ssh_port,
    }
    print('\n host:%s   port: %d    password: %s\n' % (hostname, ssh_port, password))
    return Container(name='ssh-' + hostname, image=SSH_IMAGE, env=ENV, port_bindings=port_bindings, detach=True,
                     mem_limit=512 * 1024 * 1024)


def random_pwd(length=12):
    return ''.join(
        random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for i in range(length))


def random_hostname(length=6):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def random_port(length=5):
    return (int(''.join(random.choice(string.digits) for i in range(length))) + 10000) % 65535
