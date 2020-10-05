# Patience

## Description

Strange... Everything looks the same. But there is some message hidden, I am sure!

[patience.pcap](challenge/patience.pcap)

## How to prepare the PCAP file

1. Run temporary server

```
./server.py
```

Generate the traffic between client and server and capture it:

```
sudo tcpdump -w ../challenge/patience.pcap host poc.nuke.tk and port 80 & (sleep 3 ; ./client.py ; sudo killall tcpdump)
```

## Solution

See [solution](solution/README.md)
