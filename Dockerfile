FROM python:3.10.6

WORKDIR /parser-py

COPY requirements.txt sample-data.json main.py ./

RUN pip install -r requirements.txt

CMD [ "python", "./main.py", "./sample-data.json" ]
