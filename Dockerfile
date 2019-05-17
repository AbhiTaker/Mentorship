FROM python:3

RUN apt-get update && apt-get upgrade -y
RUN apt-get install default-jdk -y
RUN mkdir /app
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
COPY . /app/
RUN chmod u+x entrypoint.sh
CMD sh entrypoint.sh
