FROM python:3.9-buster

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV PYTHONPATH "${PYTHONPATH}:/app/"

COPY . .

CMD ["python", "src/main/main.py"]