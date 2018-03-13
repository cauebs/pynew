import subprocess
from shlex import split


def run(command):
    p = subprocess.run(split(command),
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    return p.stdout.decode() or p.stderr.decode()
