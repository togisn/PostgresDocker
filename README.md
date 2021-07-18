**PostgresDocker**
-----
Consist of:
* app -> extract, reformat and insert CSV into DB
* db -> postgres
* web -> serve http with port 8080

Prerequisites
-----
I assume you have installed Docker and it is running.

See the [Docker website](http://www.docker.io/gettingstarted/#h_installation) for installation instructions.

Environment
-----
| OS                      | Build   | App   | DB   | Web   |
| ----------------------- | ------- | ----- | ---- | ----- |
| Win7 ultimate 64bit     | OK      | OK    | OK   | OK    |
| Ubuntu 18 LTS 64bit     | OK      | OK    | OK   | OK    |

I notice that Docker on Windows may have its own specific IP.

Meanwhile, Linux can access localhost for both web and DB.

![web](https://i.imgur.com/f3tQfFI.png "web")

![DB](https://i.imgur.com/3WutMnl.png "DB")

Run without Build (image already pushed to Docker hub)
-----

Steps to run Docker image:

1. Clone this repo

        git clone https://github.com/togisn/PostgresDocker.git

2a. Run docker (windows)

        cd PostgresDocker
        docker-compose pull && docker-compose up

    This will take a few minutes.

2b. Run docker (linux)

        cd PostgresDocker
        sudo docker-compose pull && sudo docker-compose up

    This will take a few minutes.

3. Web will show this sequence indicating that it is started up

    ![web](https://i.imgur.com/xuCYuiK.png "web")

4. CSV extraction by app is finished when it shows the following sequence
    
    ![web](https://i.imgur.com/JCiIS4x.png "web")

5. Once everything has started up, you should be able to access the webapp via [http://localhost:8080/](http://localhost:8080/) on your host machine, and DB at port 5432

Build and Run Docker
-----

Steps to build and run a Docker image:

1. Clone this repo

        git clone https://github.com/togisn/PostgresDocker.git

2a. Build and run image (windows)

        cd PostgresDocker
        docker-compose down && docker-compose up --build

    This will take a few minutes.

2b. Build and run image (linux)

        cd PostgresDocker
        sudo docker-compose down && sudo docker-compose up --build

    This will take a few minutes.

3. Web will show this sequence indicating that it is started up

    ![web](https://i.imgur.com/xuCYuiK.png "web")

4. CSV extraction by app is finished when it shows the following sequence
    
    ![web](https://i.imgur.com/JCiIS4x.png "web")

5. Once everything has started up, you should be able to access the webapp via [http://localhost:8080/](http://localhost:8080/) on your host machine, and DB at port 5432