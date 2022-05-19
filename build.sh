#!/bin/bash

eval $(minikube docker-env)

#docker build -t merishka/timestamps:latest .

echo $(date +%s) > data.txt

sh endpoints_build.sh