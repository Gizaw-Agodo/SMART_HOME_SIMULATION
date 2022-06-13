def loadMaterial(filename):
    contents = {}
    mtl = None
    for line in open(filename, "r"):
        if line.startswith('#'):
            continue
        values = line.split()
        if not values:
            continue
        if values[0] == 'newmtl':
            mtl = contents[values[1]] = {}
        else:
            mtl[values[0]] = list(map(float, values[1:]))
    return contents
