# Use an official Dart runtime as a parent image
FROM dart:stable

# Copy everything from the current directory to the working directory in the container
COPY ./src/ /app

# Install Dart Sass
RUN dart pub global activate sass

# Install vim
# RUN apt update -y && apt install vim -y

CMD ["sass", "--watch", "/app/:/app/"]

# Compile SCSS to CSS
# ENTRYPOINT sass styles.scss:styles.css

