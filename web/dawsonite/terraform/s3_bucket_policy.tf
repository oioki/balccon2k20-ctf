resource "aws_s3_bucket_policy" "main" {
  bucket = aws_s3_bucket.main.id

  policy = jsonencode(
    {
      "Version" : "2012-10-17",
      "Statement" : [
        {
          "Effect" : "Allow",
          "Principal" : "*",
          "Action" : [
            "s3:ListBucket",
            "s3:ListBucketVersions"
          ],
          "Resource" : aws_s3_bucket.main.arn
        }
      ]
  })
}
