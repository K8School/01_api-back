# For more information, please refer to https://aka.ms/vscode-docker-python
FROM --platform=linux/amd64 python:3-slim-buster

EXPOSE 8000/TCP

# Keep Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=0

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install \
    python3-dev \
    build-essential



WORKDIR /app
COPY . /app

# Install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
#USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
