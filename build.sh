#!/bin/bash

# Get the Git commit hash
eval $(minikube docker-env)

COMMIT_HASH=$(git rev-parse HEAD)

# Build the Docker image with the Git commit hash as part of the tag
docker build -t myflask:$COMMIT_HASH . && docker image prune