import os

class Version:
    def __init__(self, path: str, filename: str):
        v, self.sicht, _ = filename.split('_')
        mmp = v.split('.')
        self.major = int(mmp[0])
        self.minor = int(mmp[1])
        self.patch = int(mmp[2])
        self.path = path
        self.filename = filename

    def __lt__(self, other):
        if self.major != other.major:
            return self.major < other.major
        if self.minor != other.minor:
            return self.minor < other.minor
        return self.patch < other.patch

    def print(self):
        print(os.path.join(self.path, self.filename))


versions = []
paths = ["PDF", "PDF/latest"]
for path in paths:
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            continue
        if file.endswith(".pdf") and ("sicht" in file):
            versions.append(Version(path, file))

versions.sort()


for v in versions[:-2]:
    if v.path == "PDF/latest":
        os.rename(os.path.join(v.path, v.filename), os.path.join("PDF",
                                                                 v.filename))

for v in versions[-2:]:
    if v.path == "PDF":
        os.rename(os.path.join(v.path, v.filename),
                  os.path.join("PDF/latest", v.filename))

