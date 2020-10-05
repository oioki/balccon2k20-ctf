resource "aws_s3_bucket_object" "flag" {
  key    = "flag.txt"
  bucket = aws_s3_bucket.main.id
  source = "../src/flag.txt"

  content_type = "text/plain"
}
