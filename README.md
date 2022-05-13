# devoxxuk22
Repository with examples of stuff learned at Devon UK 2022

+ [Helidon and Verrazzano](helidon/README.md)
+ [Python serialization pickle](pickle/README.md)
+ [JDK17 exercises](jdk17/README.md)

Other interesting links:

+ [Baeldung on Kotlin](https://www.baeldung.com/kotlin/kotlin-overview)

## Set up JDK 17 on MacOS

Check that maven is using the correct Java version.
If you installed maven using brew, the location is something like: /usr/local/Cellar/maven/3.8.2/bin/

    export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-17.0.1.jdk/Contents/Home/
    mvn -version

## Kotlin

Kotlin command line compiler

    brew install kotlin

VSCode extensions

+ Kotlin language (Matthias Frohlich)
+ Code Runner (Jun Han)

## Quarkus

+ Generate template Maven app using the web page [Quarkus.io](https://quarkus.io)

### Running in Dev mode

+ mvn compile quarkus:dev
+ [http://localhost:8080/q/dev/](http://localhost:8080/q/dev/)

Now you can continuously test the Reactive REST Easy endpoint

    curl http://localhost:8080/hello
### Running in normal app mode

+ mvn clean install
+ java -jar target/quarkus-app/quarkus-run.jar 
+ [http://localhost:8080/](http://localhost:8080)

In src/main/docker are 4 different Dockerfile 
+ 1 for normal JVM mode from what is found in target/quarkus-app after mvn clean install
+ 1 for uber/fat jar after mvn clean install -Dquarkus.package.type=legacy-jar and java -jar target/code-with-quarkus-1.0.0-SNAPSHOT-runner.jar
+ 2 for native build, where the native build is done by mvn clean install -Pnative which requires you to have GraalVM and native-to-image installed locally!

If you do not have it locally, you will get:

[ERROR]         [error]: Build step io.quarkus.deployment.pkg.steps.NativeImageBuildStep#build threw an exception: java.lang.RuntimeException: Cannot find the `native-image` in the GRAALVM_HOME, JAVA_HOME and System PATH. Install it using `gu install native-image`

A native build based on Java 11 can be made by [src/main/docker/Dockerfile.native2] as follows:

    podman build -t myquarkus -f src/main/docker/Dockerfile.native2 .
    podman run --rm --network=host myquarkus
