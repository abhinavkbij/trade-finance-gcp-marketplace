FROM ubuntu:18.04
RUN apt-get update \
    && apt-get install default-jdk -y\
    && apt-get install tesseract-ocr -y \
    && apt-get -y install poppler-utils \
    python3 \
    #python-setuptools \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove

ADD . /home/App
WORKDIR /home/App
COPY requirements.txt ./
COPY . .
RUN pip3 install -r requirements.txt

VOLUME ["/data"]
EXPOSE 4900
CMD ["python3","main.py"]