FROM python:3.12.6

WORKDIR /

COPY . .

RUN python -m pip install --user --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]