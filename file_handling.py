##Initialize file pointer
# f = open('test.txt', 'r')
# text = f.read()
# print(text)
# ## Close the file pointer
# f.close()

# Professional Approach
with open('test.txt', 'r') as f:
    text = f.read()

print(text)

## Writing in file
with open('test2.txt', 'w+') as f:
    f.write('Hello.....')