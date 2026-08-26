# 11. Read the marks of 3 subjects into a dictionary with appropriate keys, then calculate the average and the percentage.
i=0
dic={}
while i<3:
    name=input("Enter subject name: ")
    marks=int(input("Enter marks: "))
    dic[name]=marks
    i+=1
avg=sum(dic.values())/len(dic)

print("Average: ",avg)
per=sum(dic.values())/300*100
print("Percentage: ",per)

    