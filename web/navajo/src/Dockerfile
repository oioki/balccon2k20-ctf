FROM httpd

RUN apt-get update && apt-get install -y curl python3 python3-requests

RUN echo "Include conf/extra/server-status.conf" >> /usr/local/apache2/conf/httpd.conf

COPY bin/ /usr/local/bin/

COPY apache2/ /usr/local/apache2/
