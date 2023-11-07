#!/usr/bin/env python3
import argparse
from data import *
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dot",
    nargs="?",
    const=pathlib.Path("/dev/stdout"),
    type = pathlib.Path,
    help = "the output path of dot file"
)
parser.add_argument("-c", "--csv",
    nargs="?",
    const=pathlib.Path("/dev/stdout"),
    type=pathlib.Path,
    help = "the output path of csv file"
)
parser.add_argument("-j", "--json",
    nargs="?",
    const=pathlib.Path("/dev/stdout"),
    type=pathlib.Path,
    help = "the output path of json file"
)
parser.add_argument("-r", "--rel",
    nargs="?",
    const="window",
    type=str,
    help = "the output path of relplot file, default by interactive window"
)

args = parser.parse_args()
if args.dot:
    f = open(args.dot, "w")
    outputDot(f)
    f.close()
if args.csv:
    f = open(args.csv, "w")
    outputGnucladCsv(f)
    f.close()
if args.json:
    f = open(args.json, "w")
    outputJson(f)
    f.close()
if args.rel:
    outputRelplot(args.rel)
