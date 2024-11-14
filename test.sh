#!/bin/bash

echo "Testing Ollama and Flask..."

# Test Ollama directly
echo -n "Testing Ollama service: "
if curl -s "http://localhost:11434/api/tags" > /dev/null; then
    echo "OK"
else
    echo "FAILED"
    exit 1
fi

# Test simple generation
echo -n "Testing Ollama generation: "
RESPONSE=$(curl -s -X POST http://localhost:11434/api/generate \
    -d '{"model":"llama2","prompt":"test","stream":false}')
if [ $? -eq 0 ]; then
    echo "OK"
else
    echo "FAILED"
    echo "Response: $RESPONSE"
    exit 1
fi

# Test Flask health endpoint
echo -n "Testing Flask health endpoint: "
if curl -s "http://localhost:5001/health" > /dev/null; then
    echo "OK"
else
    echo "FAILED"
    exit 1
fi

echo "All tests passed!"
