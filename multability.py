lst=[1,2,3,4,5]
tpl=(1,2,3,4,5)

lst1=list(tpl)
lst1.append(10)
tpl=tuple(lst1)
print(tpl)