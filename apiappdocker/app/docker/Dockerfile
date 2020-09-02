FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

RUN apt-get install -y nano

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD ["app.py"]

# docker build -f docker/Dockerfile -t yuqing_app .
# docker build -t yuqing_app:0.1.0 .

# docker run --name=my_app -p 5050:5050 yuqing_app
# docker run -d -p 5050:5050 yuqing_app:0.1.0          runs on localhost:5050
# docker run -d -e COLOR=pink -p 5000:5050 yuqing_app:0.1.0           runs on localhost:5000
# docker run -v /home/ubuntu/zzz.txt:/app/file.txt -p 5050:5050 yuqing_app