FROM python:3.6
COPY . ./app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["gunicorn", "-w 2", "-b 0.0.0.0:5000", "wsgi:app"]

