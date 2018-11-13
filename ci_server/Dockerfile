FROM centos/python-36-centos7 

RUN pip3.6 install connexion
RUN pip3.6 install fabric

COPY ./handler_endpoint /handler_endpoint

WORKDIR /handler_endpoint

RUN ./deploy.sh


