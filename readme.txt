


docker build -t s3_simple_browser .


docker run -p 8000:8000 --rm -it --name s3_simple_browser s3_simple_browser
	
docker tag perosa/tsk registry.heroku.com/tweesky/web
docker push registry.heroku.com/tweesky/web
heroku container:release web -a tweesky


https://tweesky.herokuapp.com/webhook/status
heroku ps:scale web=0 -a tweesky


     