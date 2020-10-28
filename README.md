# minecraftcontained
A quick and dirty minecraft docker image for the lazy

## Setup
- Clone the [minecraftcontained](https://github.com/TheLastBilly/minecraftcontained) in your local machine
```bash
git clone https://github.com/TheLastBilly/minecraftcontained
```
- Set your server version and map name (and the other stuff if you **absolutely** know what you're doing) in **variables.env**
- **(Optional)** Create a folder called **maps** and put your map in there
- Use `docker-compose up -d` to start the server in **0.0.0.0:25565**
```
docker-compose up -d
```