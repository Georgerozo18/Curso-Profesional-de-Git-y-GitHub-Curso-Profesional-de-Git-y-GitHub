def find_volume(length=1, width=1, depth=1):
    return length * width * depth, width, f'your width is {width}'

result = find_volume(width=10)
print(result)