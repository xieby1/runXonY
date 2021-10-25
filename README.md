# runXonY

A timeline tree about  run X on Y.

X and Y could be soft/hardware, and any layers in computers' world.

This project was initially meant to track BT (Binary Translation) techs, while as time goes by, I found more and more related non-BT techs tangled with BT techs. All these BT and non-BT techs' goals are to run soft/hardware on different platform. So I change project's goal from "tracking BT techs" to "tracking runXonY techs".

Inspired by [Linux Distribution Timeline](https://github.com/FabioLolix/LinuxTimeline)

## Usage

### Github Page

The pre-built version is hosted on https://xieby1.github.io/runXonY/

### Build

make sure [gnuclad](https://launchpad.net/gnuclad/) and python3 is installed.

```
git clone https://github.com/xieby1/runXonY
cd runXonY
make
python3 -m http.server
```

Self-built web page is hosted on `127.0.0.1:8000`.

## Tech stack

* python3: translate runXonY.csv to gnuclad preferred format.
* [gnuclad](https://launchpad.net/gnuclad/): generate timeline graph.
* html/js/css: make timeline interactive.
  * [papaparse.js](https://github.com/mholt/PapaParse): parse csv file.

## Contributing

😃Feel free to open issues and pull requests.