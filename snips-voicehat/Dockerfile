FROM snipsdocker/platform:arm-0.60.10

ENV TERM linux
ENV DEBIAN_FRONTEND noninteractive

# Install Dependencies for Voice Bonnet
RUN set -x && apt-get update -qqy \
    && apt-get upgrade -qqy && apt-get install -qqy \
      wget \
      apt-transport-https \
      bash \
      sudo\
    && echo "deb https://dl.google.com/aiyprojects/deb stable main" \
    | tee /etc/apt/sources.list.d/aiyprojects.list \
    && wget -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && apt-get update -qqy && apt-get install -qqy \
        raspberrypi-kernel-headers \
        aiy-voicebonnet-soundcard-dkms \
        aiy-dkms pulseaudio \
        leds-ktd202x-dkms \
        alsa-utils \
        git \
        python3 \
        python3-dev \
        python3-venv \
        python-pip \
        vim \
    && git clone https://github.com/google/aiyprojects-raspbian.git AIY-projects-python \
    && mkdir -p /etc/pulse/daemon.conf.d/ \
    && echo "default-sample-rate = 48000" | tee /etc/pulse/daemon.conf.d/aiy.conf \
    && apt-get -qqy autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN cd AIY-projects-python \
    && git checkout voicekit \
    && scripts/install-alsa-config.sh

COPY snips.toml /etc/snips.toml

ENTRYPOINT ["/opt/snips/snips-entrypoint.sh"]