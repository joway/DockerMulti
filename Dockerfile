FROM     ubuntu:14.04
MAINTAINER joway wang "joway@gmail.com"

COPY sources.list /etc/apt/sources.list
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get update \
    && apt-get install -y openssh-server pwgen curl vim wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/run/sshd \
    && sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config

ADD ./endpoint.sh /tmp/endpoint.sh
RUN chmod +x /tmp/endpoint.sh

ENV HOME /root

WORKDIR /root
VOLUME /root

EXPOSE 22
CMD ["sh","/tmp/endpoint.sh"]