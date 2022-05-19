#!/bin/bash

kubectl run timestamps --image=merishka/timestamps:latest --image-pull-policy=Never

sleep 5 # allow the pod to spin up correctly

echo $(date +%s) > deploy.txt

kubectl port-forward pods/timestamps 8000:80