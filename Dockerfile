
FROM python:3.14.0a5-alpine3.21
WORKDIR /python-docker
RUN pip install flask 
RUN pip install pymongo 
COPY  . . 
EXPOSE 4000
CMD ["python" ,"./app.py"]
