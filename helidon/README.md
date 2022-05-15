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

    podman machine init --memory=8000 --cpus=4 myvm --volume /Users --volume /Volumes
    podman machine start myvm
    
    podman build -t myhelidonimage -f Dockerfile.native .
    podman run --rm --network=host myhelidonimage
    podman machine ssh myvm
    curl -H 'Accept: application/json' -X GET http://localhost:8080/metrics


Just confirming that adding rootless_networking = "cni" under the [containers] section of ~/.config/containers/containers.conf does also fix this on MacOS :)

Podman on Mac requires you to update the Dockerfile image references with the repository identifier.

    Error: error creating build container: short-name resolution enforced but cannot prompt without a TTY

Use docker.io/ in front of the image id's.

https://github.com/quarkusio/quarkus/issues/1140
https://docs.podman.io/en/latest/markdown/podman-machine-init.1.html

The native build fails with the following message when the memory of the MacOS Podman VM is not big enough:

[INFO] 2022.05.11 18:49:42 WARNING io.helidon.common.HelidonFeatures Thread[main,5,main]: Feature 'REST Client' for path 'RESTClient' has limited support in native image: Does not support execution of default methods on interfaces.
[WARNING] Error: Image build request failed with exit status 137
[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  01:55 min
[INFO] Finished at: 2022-05-11T18:50:46Z
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal io.helidon.build-tools:helidon-maven-plugin:2.3.3:native-image (native-image) on project DevoxxUK: Image generation failed, exit code: 137 -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException
Error: error building at STEP "RUN mvn package -Pnative-image -Dnative.image.buildStatic -DskipTests": error while running runtime: exit status 1
