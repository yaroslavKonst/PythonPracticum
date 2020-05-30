#!/usr/bin/env python3

import os
import readline
import rlcompleter

history_file = os.path.expanduser("./cmdline_history")

if os.path.exists(history_file):
    readline.read_history_file(history_file)

readline.set_completer(rlcompleter.Completer().complete)
readline.parse_and_bind("tab: complete")

while A := input(">> "):
    print(f" {A}")

readline.write_history_file(history_file)
