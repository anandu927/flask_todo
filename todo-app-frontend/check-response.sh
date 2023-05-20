#!/bin/bash

response=$(curl -s -o /dev/null -w "%{http_code}" -H "Accept: application/json" --head http://localhost:3000)
if [[ $response == "200" ]]; then
    echo "Request succeeded. Proceed with building the image."
else
    echo "Request failed. Skipping the build. ${response}"
    exit 1
fi
