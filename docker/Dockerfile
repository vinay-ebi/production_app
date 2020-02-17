FROM continuumio/miniconda3
#Maintainer : Kaikala vinay
#Date : 4-02-2020
#Production App 
ENV DEBIAN_FRONTEND noninteractive
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
RUN apt-get update -y
RUN apt-get update --fix-missing && apt-get install uuid-runtime && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion python-pip python-dev build-essential

RUN apt-get install rabbitmq-server -y
RUN git clone https://github.com/vinay-ebi/production_app.git
COPY ./base.yml /base.yml
RUN conda env update -f /base.yml

WORKDIR /app
COPY ./production_init.sh .
RUN chmod +x production_init.sh
ENTRYPOINT ["./production_init.sh"]
