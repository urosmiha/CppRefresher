import os
from flake8.api import legacy as flake8

root = '../../'
paths = []
for path, subdirs, files in os.walk(root):
    for name in files:
        if(name.endswith("subdir/subsub/hello.py")):
                paths.append(os.path.join(path, name))
        # print (os.path.join(path, name))

style_guide = flake8.get_style_guide(
    format='default',
)

report = style_guide.check_files(paths)
stat = report.get_statistics('E') == [], 'End od report'


for name in stat: print(name)


