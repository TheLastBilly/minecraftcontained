FROM alpine
LABEL maintainer="Jose Ricardo jtmonegro@gmail.com"

RUN apk update && apk add openjdk8-jre jq python3 py-pip gettext
RUN pip install requests

RUN mkdir /minecraft
RUN mkdir /minecraft/maps
RUN mkdir /minecraft/settings

COPY ./server_download.py /server_download.py
COPY ./entrypoint.sh /entrypoint.sh

CMD /entrypoint.sh