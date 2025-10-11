#Matrix Script


zipped = zip(*matrix)
decoded = "".join(["".join(tup) for tup in zipped])
regex = re.compile(r"(?<=[0-9A-Za-z])([^0-9A-Za-z]+)(?=[0-9A-Za-z])")
cleaned, _ = re.subn(pattern=regex, repl=' ', string=decoded)
print(cleaned)