resource "aws_iam_user_policy" "s3" {
  name = "S3"
  user = aws_iam_user.reader.name

  policy = jsonencode(
    {
      "Version" : "2012-10-17",
      "Statement" : [
        {
          "Effect" : "Allow",
          "Action" : "s3:GetObject",
          "Resource" : "${aws_s3_bucket.main.arn}/*"
        }
      ]
    }
  )
}
