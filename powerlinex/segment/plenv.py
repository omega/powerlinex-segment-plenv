from __future__ import absolute_import
from subprocess import Popen, PIPE
import os


def readlines(cmd, cwd):
    p = Popen(cmd, shell=False, stdout=PIPE, stderr=PIPE, cwd=cwd)
    p.stderr.close()
    with p.stdout:
        for line in p.stdout:
            yield line[:-1].decode('utf-8')


def virtualenv(pl):
    try:
        for line in readlines(["plenv", "version"], os.getcwd()):
            # Now to process line
            if line[-9:-1] == "/version":
                return None
            else:
                return line.split(" ")[0]
    except OSError as e:
        if e.errno == 2:
            pass
        else:
            raise
