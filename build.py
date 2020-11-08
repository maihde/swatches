#!/usr/bin/env python
import json
import os
import optparse

parser = optparse.OptionParser()
parser.add_option("-b", "--rebuild", action="store_true", default=False)
parser.add_option("-e", "--executable") 
opts, args = parser.parse_args()

if not os.path.exists("output"):
    os.makedirs("output")

if opts.executable== None:
    if os.path.exists("./OpenSCAD-2019.05-x86_64.AppImage"):
        opts.executable = "./OpenSCAD-2019.05-x86_64.AppImage"
    elif os.path.exists("/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD"):
        opts.executable = "/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD"
    else:
        opts.executable= "openscad"

with open("swatches.json") as f:
    swatches = json.load(f)
    swatch_params = swatches.get("parameterSets", {})
    for name in sorted(swatch_params):
        if not os.path.exists("output/%s.stl" % name) or opts.rebuild:
            print("Building output/%s.stl" % name)
            os.system(" ".join([
                opts.executable,
                "-o",
                "output/%s.stl" % name,
                "-p",
                "swatches.json",
                "-P",
                name,
                "Configurable_Filament_Swatch_VW.scad",
            ]))
