with import <nixpkgs> {};
let
  interpreter = python3.withPackages (p: [ p.setuptools ]);
in
  rec {
    script = writeScript "scan-deps.py" ''
    #! ${interpreter}/bin/python
    ${builtins.readFile ./script.py}
    '';
    runner = dir: runCommand "dependencies" {} ''
      cd ${dir}
      ${script} > $out
    '';
  }
