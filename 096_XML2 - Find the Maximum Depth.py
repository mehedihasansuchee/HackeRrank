#XML2 - Find the Maximum Depth


if(level == maxdepth):
    maxdepth += 1

for child in elem:
    depth(child, level + 1)