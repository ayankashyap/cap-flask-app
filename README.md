# DOCKER-FLASK-APP

Prerequisites:
ensure docker is installed

1. Clone the repository:
```console
user@system: git clone https://github.com/ayankashyap/cap-flask-app.git
```
2. Cd into ./app 
```console
user@system: cd cap-flask-app/app
```

3. Build docker image
```console
user@system: docker build -t flask-docker:latest .
```

4. Run 
```console
user@system: docker docker run --name flask-docker -p 5001:5001 flask-docker.
```

5. The webapp should now be running on http://0.0.0.0:5001/

