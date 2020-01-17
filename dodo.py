# Our build file (using pydoit.org) for generating diagrams from all of our
# .asy files.

# We assume that all of our asy files are under week*/diagrams/ , and we want
# to generate them into .svg files.  Sometimes, they generate multiple files,
# so we'll parse them for the appropriate output filenames.

import os
import glob

def get_shipouts(fn):
    outfns = []
    with open(fn, "r") as f:
        for line in (_.strip() for _ in f):
            if line.startswith("shipout"):
                outfns.append(line[9:-3])
    return outfns

def task_build_asy():
    asy_files = sorted(glob.glob("week*/diagrams/*.asy"))
    for fn in asy_files:
        cd = os.path.normpath(
                os.path.join(
                    os.path.dirname(fn),
                    "..", "images"))
        os.makedirs(cd, exist_ok = True)
        yield {'basename': 'make_asy',
                'name': fn,
                'targets': [os.path.join(cd, _) for _ in get_shipouts(fn)],
                'file_dep': [fn],
                'actions': ['asy -cd %s %s' % (cd, 
                    os.path.join("..", "diagrams", os.path.basename(fn)))]
                }

