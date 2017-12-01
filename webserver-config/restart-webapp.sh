#SHELL COMMANDS TO RESTART AUTHOR WEBSITE APPLICATION
#RUN COMMANDS INDIVIDUALLY (WILL REQUIRE PASSWORD) IN A SCREEN SESSION
#DETACH FROM SCREEN SESSION ONCE FINISHED
ACTIVATE_PATH="/home/jeremzu2/my-software/python-virtual-envs/author-website/bin/activate"
APP_DIR="/home/jeremzu2/github/stage/author-website/mysite"
source ${ACTIVATE_PATH}
sudo /etc/init.d/nginx restart
gunicorn mysite.wsgi
