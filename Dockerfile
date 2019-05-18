FROM conda/miniconda3:latest

MAINTAINER acosta@gradiant.org

RUN apt-get update && apt-get install -y wget unzip git

COPY envs/ubuntu_environment.yml /envs/
RUN conda env create -f envs/ubuntu_environment.yml

ENV LANG C.UTF-8
