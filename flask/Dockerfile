FROM ubuntu:18.04

RUN apt-get update -y && apt-get install -y build-essential cmake \
libsm6 libxext6 libxrender-dev \
python3 python3-pip python3-dev

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install -r requirements.txt


# Step 4: copy all Project Files
COPY . /app

# Step 6:  run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
