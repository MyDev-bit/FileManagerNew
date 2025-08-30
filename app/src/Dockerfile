FROM python:3.11

WORKDIR /backend

COPY requriments.txt /backend/ .
COPY . /app/src /backend/ .

RUN pip install -r requriments.txt 

CMD ["python","api.py"]




