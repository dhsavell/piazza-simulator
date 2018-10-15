# piazza-simulator

> A set of scripts to build a Markov chain from a Piazza forum.

## Getting Started

To build a model, run scripts 0-2 in the `scripts/` directory. Each script will
output its usage when run without arguments.

Samples can be generated from script `3_simulate_piazza`.

## Distribution as a `par`

A self-contained Python archive (par) can be built using Bazel. First, use
scripts 0-2 to generate a model and place it in `self_contained/model.json`.
Then, the self-contained binary can be built and run like so:

```sh
$ bazel build //self_contained:piazza_simulator.par
$ ./bazel-bin/self_contained/piazza_simulator.par
```

Note that this is only necessary to distribute a self-contained version of the
script `3_simulate_piazza` with a model for use in other programs. If you just
want to generate a quick set of fake Piazza posts, you can just run the
scripts directly and skip over this process. This setup was made for a fairly
specific use case, but it might as well be part of the repository.
