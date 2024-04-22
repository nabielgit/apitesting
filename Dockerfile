FROM python:3.12.3-slim

#copy code from workspace into new directory pythonPytestApi
COPY . /pythonPytestApi
# set to working directory in container
WORKDIR /pythonPytestApi
# install the requirements
RUN pip3 install -r requirements.txt
# run entry-point and report.html is the test report
CMD pytest -v -s --html=report.html --self-contained-html

# FROM ubuntu:22.04 AS builder
# RUN apt-get update && apt-get install -y python3 python3-pip
# RUN pip3 install -U pytest
# RUN pip3 install requests
# RUN pip3 install pytest-html
# CMD python3 -m pytest -v -s