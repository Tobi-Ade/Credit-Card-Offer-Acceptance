FROM python:3.8-slim

WORKDIR /predict-app

COPY ["requirements.txt", "./"]

RUN pip install -r requirements.txt

COPY ["model.bin", "predict.py", "./"]

EXPOSE 9090

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9090", "predict:app"]