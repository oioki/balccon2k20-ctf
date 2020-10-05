## Reasoning

Attentive player might notice that Navajo is an ethnic group closely related to Apache. Also, there is a "status" word in the challenge description. This points to widely-known [mod_status](https://httpd.apache.org/docs/2.4/mod/mod_status.html) feature of Apache web server. The default location for it is `/server-status`.

As an additional hint, we provided `robots.txt` file which also points to `/server-status`.

## Actual solution

Small extra difficulty is that flag is not always present in the server-status output.

Hence, we request `/server-status` endpoint until we get the flag:

    $ while true ; do curl -s http://localhost:8000/server-status | grep flag | grep -v flag\.txt ; done
    </td><td>127.0.0.1</td><td>http/1.1</td><td nowrap>10.200.0.3:80</td><td nowrap>GET /flag%7Bsecret_url_that_no_one_can_guess%7D HTTP/1.1</td></tr>
