FROM python:3.6
MAINTAINER Thomas Lund Mathisen

ENV APP_DIR=/srv/app

RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR
ADD code.py $APP_DIR
ADD comparator.py $APP_DIR
ADD boards $APP_DIR

CMD ["bash"]