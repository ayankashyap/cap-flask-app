# DOCKER-FLASK-APP

Prerequisites:
ensure docker is installed

1. Clone the repository:
```console
user@system: git clone https://github.com/ayankashyap/cap-flask-app.git
```

2. Build docker image
```console
user@system: docker build -t flask-docker:latest .
```

3. Run 
```console
user@system: docker run --name flask-docker -p 5001:5001 flask-docker
```

4. The webapp should now be running on http://0.0.0.0:5001/

