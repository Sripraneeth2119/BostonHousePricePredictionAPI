#With the help of this file whatever we are writing, it will be done as a docker image and that docker image can be taken and can be run within a container
#If we don't create docker application, if we give this to another pc, then the pc should actually do all the wordk manually. So docker avoids this and it will maintain a base config and will help us to maintain the same base config across all the devices 
#From is used to select any base image
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
