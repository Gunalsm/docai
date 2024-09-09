# see, i have one final json get from doc ai re process and that will be in gcs bucket folder ree 


# and now i need to post that json data like load that json data's to platform re but which platform not sure but those data's need to have post method to load those data ree  


# in pythn script can you guide mee reee 

# ok as sample code for now give me to to load into some platform as example


# Here's a sample Python script to post a JSON file from Google Cloud Storage (GCS) to a platform using a POST method.

# Assumptions:
# You have access to the GCS bucket.
# You want to load the JSON file from the GCS bucket into some platform using the POST method.
# For this example, I'll simulate sending the data to a placeholder platform, such as a mock API (e.g., https://jsonplaceholder.typicode.com/posts).
# You'll need:

# Google Cloud SDK (google-cloud-storage).
# requests library to make HTTP requests.

# pip install google-cloud-storage requests

# sample code:


import json
import requests
from google.cloud import storage

# Function to download the JSON file from GCS
def download_json_from_gcs(bucket_name, json_file_path):
    try:
        # Initialize a storage client
        client = storage.Client()

        # Get the bucket
        bucket = client.bucket(bucket_name)

        # Get the blob (file) from the bucket
        blob = bucket.blob(json_file_path)

        # Download the contents of the blob as a string
        json_data = blob.download_as_text()

        # Parse the string as JSON
        json_content = json.loads(json_data)
        
        return json_content
    except Exception as e:
        print(f"Error downloading JSON from GCS: {e}")
        return None

# Function to post JSON data to a platform (example API)
def post_json_data(api_url, json_data):
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(api_url, json=json_data, headers=headers)

        if response.status_code == 201 or response.status_code == 200:
            print(f"Successfully posted JSON data. Response: {response.json()}")
        else:
            print(f"Failed to post JSON data. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error posting JSON data: {e}")

if __name__ == "__main__":
    # Google Cloud Storage bucket name and JSON file path
    bucket_name = 'your-gcs-bucket-name'
    json_file_path = 'folder-path/your-json-file.json'

    # Example platform API URL (replace with actual platform URL)
    api_url = 'https://jsonplaceholder.typicode.com/posts'

    # Step 1: Download JSON data from GCS
    json_data = download_json_from_gcs(bucket_name, json_file_path)

    if json_data:
        # Step 2: Post JSON data to the platform
        post_json_data(api_url, json_data)
    else:
        print("No JSON data to post.")


# Key Steps:
# Download JSON from GCS:
# The download_json_from_gcs function connects to the GCS bucket, reads the JSON file, and parses it.
# Post JSON to Platform:
# The post_json_data function sends the JSON to the specified platform API using an HTTP POST request.
# Replace the following in the code:
# your-gcs-bucket-name: The name of your GCS bucket.
# folder-path/your-json-file.json: The path to the JSON file in your bucket.
# api_url: The actual API endpoint of the platform where you want to send the JSON data.
# For testing purposes, you can use the placeholder API URL provided (https://jsonplaceholder.typicode.com/posts), but replace it with the real API when you're ready.


# --------------------- as of now with above code where you loaded re


# In the code provided above, the JSON data is loaded from the Google Cloud Storage (GCS) bucket and then posted to an example API endpoint.

# Here's how the data flow works:
# Download JSON from GCS:

# The download_json_from_gcs function loads the JSON file from a Google Cloud Storage bucket into a Python dictionary (json_content).
# Post JSON to a platform:

# The post_json_data function sends the loaded JSON to an example platform (in this case, https://jsonplaceholder.typicode.com/posts) using an HTTP POST request.
# However, the example platform (https://jsonplaceholder.typicode.com/posts) is just a placeholder API for testing purposes. It doesn't actually store the data long-term but simulates a successful post.

# Where is it "loaded"?
# GCS to Python: The JSON data is fetched from GCS and loaded into a Python dictionary (json_content).
# Python to Platform: The dictionary is then sent to the platform as a POST request to the example API.
# To use this in your real platform:

# Replace the api_url with the real API endpoint of the platform where you need to post the JSON.
# Ensure that the platform can handle a POST request with JSON payload.
# If you want to load the data into another platform, you just need to change the api_url in the post_json_data function.


#sample code 2 -----------------------------------




import json
import requests
from google.cloud import storage

# Function to download the JSON file from GCS
def download_json_from_gcs(bucket_name, json_file_path):
    try:
        # Initialize a storage client
        client = storage.Client()

        # Get the bucket
        bucket = client.bucket(bucket_name)

        # Get the blob (file) from the bucket
        blob = bucket.blob(json_file_path)

        # Download the contents of the blob as a string
        json_data = blob.download_as_text()

        # Parse the string as JSON
        json_content = json.loads(json_data)
        
        return json_content
    except Exception as e:
        print(f"Error downloading JSON from GCS: {e}")
        return None

# Function to post JSON data to a platform (example API)
def post_json_data(api_url, json_data):
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(api_url, json=json_data, headers=headers)

        if response.status_code == 201 or response.status_code == 200:
            print(f"Successfully posted JSON data. Response: {response.json()}")
        else:
            print(f"Failed to post JSON data. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error posting JSON data: {e}")

if __name__ == "__main__":
    # Google Cloud Storage bucket name and JSON file path
    bucket_name = 'your-gcs-bucket-name'
    json_file_path = 'folder-path/your-json-file.json'

    # Example platform API URL (replace with actual platform URL)
    api_url = 'https://example-platform.com/post-endpoint'

    # Step 1: Download JSON data from GCS
    json_data = download_json_from_gcs(bucket_name, json_file_path)

    if json_data:
        # Step 2: Post JSON data to the platform
        post_json_data(api_url, json_data)
    else:
        print("No JSON data to post.")
