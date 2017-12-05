FROM piplates-base

COPY . .
RUN apk add --no-cache git
RUN pip install -r /train_controller/requirements.txt
RUN pip install -e /train_controller/.
RUN trainapi init

CMD [ "trainapi", "run" ]