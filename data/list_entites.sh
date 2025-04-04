#!/bin/bash

NGSILD_URL="http://localhost:1026/ngsi-ld/v1/entities"

curl -G -X GET "$NGSILD_URL" \
    -H "Content-Type: application/ld+json" \
    -H "Accept: application/ld+json" \
    -d 'type=City' \
    -d 'options=keyValues' \
    -d 'attrs=https://schema.org/name,country' \
    -d 'limit=1000'
