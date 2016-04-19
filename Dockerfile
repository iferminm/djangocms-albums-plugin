FROM bluszcz/djangocms
MAINTAINER Israel Fermín Montilla<iferminm@gmail.com>

RUN apt-get install aptitude -y
RUN aptitude update && aptitude upgrade -y
RUN aptitude install -y \
    python-virtualenv \

USER djangocms
WORKDIR /home/djangocms

RUN virtualenv --no-site-packages venv

