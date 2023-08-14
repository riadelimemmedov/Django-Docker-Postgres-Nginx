#?Pull official base image
FROM python:3.11.4-slim-buster


#?Set working directory
RUN mkdir /code
WORKDIR /code


#?Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


#?Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


#?Install Netcat
RUN apt-get update && apt-get install -y netcat



#?Copy entrypoint.sh
# COPY ./entrypoint.sh ./backend
# RUN sed -i 's/\r$//g' ./backend/entrypoint.sh 
# RUN chmod +x ./backend/entrypoint.sh


#?Copy project
COPY . /code/


#?Application port
EXPOSE 8000


#?Run script on cmd terminal
CMD ["gunicorn","--chdir","backend","--bind",":8000","config.wsgi:application","--reload"]


#?Run entrypoint.sh
# ENTRYPOINT ["./backend/entrypoint.sh"]


#!After configuration run this command,create django-book image => sudo docker build . -t django-book  
#!Then run container => sudo docker run -p 8000:8000 django-book => First port number client port number,seconds is application port number
#!Go to inside the container => sudo docker -it 17727b689451 /bin/bash

