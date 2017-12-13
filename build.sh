docker build -t train-flask .
docker tag train-flask 10.127.16.10:5050/train-flask:latest
docker push 10.127.16.10:5050/train-flask:latest