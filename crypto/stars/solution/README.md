# Solution

We have a hint about "stars" and "konstelacija" (constellation) in the challenge description. The main idea is prime factors of *n* are parts of [prime k-tuple](https://en.wikipedia.org/wiki/Prime_k-tuple). This is not entirely the same as "prime constellations", but very close term.

Assuming this, and knowing that prime number *n* is large, we should have prime factors very close to each other. If we assume there are *x* prime factors, then all of them should be approximately equal to root of degree x: `n ** (1/x)`. Then to find real factors, we need to search around this central number with some small offset.

See full [solution](solution.py).
