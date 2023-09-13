FROM python:3.11.4 as builder
COPY requirements.txt .

RUN pip install --user -r requirements.txt

ADD /api /

CMD ["python","-u","./endpoints.py"]
