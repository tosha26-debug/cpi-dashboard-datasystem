import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# === 1. Fetch API data from AlphaVantage ===
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
url = f'https://www.alphavantage.co/query?function=CPI&interval=monthly&apikey={ALPHA_VANTAGE_API_KEY}'
r = requests.get(url)
data = r.json()

print(json.dumps(data, indent=4))

# === 2. Store as json file and save to local file ===
local_path = "./data"
os.makedirs(local_path, exist_ok=True)
local_file_name = "cpi_data.json"
upload_file_path = os.path.join(local_path, local_file_name)

with open(upload_file_path, "w") as f:
    json.dump(data, f)

# === 3. Upload to Azure Blob Storage ===
# Get Azure Storage account configuration from environment variables
account_name = os.getenv("AZURE_ACCOUNT_NAME")
account_url = f"https://{account_name}.blob.core.windows.net"
container_name = os.getenv("AZURE_CONTAINER_NAME", "inflation-data")

# Use DefaultAzureCredential for authentication
credential = DefaultAzureCredential()
blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

try:
    # Ensure the container exists or create it
    try:
        container_client = blob_service_client.create_container(container_name)
        print(f"Container '{container_name}' created.")
    except Exception:
        container_client = blob_service_client.get_container_client(container_name)
        print(f"Using existing container: '{container_name}'")

    # Create a blob client and upload the file
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    print("Upload complete.")

except Exception as ex:
    print("Exception occurred:")
    print(ex)
