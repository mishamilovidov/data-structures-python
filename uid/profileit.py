#!/usr/bin/env python3

#   Profiles the base conversion code.  Run this from its parent directory:
#
#       python3 profileit.py
#

try:
    import cProfile as profile
except ImportError:
    import profile
from uid import generate

def main():
  # f = open("uids.txt","w+")

  for i in range(10000):
    generate(2)
    # f.write(generate() + '\n')
    # f.write(generate(2) + '\n')
    # f.write(generate(16) + '\n')
    # f.write(generate(58) + '\n')
    # f.write(generate(64) + '\n')

  # f.close()

# start things up!
prof = profile.Profile()
prof.runcall(main)
prof.print_stats()
