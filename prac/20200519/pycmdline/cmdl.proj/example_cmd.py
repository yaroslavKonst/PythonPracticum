#!/usr/bin/env python3

import os
import cmd

class Parser(cmd.Cmd):
    intro = "Hello, whoever you are!"
    prompt = "[enter command] >$ "

    def do_up(self, *args):
        """Print up
        """
        print("up", args)

    def do_hello(self, *args):
        """Print hello
        """
        print("hello", args)

    def do_eof(self, line):
        """Quit
        """
        print("Bye!")
        return True

    def precmd(self, line):
        return line.lower()

    def complete_hello(self, text, line, begin, end):
        all_comms = ["welcome", "world"]
        a = [i for i in all_comms if i.startswith(text.split()[-1])]
        return a if len(a) > 0 else all_comms

Parser().cmdloop()
