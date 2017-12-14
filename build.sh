docker build --no-cache -t train-flask .
docker tag train-flask 10.127.16.10:5050/train-flask:latest
docker push 10.127.16.10:5050/train-flask:latest

ssh pirate@train-controller.local "docker pull 10.127.16.10:5050/train-flask && docker run  -it   --device /dev/spidev0.1     --device /dev/gpiomem     --rm     -p 5000:5000     10.127.16.10:5050/train-flask"