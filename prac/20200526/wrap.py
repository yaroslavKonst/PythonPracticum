import sys
import subprocess

ex = sys.executable

print(subprocess.run([ex, sys.argv[1], *sys.argv[2:]], capture_output=True).stdout.decode("UTF-8"))
