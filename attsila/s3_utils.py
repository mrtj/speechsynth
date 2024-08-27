import boto3

def parse_s3_uri(s3_uri):
    parts = s3_uri.replace("s3://", "").split("/")
    bucket = parts[0]
    key = "/".join(parts[1:])
    return bucket, key

def create_s3_uri(bucket, key):
    return f"s3://{bucket}/{key}"

def create_presigned_url(s3_uri, expiration=3600):
    # Generate a presigned URL for the S3 object
    bucket_name, object_name = parse_s3_uri(s3_uri)
    s3_client = boto3.client("s3")
    response = s3_client.generate_presigned_url(
        "get_object",
        Params={"Bucket": bucket_name, "Key": object_name},
        ExpiresIn=expiration
    )
    return response
