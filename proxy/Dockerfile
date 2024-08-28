FROM nginx:1.27.1

EXPOSE 80


COPY ../frontend/index.html /usr/share/html/
COPY ../frontend/styles.css /usr/share/html/
COPY nginx.conf /etc/nginx/

RUN mkdir /usr/share/html
