FROM python:3.11


WORKDIR /admin_menu

COPY requriments.txt
COPY . /app/admin_menu

RUN pip install -r requriments.txt


CMD ["python","admin.py"]
