FROM ubuntu:20.04

COPY ./src/ /app/

WORKDIR /tmp
RUN apt update 
RUN apt-get install -y python3 python3-pip curl fonts-ipafont
RUN curl -L -O https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.focal_amd64.deb
RUN apt install -y ./wkhtmltox_0.12.5-1.focal_amd64.deb
RUN pip3 install pipenv

WORKDIR /app

RUN pipenv install --system
RUN useradd app
RUN chown -R app /app

USER app
CMD python3 app.py