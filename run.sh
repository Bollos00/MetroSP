#!/bin/sh

docker run \
    --publish=7474:7474 \
    --publish=7687:7687 \
    --volume=$(pwd)/data:/data \
    --volume=$(pwd)/logs:/logs \
    --volume=$(pwd)/conf:/conf \
    --volume=$(pwd)/plugins:/plugins \
    --env=NEO4J_AUTH=none \
    neo4j
