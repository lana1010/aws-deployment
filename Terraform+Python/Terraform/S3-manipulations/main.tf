provider "aws" {
  region = var.location
}

resource "aws_s3_bucket" "onebucket" {
  bucket = var.bucket_name
}

resource "aws_s3_bucket_ownership_controls" "onebucket" {
  bucket = aws_s3_bucket.onebucket.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_acl" "onebucket" {
  depends_on = [aws_s3_bucket_ownership_controls.onebucket]
  bucket = aws_s3_bucket.onebucket.id
  acl = "private"
}

resource "aws_s3_bucket_versioning" "onebucket" {
  bucket = aws_s3_bucket.onebucket.id
  versioning_configuration {
    status = "Disabled"
  }
}
