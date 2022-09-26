{}:
let
  name = "runXonY";
  pkgs = import (builtins.fetchTarball {
    url = "https://github.com/NixOS/nixpkgs/archive/78fd35f98e9411ddd2c31ef201a2fd8821bcd85a.tar.gz";
    sha256 = "08l09d3i96arid2ag77lx715hzyf47ybb7cajcsp3iia24jpl6d8";
  }) {};
  myPython = pkgs.python3.withPackages (
    p: with p; [
      ipython
      multimethod
      seaborn
      # default tk cannot handle system zoom,
      # qt5 will handle system zoom correctly,
      # and ipython `%matplotlib qt` also needs,
      pyqt5
    ]
  );
in
pkgs.mkShell {
  inherit name;
  buildInputs = with pkgs; [
    myPython
    qt5.full
  ];
  shellHook = ''
    # env
    export PYTHONPATH=${myPython}/${myPython.sitePackages}
    export debian_chroot=${name}
  '';
}
