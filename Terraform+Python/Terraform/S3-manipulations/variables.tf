variable "location" {
  type        = string
  description = "The project region"
  default     = "us-east-1"
}
variable "bucket_name" {
  type        = string
  description = "Name of the S3 bucket."
  default     = "give_me_a_name_please"
}
