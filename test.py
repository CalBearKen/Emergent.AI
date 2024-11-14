import requests
import json

url = "http://localhost:5001/api/generate"

initial_prompt = "You are to act as a Personal Identifiable Information (PII) detector. You will be given a sentence and you will need to determine if it contains any Personal Identifiable Information, even if it is obfuscated/masked or looks similar to PII. If it does, you will need to raise an alert to me by returning 'PII detected' without providing any other information. If it does not, you will need to return the original sentence. The sentence is: "
data = input('Please input data:')
payload = {
    "model": "llama3.2",
    "prompt": initial_prompt + data
}
headers = {
    "Content-Type": "application/json"
}



# Use stream=True to enable streaming
response = requests.post(url, json=payload, headers=headers, stream=True)

full_sentence = ""
buffer = ""
for chunk in response.iter_content(chunk_size=1024):
    if chunk:
        # Decode the chunk and add it to the buffer
        buffer += chunk.decode('utf-8')
        
        try:
            # Attempt to decode the JSON from the buffer
            chunk_json = json.loads(buffer)
            full_sentence += chunk_json['response']  # Accumulate the response
            buffer = ""  # Clear the buffer after successful decoding
        except json.JSONDecodeError:
            # If JSON is incomplete, continue accumulating
            continue

print("Full Sentence:", full_sentence)
