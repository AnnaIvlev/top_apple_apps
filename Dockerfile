FROM python:3.9

ADD bin .
ADD test .
ADD app.py .
ADD apple_apps_getter.py .
ADD README.md .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./app.py"]

