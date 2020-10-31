from typing import Optional

from google.cloud import storage
from google.cloud.exceptions import NotFound


class FileUploader:
    """
        Class for creating a connection to google cloud storage. Object of the class can create bucket, upload
        file to the bucket and download files from the buckets.
    """
    def __init__(self, json_service_account: str, bucket_name: str):
        """
        Initialize client and getting or creating bucket

        :param json_service_account: path to json file of service key with keys
        :param bucket_name: name of bucket where will uploading and downloading
        """
        self.client = storage.Client.from_service_account_json(json_service_account)

        try:
            self.bucket = self.client.get_bucket(bucket_name)
        except NotFound:
            self.bucket = self.client.create_bucket(bucket_name)

    def upload_file(self, uploaded_file_name: str, storage_file_name: Optional[str] = None):
        """
        Uploading file to google cloud storage

        :param uploaded_file_name: file name of object to uploading to the bucket
        :param storage_file_name: file name that will have the file in google cloud storage
        """
        blob = self.bucket.blob(storage_file_name) if storage_file_name else self.bucket.blob(uploaded_file_name)

        blob.upload_from_filename(uploaded_file_name)

    def download_file(self, downloaded_file_name: str, storage_file_name: Optional[str] = None):
        """
        Downloading to local space file from google cloud storage
        :param downloaded_file_name: file name of file that we will download from google cloud storage
        :param storage_file_name: name of downloaded file in local
        """
        blob = self.bucket.blob(downloaded_file_name)

        blob.download_to_filename(storage_file_name if storage_file_name else downloaded_file_name)

    def list_blobs(self):
        """
        :return: list of blobs in the current bucket
        """
        all_blobs = list(self.client.list_blobs(self.bucket))

        return all_blobs


if __name__ == '__main__':
    file_uploader = FileUploader(r'E:\Projects\medicine_center\keys_service_account.json',
                                 'disease-history-files')

    lst = file_uploader.list_blobs()
    print(lst)
