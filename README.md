# timestamps

A webserver to access time stamps from scripts.

To run enter the following:
```
Ensure minikube is running
$ sh build.sh
$ sh deploy.sh 
$ sh endpoints_deploy.sh
Open 127.0.0.1:8000
```

## The API:

### POST methods

Endpoint:
```
/set_build_time
```
Request:
```
      {
        "built_at" : unix_timestamp
      }
```

Endpoint:
```
/set_deploy_time
```
Request:
```
      {
        "deloyed_at" : unix_timestamp
      }
```

GET methods:

Endpoint:
```
/health 
```
Note: This is for adaptability for future k8s usage. Specifically health and liveness probes.  


Endpoint:
```
/ 
```



