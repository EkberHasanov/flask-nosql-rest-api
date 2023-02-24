#!/bin/bash

THRESHOLD=80
API_ENDPOINT="http://127.0.0.1:8080/create"

while true; do
  MEMORY_USAGE=$(free | awk 'NR==2{printf "%.2f", $3*100/$2 }')
  if (( $(echo "$MEMORY_USAGE > $THRESHOLD" | bc -l) )); then
    curl -X POST -H "Content-Type: application/json" -d '{"message": "High memory usage detected"}' $API_ENDPOINT
  fi
  echo $MEMORY_USAGE
  sleep 5
done

