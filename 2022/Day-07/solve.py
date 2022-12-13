class Directory:
    def __init__(self, path):
        self.items = []
        self.path = path
        self.name = path.split("/")[-1]
        self.directories = []
    def add_item(self, item):
        self.items.append(item)
        
    def get_name(self):
        return self.name
    
    def get_path(self):
        return self.path
    
    def get_size(self):
        return sum([item.get_size() for item in self.items])
    
    def get_subd(self, path):
        name = path.split("/")[1]
        path = path[len(name)+1:]
        for item in self.items:
            if type(item) == Directory and item.get_name() == name:
                if path != "/":
                    return item.get_subd(path)
                return item
        return None

class File:
    def __init__(self, path, name, size):
        self.path = path
        self.name = name
        self.size = size
    def get_size(self):
        return self.size


with open("input.txt") as file:
    data = file.read()


data = data.split("\n")
path = "/"
root = Directory("/")
filesystem = root
data.pop(0)
for line in data:
    if "$ cd " in line:
        if line[5:] == "..":
            path = "/" + "/".join(path.strip("/").split("/")[:-1]) + "/"
            if path == "//":
                path = "/"
        else:
            path += line[5:] + "/"
            filesystem = root.get_subd(path)
    elif "dir" in line:
        name = line.split(" ")[-1]
        filesystem.add_item(Directory(path+name))
        root.directories.append(path+name+"/")
    elif " ls" in line:
        continue
    else:
        size, name = line.split(" ")
        filesystem.add_item(File(path, name, int(size)))
        
count = 0
unused = 70000000 - root.get_size()
need = 30000000 - unused
possible = []
for path in root.directories:
    size = root.get_subd(path).get_size()
    if size < 100000:
        count += size
    if size > need:
        possible.append(size)


print(count)
print(min(possible))
    
    
