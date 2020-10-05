# Solution

"Patience" is a hint towards "time".

One can observe that HTTP server takes different time to respond. Sometimes it's ~100 ms, sometimes ~600 ms, sometimes ~1100 ms. Thus, some information could be transmitted using this covert timing channel.

We can interpret server delays as a morse code string. Delay >1000 ms is a space, delay >500 ms is a dash `-`, delay ~100 ms is a dot `.`.

Full solution using pyshark library: [solution.py](solution.py)
