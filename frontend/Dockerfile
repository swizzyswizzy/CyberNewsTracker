# Use an official Dart runtime as a parent image
FROM dart:stable

# Set the working directory in the container
WORKDIR /app

# Copy everything from the current directory to the working directory in the container
COPY . /app

# Install Dart Sass
RUN dart pub global activate sass

# Compile SCSS to CSS
ENTRYPOINT sass styles.scss:styles.css

#CMD ["tail", "-f", "/dev/null"]
