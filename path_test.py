import os

path_sequence = None

path_sequence = "Test_RSC_SY/Rookie"
list_sequence = []

for (root, directories, files) in os.walk(path_sequence):
    for file in files:
        print(file)
        list_sequence.append(file)

print(list_sequence)
print(len(list_sequence))

new_path = os.path.join(path_sequence, list_sequence[0])
print(new_path)