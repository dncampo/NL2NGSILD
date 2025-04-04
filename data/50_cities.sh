#!/bin/bash
SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

curl --location 'http://localhost:1026/ngsi-ld/v1/entityOperations/upsert' \
--header 'Content-Type: application/json' \
-H 'Accept: application/ld+json' \
-d @"50_cities.json"
