from fabric.api import local


def commit():
	local('pip freeze > ../requirements.txt')
	local('git add --interactive && git commit')
