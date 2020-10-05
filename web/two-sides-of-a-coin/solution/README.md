# Solution

This challenge demonstrates that some *pseudo* random number generators are actually predictable if one knows the seed which was used to initialize it.

Having source code available, one can spin up the application locally and test it.

Our challenge has read-only mode enabled, however locally one can disable it and actually create new advertisement on a bulletin board. When it's created, the user is redirected to editor-side view with a separate URL. Therefore, each advertisement has 2 sides: viewer-side (public), and editor-side (available "only" to creator of the advertisement).

The flaw here is that random IDs for these URLs are created using a PRNG from random numbers in the same random sequence. Therefore, one can brute force a seed trying to repeat the same pseudo random sequence. However, we need to consider a few important points:

1. We need to use the time when the advertisement was posted. This will reduce bruteforce volume by a lot.

2. The timestamp seed is rounded to 0.0001 sec

3. There are several advertisements, and flag could be in any of these.

This [solution](solution.py) takes all points into account, and the flag is behind one of editor-side URLs.
