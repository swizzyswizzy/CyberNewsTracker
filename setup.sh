# (optional) Remove all container images
# docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)

# Create networking:

docker network create --subnet 10.48.0.0/16 --ip-range 10.48.81.0/24 cybernews_network

# 1. Build nginx image and copy configuration file

docker build -f Dockerfile.nginx -t cybernews_frontend .
docker run -p80:80 -it -d cybernews_frontend

# 2. Create python image (with a backend flask running)

docker build -f Dockerfile.backend -t cybernews_backend .
docker run -p9000:9000 -it -d cybernews_backend
