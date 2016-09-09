import logging

from docker import Client

cli = Client(base_url='unix://var/run/docker.sock')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('docker-mutil-ssh')


def log(func):
    def wrapper(*args, **kw):
        resp = func(*args, **kw)
        if resp:
            logger.info(resp)
        return resp

    return wrapper


class Container(object):
    def __init__(self, name, image, env=None, port_bindings=None, detach=False):
        self.name = name
        self.image = image
        self.env = env
        self.host_config = cli.create_host_config(port_bindings=port_bindings)
        self.detach = detach
        self.id = self.create_container()['Id']

    @log
    def create_container(self):
        return cli.create_container(image=self.image, environment=self.env,
                                    detach=self.detach, host_config=self.host_config,
                                    name=self.name)

    @log
    def start(self):
        return cli.start(container=self.id)

    @log
    def stop(self):
        return cli.stop(container=self.id)

    @log
    def logs(self):
        return cli.logs(container=self.id)

    def inspect(self):
        return cli.inspect_container(container=self.id)
