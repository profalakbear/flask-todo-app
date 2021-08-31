# pull official base image 
FROM python:3.8-rc-stretch 
# set work directory 
WORKDIR /app 
# install dependencies 
RUN pip install --upgrade pip 
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt 

COPY . . 
EXPOSE 5000 

RUN chmod +x main.py
COPY init.sql /docker-entrypoint-initdb.d/10-init.sql
 
ENTRYPOINT  ["python", "main.py"]


#RUN chmod u+x ./entrypoint.sh
#CMD ["/bin/bash", "/app/docker-entrypoint.sh"]
#ENTRYPOINT ["./entrypoint.sh"]