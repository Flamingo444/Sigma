import base64

# Read the Python script and encode it to Base64
with open("RansomPython.py", "r") as f:
    encoded_script = base64.b64encode(f.read().encode('utf-8')).decode('utf-8')

# Write the encoded script to ransomEncoded.py
with open("ransomEncoded.py", "w") as out_file:
    out_file.write(encoded_script)
