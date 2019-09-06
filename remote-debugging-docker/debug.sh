#!/bin/bash

if [ "$1" == "start" ]; then
    docker build -t remote-debugging-docker .
    docker run -d -t -p 3000:3000 --name remote-dbg-docker remote-debugging-docker
elif [ "$1" == "stop" ]; then
    docker stop remote-dbg-docker
    docker rm remote-dbg-docker
fi