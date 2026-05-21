#!/usr/bin/env python3
"""Run the landing site locally on http://localhost:5174/demo/chat"""
import os
import subprocess
import sys

root = os.path.dirname(os.path.abspath(__file__))

if not os.path.isdir(os.path.join(root, "node_modules")):
    print("Installing landing dependencies...")
    subprocess.run(["npm", "install"], cwd=root, check=True)

os.execvp("npm", ["npm", "run", "dev"])
