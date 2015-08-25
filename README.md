# swarm-bench: Benchmarking the Giant Swarm API

Running this benchmark requires a valid user account that actually
has access to a few environments and services.

As preparation, log in with the swarm CLI (using the API endpoint
you are going to use, if not the default). Then fetch the token
from `~/.swarm/token`.

## Executing the docker container

Call the docker container like this:

```
$ docker run --rm --name swarmbench \
   registry.giantswarm.io/giantswarm/swarmbench \
   -u <username> \
   -t <token>
```

Optionally, you can set the following additional flags:

- `-r`: Number of repetitions for the test (default 3)
- `--api-endpoint`: API endpoint, defaults to https://api.giantswarm.io/v1
- `--cluster-id`: Cluster ID, defaults to alpha.private.giantswarm.io

The `SWARM_*` environment variables are _not_ used.

## Executing without docker

If you don't want to execute this from a Docker container, call the `benchmark.py` script directly. You need the `requests` module installed (`pip install requests` or `sudopip install requests`). The command line arguments mentioned above apply here just the same:

```
$ python benchmark.py -u <username> -t <token>
```

## Resulting data

As a result, comma-separated values will be printed out to the standard output.

Note: If request errors occur, they might be mingled with the output.

Feel free to paste your results (tab-separated) here:

https://docs.google.com/spreadsheets/d/1u_SxYHxRX5F_h0JVVpH44pmZ57b9HLLEYZSVOJ0kZ7A/edit#gid=0

(Access restricted to Giant Swarm staff)

## Analysis

Store the output to `data.csv`. The file `swarm-bench.Rproj` can be
opened in RStudio to generate some box plots form the results.

