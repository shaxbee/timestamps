# timestamps

A webserver to access time stamps from scripts 

To run enter the following:
```
$ sh build.sh
$ sh deploy.sh 
$ sh endpoint.sh  
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

Endpoint:
```
/ 
```



