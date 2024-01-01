# Use the official MongoDB image as a base image
FROM mongo:latest

# Expose MongoDB default port
EXPOSE 27017

# Copy initialization scripts into the container
COPY ./init-mongo.js /docker-entrypoint-initdb.d/