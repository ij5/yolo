FROM python:3

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY run.py ./

RUN apt update

RUN apt install -y libgl1-mesa-glx

CMD ["python", "run.py"]