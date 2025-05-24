def UploadToBlob(container, api_view, data):
    """
    Uploads the data to Azure Blob Storage.

    Args:
        fileName: The name of the file to be uploaded.
        data: The data to be uploaded.
   
    uploadable_data = convert_to_csv(data)
    try:
        blob_service_client = BlobServiceClient.from_connection_string(config.connection_string)
        blob_client = blob_service_client.get_blob_client(container=container, blob=f'{api_view}.csv')
        blob_client.upload_blob(uploadable_data)
        logger.info(f"Data uploaded to Azure Blob Storage: {api_view}")
    except Exception as e:
        print(f"Error uploading data to Azure Blob Storage: {e}")
        
        
def check_archive(self, api_view: str):
        try:
            blob_service_client = BlobServiceClient.from_connection_string(config.azure_storage_connection_string)
            blob_client = blob_service_client.get_blob_client(container=config.archive_container_name, blob=api_view)
            if blob_client.exists():
                return True
            else:
                return False
        except Exception as e:
            print(f"Error downloading data from Azure Blob Storage: {e}")
            return False
             """