# Pickle serialize - deserialize Python code

## Run the pickle.py 

[Override podman entrypoint](https://oprearocks.medium.com/how-to-properly-override-the-entrypoint-using-docker-run-2e081e5feb9d)
[Exploiting Python pickles](https://davidhamann.de/2020/04/05/exploiting-python-pickle/)

    export MYDATA=$(base64 pickle.py) 
    #podman machine ssh 'echo "$MYDATA" > pickle.py;ls'
    podman run --rm -ti -e MYDATA=$MYDATA docker.io/python:2.7.18 /bin/bash

    echo $MYDATA|base64 -d > pickle.py
    python pickle.py


    python3 pickle3.py