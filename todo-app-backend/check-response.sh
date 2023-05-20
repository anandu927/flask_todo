#!/bin/bash

response=$(curl -s -w "%{http_code}" localhost:5000/todo)
if [[ $response == "200" ]]; then
    echo "Request succeeded. Proceed with building the image."
else
    echo "Request failed. Skipping the build. ${response}"
    exit 1
fi
