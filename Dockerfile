FROM python:3.11

# ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000

ENV NAME World

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
