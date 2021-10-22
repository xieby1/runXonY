#!/bin/python3

import csv

# column index
IDX_Name = 0
IDX_Parent = IDX_Name + 1
IDX_OParent = IDX_Parent + 1
IDX_From = IDX_OParent + 1
IDX_To = IDX_From + 1
IDX_License=IDX_To + 1
IDX_Developer = IDX_From + 3
IDX_Guest = IDX_Developer + 1
IDX_GInterface = IDX_Guest + 1
IDX_ISA = IDX_GInterface + 1
IDX_Host = IDX_ISA + 1
IDX_HInterface = IDX_Host + 1


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


with open("./runXonY.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open("./gnuclad.csv", 'w', newline='') as gnucladfile:
        writer = csv.writer(gnucladfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        ## jump over first row in csv
        next(reader)
        for row in reader:
            ## generate Node
            ### Name, Color, Parent
            node = ["N", row[IDX_Name], "#000", row[IDX_Parent]]
            ### Start, Stop
            node +=[row[IDX_From], stopTime(row[IDX_From], row[IDX_To])]
            ### Icon, Description
            node += ["", ""]
            writer.writerow(node)
            ## generate Connector
            if row[IDX_OParent] != "":
                ### From When, From
                conn = ["C", row[IDX_From], row[IDX_OParent]]
                ### To When, To, Thickness, Color, csvPadding
                conn +=["", row[IDX_Name], 2, "#000", None]
                writer.writerow(conn)

