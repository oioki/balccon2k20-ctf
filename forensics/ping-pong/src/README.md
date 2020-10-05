# Setup

## Customizable strings

```
PASSWORD="trustno1"
FLAG1="flag{its_the_old_flag_mate}"
KNOCK_WORD="pleasegivemeflag"
FLAG2="flag{good_job_you_found_it}"
```

## Setup 1: To produce PCAP file for the challenge

### Server

```
./hans -s 192.168.18.0 -p "$PASSWORD" -f -v
./ping-responder.py -i tun0 -t "$KNOCK_WORD" -s "$FLAG1"
tcpdump -i eth0 -nA -w tcpdump.pcap icmp and host "$YOUR_COMPUTER_IP"
```

### Client

```
>>> s='pleasegivemeflag'
>>> print(''.join([hex(ord(c)).replace('0x','') for c in s]))
706c65617365676976656d65666c6167

sudo ./hans -p "$PASSWORD" -c "$SERVER_IP" -f -v
ping 192.168.18.1 -c2 -p 706c65617365676976656d65666c6167
Ctrl+C on tcpdump
```


## Setup 2: Live production system

### Server

```
./hans -s 192.168.18.0 -p "$PASSWORD" -f -v
```

To scale pool of IP addresses, update `SUBNETS` constant in [hans.patch](hans.patch), recompile, run the server and run these commands to add more network aliases on tunnel interface:

```
ifconfig tun0 add 192.168.19.1 netmask 255.255.255.0
ifconfig tun0 add 192.168.20.1 netmask 255.255.255.0
...
```

Run ICMP custom responder:

```
./ping-responder.py -i tun0 -t "$KNOCK_WORD" -s "$FLAG2"
```
