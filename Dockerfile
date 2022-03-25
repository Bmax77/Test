FROM python:3.10.2-alpine3.15

RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -U pip \
    && python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org requests \
    && python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org flask
COPY server /app

ENTRYPOINT ["python3","/app/server_flask.py"]

# minikube image load <IMAGE_NAME>
# minikube image build -t <IMAGE_NAME> .

# docker run  -dit --publish 0.0.0.0:8080:8080 --env HOMEPATH=/home --restart always --name kibana-cloud gitlab-hrp.ru:5050/sre/initial/bmax1977/kibanacloud:latest

# docker image build -t gitlab-hrp.ru:5050/sre/initial/bmax1977/kibanacloud .
# docker push gitlab-hrp.ru:5050/sre/initial/bmax1977/kibanacloud