data "template_file" "config" {
  template = file("../src/config.0.js")

  vars = {
    aws_access_key_id     = aws_iam_access_key.reader.id
    aws_secret_access_key = aws_iam_access_key.reader.secret
  }
}

resource "aws_s3_bucket_object" "config_0" {
  key     = "config.js"
  bucket  = aws_s3_bucket.main.id
  content = data.template_file.config.rendered

  content_type = "text/javascript"
  acl          = "public-read"
}

resource "aws_s3_bucket_object" "config_1" {
  key    = "config.js"
  bucket = aws_s3_bucket.main.id
  source = "../src/config.1.js"

  content_type = "text/javascript"
  acl          = "public-read"

  depends_on = [
    aws_s3_bucket_object.config_0
  ]
}
