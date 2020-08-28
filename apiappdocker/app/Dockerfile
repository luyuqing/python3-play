FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# yuqing_app:0.1.1
RUN apt-get install -y nano

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD ["app.py"]

# docker build -t yuqing_app:0.1.0 .
# docker run -d -p 5050:5050 yuqing_app:0.1.0          runs on localhost:5050
# docker run -d -e COLOR=pink -p 5000:5050 yuqing_app:0.1.0           runs on localhost:5000