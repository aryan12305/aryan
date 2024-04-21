def marks():
    marklist=[]
    n=int(input("Enter the total number of students:"))
    for i in range (n):
        x=int(input("Enter the marks of student:"))
        marklist.append(x)
        if(x<0 or x>30):
            print("Invalid marks")
        total=0
        for i in marklist:
            j=int(i)
            total+=j
            avg=total/n
        min=31
        max=-1
        for marks in marklist:
            mark=int(marks)
            if(mark<min):
                min=mark
            if(max<mark):
                max=mark
        freq={}
        for mark in marklist:
            if mark !=None:
                if freq.get(mark)==None:
                    freq[mark]=1
                else:
                    freq[mark]+=1
        largestfreq=0
        largestfreqmark=0
        for mark in marklist:
            if(largestfreq<freq[mark]):
                largestfreq=freq[mark]
                largestfreqmark=mark
    print("The average marks of student in FDS is:",avg)
    print("Marks with highest frequency:",largestfreqmark)
    print("The highest score is:",max)
    print("The lowest score is:",min)
marks()
def absent():
    marklist=[1,2,3,"AB",5,"AB",9,"AB"]
    count=0
    for i in range (len(marklist)):
        if(marklist[i]=="AB"):
            count+=1
    print("Absent students are:",count)
absent()