#!/usr/bin/python3
print("%s" % "".join(chr(i) for i in range(97, 123) if chr(i) not in "qe"), end="")
