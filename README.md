# sd2018b-exam2
**Icesi University**  
**Course:** Distributed Systems   
**Professor:** Daniel Barragán C.  
**Subject:** Artifact building for Continous Delivery  
**Email:** daniel.barragan at correo.icesi.edu.co  
**Student:** Juan Camilo Swan.  
**Student ID:** A00054620  
**Git URL:** https://github.com/juanswan13/sd2018b-exam2.git  

## Expected results
* Develop artifact automatic building for Continous Delivery  
* Use libraries of programming languages to perform specific tasks   
* Diagnose and execute the needed actions to achieve a stable infrastructure  

## Used technologies
* Docker  
* CentOS7 Box
* Github Repository
* Python3
* Python3 Libraries: Flask, Fabric
* Ngrok  

## Infrastructure diagram  
The desired infrastructure to deploy consists in three Docker Containers and one Docker Client with the following settings:

* Python:3.6-slim CI Server: this CT has a Flask application with and endpoint using RESTful architecture best practices. The endpoint has the following logic:   
  * A Webhook attached to a Pull Request triggers the endpoint.  
  * The endpoint reads the Pull Request content and validates if the PR is mergedd  
  * If merged, via the Docker Python SDK, the endpoint runs the required commands to build the Docker Artifact and push it to the local registry.  
* wernight/ngrok Ngrok: this CT creates a temporary public domain name to expose the CI Server's endpoint.  
* registry Registry: this CT is a private local registry where the created artifacts will be pushed.  
* Windows 10 Home Docker Client: this Docker Client will be used to pull the private registry's artifacts. 


![][1]  
**Figure 1**. Deploy Diagram  

## Introduction  

The current branch contains two key elements to deploy the infrastructure. The first one is the docker-compose.yml. This file contains the provisioning required for each CT. The second one is the ci_server folder that contains the Dockerfile and python script to build the CI Server Docker image. 

### docker-compose.yml:
the docker-compose.yml contains three services, that will be described above  
  
* **Registry:** This service refers to the private local Registry for Docker images that we are creating. It uses the a Docker image called Registry that Docker already provide to create this type of servers, it is attached to the port 443. It also has two self-signed SSL certificates created with OpenSSL. These certificates  allow the server to be secure and that clients can trust in it. they are located at ./certs.
```
swan-registry.icesi.edu.co:
        image: registry:2
        container_name: swan-registry.icesi.edu.co
        volumes:
            - './docker_data/certs:/certs'
        environment:
            - 'REGISTRY_HTTP_ADDR=0.0.0.0:443'
            - REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt
            - REGISTRY_HTTP_TLS_KEY=/certs/domain.key
        ports:
            - '443:443'
```
* **ngrok:** 
