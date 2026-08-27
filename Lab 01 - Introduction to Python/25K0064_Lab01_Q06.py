# 6. Aliza scored 40 in Physics, 78 in Chemistry and 82 in Maths. Read these marks, store them in a dictionary keyed by subject, then print the average and the subject with the highest marks.

# Name: Sarim Raza Ansari
#Roll No: 25K0064
#Q6

dic={}

dic['Physics']=40
dic['Chemistry']=78
dic['Maths']=82

print("Average = ",sum(dic.values())/len(dic))
print("Subject : ",max(dic,key=dic.get), "| MArks: ",dic[max(dic,key=dic.get)])