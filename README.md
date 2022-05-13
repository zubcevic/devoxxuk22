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
