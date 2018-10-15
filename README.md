# piazza-simulator

> A set of scripts to build a Markov chain from a Piazza forum.

## Getting Started

To build a model, run scripts 0-2 in the `scripts/` directory. Each script will
output its usage when run without arguments.

Samples can be generated from script `3_simulate_piazza`.

## Distribution

A self-contained Python executable (pex) can be built using Please, a
Bazel-like build system chosen for the ability to easily include pip libraries.

Note that this is only necessary to distribute a self-contained version of the
script `3_simulate_piazza` with a model for use in other programs. If you just
want to generate a quick set of fake Piazza posts, you can just run the
scripts directly and skip over this process.

