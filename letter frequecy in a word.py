w = input('Enter the word:- ')
l = list(w)


count = {}
for i in l:
    if i in count.keys():
       count[i] = count[i]+1
    else:
        count[i] = 1

for x in count.keys():
    if count[x]==1:
        print(x," occurs for ",count[x]," time")
    else:
        print(x," occurs for ",count[x]," times")
