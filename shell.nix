{}:
let
  name = "runXonY";
  pkgs = import <nixpkgs> {};
  myPython = pkgs.python3.withPackages (
    p: with p; [
      ipython
      multimethod
      matplotlib
      numpy
    ]
  );
in
pkgs.mkShell {
  inherit name;
  buildInputs = with pkgs; [
    myPython
    gnuclad
    mdbook
    nodePackages.typescript
    pandoc
  ];
  shellHook = ''
    # env
    export PYTHONPATH="${myPython}/${myPython.sitePackages}:''$(realpath scripts)"
    export debian_chroot=${name}
  '';
}
