import requests

# Replace with your Pastebin API key
api_key = 'YOUR-KEY-HERE'

# Your paste content
paste_content = "This is the content of my paste."

# Set paste visibility (public, unlisted, private)
paste_visibility = 'public'

# Set paste expiration (N for Never, 10M for 10 minutes, 1H for 1 hour, etc.)
paste_expiration = '1H'

# Pastebin API endpoint
api_url = 'https://pastebin.com/api/api_post.php'

# Create a dictionary with the required parameters
data = {
    'api_dev_key': api_key,
    'api_option': 'paste',
    'api_paste_code': paste_content,
    'api_paste_private': paste_visibility,
    'api_paste_expire_date': paste_expiration
}
# https://pastebin.com/gtuG2gkt
# Make the POST request to create the paste
response = requests.post(api_url, data=data)

# Check if the request was successful
if response.status_code == 200:
    # Print the URL of the created paste
    print("Paste URL:", response.text)
else:
    print("Failed to create paste. Status code:", response.status_code)
