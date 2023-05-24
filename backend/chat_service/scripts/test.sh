export PYTHONPATH='.'

export DATABASE_URI='postgresql://usertestservices:testuser@localhost/swift_talk_test' 

clear
pytest -s -vvvv $1 $2
