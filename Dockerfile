FROM python:3

WORKDIR /timestamp

COPY . /timestamp
RUN pip install -e .

ENV NAME timestamp

EXPOSE 80

CMD ["python3", "server.py"]