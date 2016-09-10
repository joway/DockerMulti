# DockerMulti
基于 docker 实现轻量级多用户环境

### Install

1. git clone git@github.com:joway/DockerMulti.git
2. cd DockerMulti
3. pip install -r requirements.txt

### Usage:

1. `python docker_multi_ssh.py 10 --mem 128` # create 10 ssh docker server with 128M mem limit

    output:


        host:jthtjn   port: 64060    password: XG5MFTYUTGWR

        INFO:docker-mutil-ssh:{'Id': '65b3c4ea6d544070b887d955847baf1516b34d75a861453cc0e970699598e808', 'Warnings': None}

        host:anrigf   port: 14476    password: GDRtbNP8fWCv

        INFO:docker-mutil-ssh:{'Id': 'f0c4293db2af773c5fa39c26e924715051954e6c2e84bd1009fe6e15a4cb7535', 'Warnings': None}

        host:lozvyj   port: 7633    password: eJU1BJFo6W3v

        INFO:docker-mutil-ssh:{'Id': '49073a318c044039046cf6992c4bac5839149b80f5cdc85068093dddaa57dc6b', 'Warnings': None}

        ......

2. get your machine's ip : `ifconfig`

   (example: 123.100.100.12)
3. `ssh root@123.100.100.12 -p 64060 ` # the password for port 64060 is XG5MFTYUTGWR
4. you can custom the Dockerfile to create the environment you want