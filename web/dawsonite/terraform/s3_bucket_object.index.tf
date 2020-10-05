resource "aws_s3_bucket_object" "index" {
  key    = "index.html"
  bucket = aws_s3_bucket.main.id
  source = "../src/index.html"

  content_type = "text/html"
  acl          = "public-read"
}
