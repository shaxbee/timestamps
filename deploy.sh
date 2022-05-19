#!/bin/bash

kubectl run timestamps --image=timestamps/merishka:latest --image-pull-policy=Never

kubectl port-forward pods/timestamps 80:80