#!/bin/sh
set -e

ollama serve &

echo "Starting Ollama serve..."
sleep 5

echo "Downloading the model..."
ollama pull granite3-dense

# shellcheck disable=SC2039
wait -n
