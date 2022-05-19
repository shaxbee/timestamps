#!/bin/bash

eval $(minikube docker-env)

docker build -t timestamps/merishka:latest .

env build_time=$(date +%s)