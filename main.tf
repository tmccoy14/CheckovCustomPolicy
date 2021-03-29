terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "checkov_bucket" {
  bucket        = "checkov-test-bucket"
  acl           = "private"
  force_destroy = false

  tags = {
    Purpose = "checkov",

  }
}
