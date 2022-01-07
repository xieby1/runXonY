#!/bin/python3

import csv

# column index
IDX_Type = 0
IDX_Name = IDX_Type + 1
IDX_Color = IDX_Name + 1
IDX_Parent = IDX_Color + 1
IDX_From = IDX_Parent + 1
IDX_To = IDX_From + 1
IDX_License=IDX_To + 1
IDX_Developer = IDX_From + 3
IDX_Guest = IDX_Developer + 1
IDX_GInterface = IDX_Guest + 1
IDX_ISA = IDX_GInterface + 1
IDX_Host = IDX_ISA + 1
IDX_HInterface = IDX_Host + 1
IDX_Rename = IDX_HInterface + 4


def nodeName(x):
    x = x.replace(' ', '')
    x = x.replace('!', '')  # FX!32
    x = x.replace('/', '') # WineX / ...
    x = x.replace('-', '')
    x = x.replace('.', '') # rev.ng
    x = x.lower()
    return x


def stopTime(f, t):
    if t=="":
        return f
    elif t=="x":
        return f
    elif t=="now":
        return ""
    else:
        return t


def color(c):
    if c=="":
        return "#000"
    else:
        return c


with open("./runXonY.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open("./gnuclad.csv", 'w', newline='') as gnucladfile:
        writer = csv.writer(gnucladfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in reader:
            if row[IDX_Type] == "#":
                continue
            elif row[IDX_Type] == "N":
                ## generate Node
                ### Type, Name, Color, Parent
                node = ["N", row[IDX_Name], color(row[IDX_Color]), row[IDX_Parent]]
                ### Start, Stop
                node +=[row[IDX_From], stopTime(row[IDX_From], row[IDX_To])]
                ### Icon, Description
                node += ["", ""]
                ### TODO: Rename
                node += row[IDX_Rename:]
                writer.writerow(node)
            elif row[IDX_Type] == "C":
                ## generate Connector
                ### From When, From
                conn = ["C", row[IDX_From], row[IDX_Parent]]
                ### To When, To, Thickness, Color
                conn +=[row[IDX_To], row[IDX_Name], 2, color(row[IDX_Color]), ""]
                ### TODO: Padding
                conn +=[""]*(len(node) - len(conn))
                writer.writerow(conn)

