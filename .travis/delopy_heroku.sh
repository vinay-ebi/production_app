wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
heroku plugins:install @heroku-cli/plugin-container-registry
echo $DOCKER_PASS | docker login -u $DOCKER_USERNAME --password-stdin
echo $HEROKU_PASS | docker login -u $HEROKU_USER --password-stdin registry.heroku.com


docker login --username _ --password=$HEROKU_API_KEY registry.heroku.com
heroku container:push web --app $HEROKU_APP_NAME
heroku container:release web --app $HEROKU_APP_NAME
