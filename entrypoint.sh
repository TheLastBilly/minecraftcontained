#!/bin/sh

/server_download.py

cd $MINECRAFT_ROOT

ln -s $MINECRAFT_ROOT/settings/* .
if [ ! -d $MINECRAFT_MAPS_DIR/$MINECRAFT_MAP_NAME ]; then
    mkdir $MINECRAFT_MAPS_DIR/$MINECRAFT_MAP_NAME
fi
ln -s $MINECRAFT_MAPS_DIR$MINECRAFT_MAP_NAME .
ln -s $MINECRAFT_ROOT/servers/$MINECRAFT_SERVER_VERSION/server.jar server.jar

envsubst < "server.properties.template" > "server.properties"
java -Xms"$MINECRAFT_JRE_RAM" -Xmx"$MINECRAFT_SERVER_RAM" -jar ./server.jar nogui