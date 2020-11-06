#!/usr/bin/env python
import json
import os
import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-b", "--rebuild", action="store_true", default=False)
opts, args = parser.parse_args()

if not os.path.exists("output"):
    os.makedirs("output")

with open("swatches.json") as f:
    swatches = json.load(f)
    swatch_params = swatches.get("parameterSets", {})
    for name in sorted(swatch_params):
        if not os.path.exists(f"output/{name}.stl") or opts.rebuild:
            print(f"Building output/{name}.stl")
            subprocess.run([
                "./OpenSCAD-2019.05-x86_64.AppImage",
                "-o",
                f"output/{name}.stl",
                "-p",
                "swatches.json",
                "-P",
                f"{name}",
                "Configurable_Filament_Swatch_VW.scad",
            ])
