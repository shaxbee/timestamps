#!/bin/bash

read -r deployed_time < deploy.txt

curl -d '{"deployed_at":'$deployed_time'}' -H "Content-Type: application/json" -X POST http://0.0.0.0:8000/set_deploy_time