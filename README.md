# taldcrofts-nightmare

Repo: https://github.com/cdeil/taldcrofts-nightmare

## What is this?

Let's try to crash Astropy table!

This is a test for the Astropy fast CSV table code.

The goal is to see if we can make it segfault on invalid input.
See https://github.com/astropy/astropy/pull/5534#issuecomment-264434989

The idea is to use https://hypothesis.readthedocs.io/ to throw random
invalid ascii table files at it and see if it crashes.

## How to run it

First install `astropy` and `hypothesis`.

Then execute this and see what happens:

    python2 test_taldcroft.py
    python3 test_taldcroft.py

## TODO

- How can we run the parser without hitting the disk, looking for files?
- Set up grid of different parser configs
- Figure out what valid inputs are (unicode?) and valid responses (ValueError?)
- Figure out how to configure the hypothesis text strategy to test this well
