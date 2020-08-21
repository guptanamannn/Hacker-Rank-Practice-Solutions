st=input()
strev=st[::-1]
ans=[]
j=0
replace=-1
for i in range(len(strev)):
    if j>=len(strev):
        break
    if strev[j]=='*':
        ans.append(strev[j+2])
        ans.append(strev[j+1])
        j=j+3
    elif strev[j]=='0': 
        ans.append(strev[replace])
        replace=replace-1
        j=j+1
    elif strev[j].isdigit() and strev[j]!='0': 
        pass
    else:
        ans.append(strev[j])
        j=j+1
print(''.join(ans[::-1]))
