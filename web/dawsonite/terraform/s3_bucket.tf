resource "aws_s3_bucket" "main" {
  bucket = "dawsonite.pwn.institute"
  acl    = "public-read"

  website {
    index_document = "index.html"
    error_document = "error.html"
  }

  versioning {
    enabled = true
  }
}
