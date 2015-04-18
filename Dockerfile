FROM python:2.7
MAINTAINER Brian McManus <brian@kickbackpoints.com>
ADD . /
RUN pip install -r /requirements.txt
WORKDIR /src
CMD python ctf.py
EXPOSE 5000
