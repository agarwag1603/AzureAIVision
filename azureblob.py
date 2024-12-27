from azure.storage.blob import  generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta,timezone

account_name = 'ai900storage1603'  # Replace with your storage account name
account_key = ''  # Replace with your storage account key
container_name='aidata' #Replace with the container name
#blob_name='advert.jpg'


def get_blob_url(id):
    if id=="OCR":
        blob_name='advert.jpg' #replace with blob name
    else:
        blob_name = 'store-camera-2.jpg' #replace with blob name
    #sas token generator to develop the image url which will be used by OCR and image analysis
    sas_token = generate_blob_sas(
        account_name=account_name,
        container_name=container_name,
        blob_name=blob_name,
        account_key=account_key,
        permission=BlobSasPermissions(read=True),
        expiry=datetime.now(timezone.utc) + timedelta(hours=1)  # Use timezone-aware UTC time
    )
    # Construct the full URL with SAS token
    sas_url = f"https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas_token}"
    return sas_url











