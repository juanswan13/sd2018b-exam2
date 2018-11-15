FROM centos:7

#Install package
RUN yum install httpd


#Configuracion del puerto de postgres
EXPOSE 80
CMD sudo systemctl start httpd
CMD systemctl enable httpd

