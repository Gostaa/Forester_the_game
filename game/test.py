import re

with open("script.rpy", 'r', encoding='utf-8') as my_file:
    lines = my_file.readlines()

lines = [line.strip() for line in lines if line != '\n']

jumps = set()
labels = set()

for line in lines:
    jump = re.search(r'jump.+', line)
    label = re.search(r'label.+', line)

    if jump:
        jump_str = jump[0]
        jumps.add(jump_str[5:])
    else:
        pass

    if label and label[0] != 'label start:':
        label_str = label[0]
        labels.add(label_str[6:-1])
    else:
        pass

if set.issubset(jumps, labels) == False:
    print("Jumps do not match labels.\n",
          "Jumps without labels:", set.difference(jumps, labels), "\n",
          "Labels without jumps:", set.difference(labels, jumps))
else:
    print("Jumps match labels")


