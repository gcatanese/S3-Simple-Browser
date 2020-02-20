# S3-Simple-Browser
Minimalist browser for Amazon S3, supporting also S3 on localstack.


![Alt text](wiki/buckets.jpg?raw=true "Title")
## Run on Docker

### Connect to Amazon S3 

```
docker run -it -p 8080:8080 
 -e AWS_ACCESS_KEY_ID=<aws access key id>> -e AWS_SECRET_ACCESS_KEY=<aws secret access key>  
    gcatanese/s3-simple-browser
```

### Connect to Localstack S3 

```
docker run -it -p 8080:8080 -e AWS_ACCESS_KEY_ID=<localstack access key id>> 
 -e AWS_SECRET_ACCESS_KEY=<localstack secret access key> 
  -e ENDPOINT_URL=http://localhost:4572 gcatanese/s3-simple-browser
```

## Run from source

Clone the repository and add .env file in the root:  
```
AWS_ACCESS_KEY_ID = aws01
AWS_SECRET_ACCESS_KEY = aws01
S3_LOCALSTACK_URL = http://localhost:4572
```
Run on the desired port
```
python manage.py runserver 8080
```

