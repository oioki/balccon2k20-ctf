## Reasoning

From challenge description, we can understand that it's most probably about XOR operation, and message was encrypted using a key.

Running `strings ciphertext` reveals the string `{factors?}` which is a hint.

The size of the file is 1763 = 41 x 43.

One might guess that the message had length of 41 or 43 and was encrypted by a key of length 43 or 41, respectively.

## Actual solution

We know a priori, that flag (plaintext) should contain `flag{` string.

For the sake of simplicity, let's assume `len(flag) = 7` and `len(key) = 8`. If we assume plaintext to be `flag{x}` (7 bytes), we then have this per-byte operations:

```
    P1 P2 P3 P4 P5 P6 P7   P1 P2 P3  P4  P5  P6  P7    P1  P2  P3  P4  P5  P6  P7    P1  P2  P3  P4  P5  P6  P7    P1  P2  P3  P4  P5  P6  P7    P1  P2  P3  P4  P5  P6  P7    P1  P2  P3  P4  P5  P6  P7    P1  P2  P3  P4  P5  P6  P7
XOR
    K1 K2 K3 K4 K5 K6 K7   K8 K1 K2  K3  K4  K5  K6    K7  K8  K1  K2  K3  K4  K5    K6  K7  K8  K1  K2  K3  K4    K5  K6  K7  K8  K1  K2  K3    K4  K5  K6  K7  K8  K1  K2    K3  K4  K5  K6  K7  K8  K1    K2  K3  K4  K5  K6  K7  K8
 =
    E1 E2 E3 E4 E5 E6 E7   E8 E9 E10 E11 E12 E13 E14   E15 E16 E17 E18 E19 E20 E21   E22 E23 E24 E25 E26 E27 E28   E29 E30 E31 E32 E33 E34 E35   E36 E37 E38 E39 E40 E41 E42   E43 E44 E45 E46 E47 E48 E49   E50 E51 E52 E53 E54 E55 E56
```

So, here is `len(key)=8` copies of a flag encrypted in the whole ciphertext, and we can use that.

The flag could be offsetted, though. For example, if its known part, `flag{` (5 bytes) is stored starting from 2nd byte (offset=1):

```
    P2 P3 P4 P5 P6 = `flag{`
XOR
    K2 K3 K4 K5 K6
 =
    E2 E3 E4 E5 E6
```

Since XOR is a symmetric operation, we can derive part of a key having part of ciphertext E2:E6 and assuming the flag is at given offset (1):
```
(K2:K6) = `flag{` XOR (E2:E6)
```

Now, we can use this key part to decrypt other parts of plaintext:
```
(P3:P7)       = (K2:K6) XOR (E10:E14)
(P4:P7,P1)    = (K2:K6) XOR (E18:E22)
(P5:P7,P1:P2) = (K2:K6) XOR (E26:E30)
(P6:P7,P1:P3) = (K2:K6) XOR (E34:E38)
(P7,P1:P4)    = (K2:K6) XOR (E42:E46)
(P1:P5)       = (K2:K6) XOR (E50:E54)
```

In case of correct offset, this should decrypt to something meaningful. Otherwise, we try next flag offset.

See full [solution script](./solution.py)
