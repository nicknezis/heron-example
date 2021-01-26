Structure:
```
.
├── setup.py
└── src
    └── my_topology
        ├── __init__.py
        └── __main__.py
```
 * `setup.py` provides data for packaging up the files under it into a python package
 * `__init__.py` is so that `src/my_topology/` is discovered as a python package.
 * `__main__.py` is like the `if __name__ == "__main__":` thing in python, but in its own file so you can run the parent module (`my_topology` instead of a submodule e.g. `my_topology.entrypoint` if that _if_ was in a `my_topology/entrypoint.py`)

To build these into a pex, you can do
```shell
cd "$top_directory"
pex \
    --python=python3 \
    --entry-point=my_topology \
    --output=my_topology.pex \
    .
```
To submit to heron you can use the following pattern: `heron submit <artifact> - <topology name>`
```
heron submit my_topology.pex - my_topology
```

Trivia:
 * a pex is a zip file, so you can inspect the contents to see your packaged files, e.g. `unzil -l my_topology.pex | grep my_topology`
 * a pex can be executed (thanks to python executing zip files [e.g. "eggs"]) e.g. `./my_topology.pex` (what heron can do internally to get data about the topology)
