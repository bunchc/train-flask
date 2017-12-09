FROM train-power

COPY . .

RUN pip install -r /train_controller/requirements.txt
RUN pip install -e /train_controller/.
RUN sudo trainapi init

EXPOSE 5000
VOLUME [ "/train_controller/" ]

CMD [ "trainapi", "run" ]