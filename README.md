# Combine a bunch of setup.py files

This is a very simple and hacky script that collects requirements of setup.py
file. The files must provide `INSTALL_REQUIRES` and `TEST_REQUIRE` variables.
The `MANIFEST.in` files are also collected but not processed further.

# How?

You can just build the `run.nix` expression while passing the `dir` parameter.
`dir` should point to the root directory of all the python packages that you
want to combine.

```shell
$ nix-build run.nix --arg dir /some/where/packages
```

The output file will then contain a JSON structure you can use for further processing.
