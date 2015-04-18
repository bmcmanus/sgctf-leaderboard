#!/bin/bash

# To set DockerHub Repo or TAG from the command line:
#   $ TAG="latest" DHREPO="jetsnoc/sgctf" ./build.sh -e

if [ -z "$TAG" ]; then
    TAG="latest"
fi
if [ -z "$DHREPO"]; then
    DHREPO="jetsnoc/sgctf"
fi

# Check for and pull latest changes from remote branch
git pull

# Initialize submodules if they don't exist already
# git submodule init

# Pull the current commit hash. If different then before,
# it will update the submodule to the correct hash.
# git submodule update

# Build a docker image 
docker build -t $DHREPO:$TAG --no-cache .
RESULT=$?
if [[ $RESULT != 0 ]]; then
    echo "Failed build."
    exit $RESULT
fi

###
# To push the built container to the remote repository
# after a successful build:
#   $ ./build.sh -e
###
if [[ $@ == **-e** ]]; then
    docker push $DHREPO:$TAG
fi

