# runXonY

A timeline tree about  run X on Y.

X and Y could be soft/hardware, and any layers in computers' world.

[![runXonY](gnuclad/gnuclad.svg)](https://xieby1.github.io/runXonY/)

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

## CSV syntax

The syntax of runXonY.csv is similar to [gnuclad](https://launchpad.net/gnuclad/). I add/drop some features on basis of gnuclad's syntax.

Every row in csv represents either a **comment (#)**, or a **node (N)**, or a **connector (C)**.

* **Comment (#)**: the whole row will be ignored
* **Node (N)**:
  * **Name**: project name, <u>case sensitive</u>, <u>unique</u> (can only be defined once)
  * **Color**: hex color code, like `#71B21F`, `#F60`, <u>default: #FFF (black)</u>
  * **Parent**: parent project name, <u>case sensitive</u>
  * **From**: project start time, `year.month.day`
  * **To**: project stop time, `year.month.day`, <u>default: **From**</u>
  * **License, Developer, Guest, Interface, ISA, Host, Interface, Tech, Feature, Info Source**: <u>optional</u>
  * **Rename, Time, Desc**: Project name change, <u>optinal</u>, can be add <u>repetitively</u>
* **Connector (C)**:
  * **Name**: <u>not unique</u> (can be defined multiple times)
  * **Color, Other Parent, From, To**: same to Node's
  * Other attributes will be ignored

User libreoffice as csv editor.
Two settings need to be changed:
Open csv -> Text Import -> Format quoted field as text
Save as -> Edit filter settings -> Quote all text cells

## Tech stack

* python3: translate runXonY.csv to gnuclad preferred format.
* [gnuclad](https://launchpad.net/gnuclad/): generate timeline graph.
* html/js/css: make timeline interactive.
  * [papaparse.js](https://github.com/mholt/PapaParse): parse csv file.

## Contributing

😃Feel free to open issues and pull requests.
