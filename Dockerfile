FROM arm32v6/alpine:latest

RUN apk --no-cache add \
  bash \
  python3 \
  python3-dev \
  build-base \
  curl \
  gcc \
  g++ \
  flex \
  bison \
  linux-headers \
  sudo

COPY requirements.txt .
RUN adduser -u 1000 -G wheel -D alpine && \
  rm -rf /var/cache/apk/* && \
  python3 -m ensurepip && \
  pip3 install --upgrade pip setuptools && \
  if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
  if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
  rm -rf /root/.cache && \
  pip3 install --no-cache-dir -r requirements.txt

COPY . .
RUN pip3 install --no-cache-dir -e /train_controller/. && \
  chmod +x init.sh

EXPOSE 5000
VOLUME [ "/train_controller/" ]

CMD [ "/bin/bash", "/init.sh" ]
