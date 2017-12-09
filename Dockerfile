FROM train-power

COPY . .

RUN pip install -r /train_controller/requirements.txt && \
  pip install -e /train_controller/. && \
  chmod +x init.sh

EXPOSE 5000
VOLUME [ "/train_controller/" ]

CMD [ "/bin/bash", "/init.sh" ]