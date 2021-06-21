# ![Docker](docker_horizontal.png)

| Images |
|----------------|
| Run docker image interactively |
| `#!bash docker run -it <image> bash` |
| Clean up dangling images |
| `#!bash docker image prune` |
| Clean up all images |
| `#!bash docker image prune --all` |
| Clean up unused data |
| `#!bash docker system prune` |

| Containers |
|-----------------|
| List docker containers |
| `#!bash docker container ls` |
| Kill a docker container |
| `#!bash docker container kill <container>` |
| Get IP address of a container |
| `#!bash docker inspect <container> | grep IP` |
