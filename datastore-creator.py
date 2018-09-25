import re
import csv
def getEntitities(text):
    try:
#         print(text)
        found = re.search(r"(resto_\w+)", text).group(1)
        print(text)

    except AttributeError:
        # AAA, ZZZ not found in the original string
        found = None
    return found    
fname="data/dialog-bAbi-tasks/dialog-babi-candidates.txt"
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
content=map(getEntitities,content)
content=filter(lambda a:a is not None,content)
entities=list(content)


_csv={}

def isRestuarantName(entity):
    if entity.endswith(("_phone","_address")):
        return False
    return True
def getLocation(text):
    return re.search(r"resto_([^_]+)", text).group(1)
def getPrice(text):
    return re.search(r"resto_[^_]+_([^_]+)", text).group(1)
def getCuisine(text):
    return re.search(r"resto_[^_]+_[^_]+_([^_]+)", text).group(1)
def getRating(text):
    return re.search(r"resto_[^_]+_[^_]+_[^_]+_([^_]+)", text).group(1)
restuarantNames=list(set(list(filter(isRestuarantName,entities))))
print(restuarantNames)
for rest in restuarantNames:
    _csv[rest]={"name":rest,
               "address":rest+"_address",
               "phone":rest+"_phone",
               "location":getLocation(rest),
               "price":getPrice(rest),
               "cuisine":getCuisine(rest),
               "rating":getRating(rest)
               
               }
print(_csv)
_csv=list(_csv.values())
keys = _csv[0].keys()

with open('data/dialog-bAbi-tasks/data-store.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(_csv)


