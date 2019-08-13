# Combine a bunch of setup.py files

This is a very simple and hacky script that collects requirements of setup.py
file. The files must provide `INSTALL_REQUIRES` and `TEST_REQUIRE` variables.
The `MANIFEST.in` files are also collected but not processed further.

# How?

You can run this in a nix repl to make use of the nix build sandbox since this script just evals random setup.py's.

```shell
$ nix repl ./default.nix
nix-repl> :b runer ../my-project
	out -> /nix/store/…-dependencies
```

The output file will then contain a JSON structure you can use for further processing.
