# Helidon

[Helidon docs](https://helidon.io/docs/v2/)

## Prerequisites

+ Java 11 or higher
+ Maven 3.6 or higher
+ Helidon CLI

## Helidon CLI installatiom on Mac OS

    curl -L -O https://helidon.io/cli/latest/darwin/helidon
    chmod +x ./helidon
    sudo mv ./helidon /usr/local/bin/

## Create Maven project using Helidon CLI

    helidon init
    
Answer the interactive questions. Use MP for the flavor, and quickstart for the archetype.
Then go to the created maven project directory and follow the instructions from the generated README.md

## Build container image

    podman machine init
    podman build -t myhelidonimage -f Dockerfile.native .

    podman machine ssh
    curl -H 'Accept: application/json' -X GET http://localhost:8080/metrics

Error: error creating build container: short-name resolution enforced but cannot prompt without a TTY

docker.io/