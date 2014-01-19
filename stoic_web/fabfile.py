from fabric.api import local
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def commit():
	local('pip freeze > '+BASE_DIR+'/requirements.txt')
	local('git add --interactive && git commit')
