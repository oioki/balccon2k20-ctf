# Solution

The challenge file might resemble Base64 encoding, but it's not exactly it. It is [Base32](https://en.wikipedia.org/wiki/Base32), actually. *Twice* Cooler is a hint for 64 vs 32. distinctive feature -- it contains only capital letters.

By applying `base32 -d` several times, we get the flag. See [solution.sh]
