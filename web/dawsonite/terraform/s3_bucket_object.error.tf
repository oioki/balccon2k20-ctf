resource "aws_s3_bucket_object" "error" {
  key    = "error.html"
  bucket = aws_s3_bucket.main.id
  source = "../src/error.html"

  content_type = "text/html"
  acl          = "public-read"
}
