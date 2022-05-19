#!/bin/bash

read -r build_time < data.txt #Read persisted data in the use case that you build an image now but not deploy immediately

curl -d '{"built_at":'$build_time'}' -H "Content-Type: application/json" -X POST http://0.0.0.0:8000/set_build_time