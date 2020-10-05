resource "aws_iam_access_key" "reader" {
  user = aws_iam_user.reader.name
}
