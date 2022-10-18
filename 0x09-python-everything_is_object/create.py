import os
  
# Parent Directory path
parent_dir = "G:/documents/PERSONAL DOCS/projects/ALX/alx-higher_level_programming/0x09-python-everything_is_object"
  
# Path
for i in range(1, 3):
    directory = '103-line' + str(i) + '.txt'
    path = os.path.join(parent_dir, directory)
    print("Directory '% s' created" % directory)
    f = open(path, "a")