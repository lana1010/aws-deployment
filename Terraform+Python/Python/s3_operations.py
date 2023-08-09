###############################################################################################################
# This script will upload the specified files to the S3 bucket, delete the specified objects from 
# the bucket, and describe the objects in the bucket based on the provided arguments and options.
#
# To run, replace <bucket_name>, <file_paths>, and <object_keys> with the appropriate values. 
# python s3_operations.py <bucket_name> --upload <file_paths> --delete <object_keys> --describe
# For example:
# python s3_operations.py lana-s3-test1 --upload index.html image.jpg notes.txt --delete notes.txt --describe
#
# Before to run this python script, set session Environment Variables:
# set AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_KEY_ID>
# set AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_ACCESS_KEY>
#
###############################################################################################################
'''
Create a python script to populate the bucket with some assets:
-The script should place a few objects in the bucket
-The script should also be able to delete objects in the bucket
-The script should be able to describe the objects in the bucket
-The script should take command line arguments
'''

import boto3
import argparse

AWS_DAFAULT_REGION = "us-west-1"

def create_s3_client():
    return boto3.client('s3')
    
# Upload the files specified in the the command line to S3 bucket
def upload_objects(s3_client, bucket_name, file_paths):
    for file_path in file_paths:
        object_key = file_path.split('/')[-1]  # Get the filename as the object key
        try:
           s3_client.upload_file(file_path, bucket_name, object_key)
           print(f"Uploaded {file_path} to S3 bucket {bucket_name} as {object_key}")
        except Exception as e:
           print(f"Error uploading file to S3: {e}")
        
# Delete the files specified in the the command line to S3 bucket
def delete_objects(s3_client, bucket_name, object_keys):
    for object_key in object_keys:
        try:
           response = s3_client.delete_object(Bucket=bucket_name, Key=object_key)
           print(response)
           print(f"Deleted object {object_key} from S3 bucket {bucket_name}")
        except Exception as e:
           print(f"Error deleting file to S3: {e}")   
           
# List existing objects/files in S3 bucket
def describe_objects(s3_client, bucket_name):
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    objects = response.get('Contents', [])
    if not objects:
        print(f"No objects found in S3 bucket {bucket_name}")
    else:
        print(f"Objects in S3 bucket {bucket_name}:")
        for obj in objects:
            print(f"- {obj['Key']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage objects in an AWS S3 bucket.")
    parser.add_argument("bucket_name", help="Name of the S3 bucket.")
    parser.add_argument("--upload", nargs="+", help="Paths of files to upload to the bucket.")
    parser.add_argument("--delete", nargs="+", help="Keys of objects to delete from the bucket.")
    parser.add_argument("--describe", action="store_true", help="Describe objects in the bucket.")
    args = parser.parse_args()

    s3_client = create_s3_client()

    if args.upload:
        upload_objects(s3_client, args.bucket_name, args.upload)

    if args.delete:
        delete_objects(s3_client, args.bucket_name, args.delete)

    if args.describe:
        describe_objects(s3_client, args.bucket_name)