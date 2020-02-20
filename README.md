# S3-Simple-Browser
Minimalist browser for Amazon S3, supporting also S3 on localstack.


![Alt text](wiki/buckets.jpg?raw=true "Title")
## Run on Docker

### Connect to S3 

Provide your AWS credentials as env variables:
```
docker run -it -p 8080:8080 
 -e AWS_ACCESS_KEY_ID=<aws access key id>> -e AWS_SECRET_ACCESS_KEY=<aws secret access key>  
    gcatanese/s3-simple-browser
```

### Connect to Localstack S3 

The docker-compose file in the repository provides a good starting point to use [localstack](https://github.com/localstack/localstack).   
It runs a local S3 instance and the S3 Simple Browser app.

Configure environment variables accordingly.

## Run from source

Clone the repository and add .env file in the root:  
```
AWS_ACCESS_KEY_ID = aws01
AWS_SECRET_ACCESS_KEY = aws01
# Uncomment to use localstack
#S3_LOCALSTACK_URL = http://localhost:4572
```
Run on the desired port
```
python manage.py runserver 8080
```


