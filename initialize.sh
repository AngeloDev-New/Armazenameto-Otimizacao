rm -rf db
python script.py
docker stop mecanica_container
docker rm mecanica_container
docker build -t mecanica-db .
docker run -p 7000:3306 --name mecanica_container mecanica-db