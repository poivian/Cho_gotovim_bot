FROM python:3.12.4-slim AS builder

RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*
WORKDIR /src
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

FROM python:3.12.4-slim
RUN apt update && \
    apt install --no-install-recommends -y build-essential python3 && \
    apt clean && rm -rf /var/lib/apt/lists/*
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /src
CMD [ "python", "server.py" ]
EXPOSE 8001