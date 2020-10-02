print("*****well come to helth management system*****")

def gettime():
    import datetime
    return datetime.datetime.now()
D1={1:"KUNTAL",2:"ROHAN",3:"RAM",}
D2={1:"EXA", 2:"FOOD",}
try:
      print("enter clint name:")
      for key, value in D1.items():
        print("press",key,"for",value, "\n")
      clint_name =int(input())
      print("select clint name:",D1[clint_name],"\n",end="")


      print("enter 1 for log:")
      print("enter 2 for retrieve:")
      n=int(input())
      if n is 1:
         for key,value in D2.items():
            print("press",key,"for",value,"\n",end="")
         job =int(input())
         print("you select:",D2[job],"\n",end="")
         f=open(D1[clint_name]+"_"+D2[job]+".txt","a")
         k='y'
         while(k is not "n"):
             print("enter",D2[job],"\n",end="")
             mytext=input()
             f.write(f"[{(str(gettime()))} {mytext} ","\n")
             k = input("add more ? y or n")
             continue
         f.close()
      elif n is 2:
           for key, value in D2.items():
             print("press", key, "for", value, "\n", end="")
           job=int(input())
           print(f"{D1[clint_name]}_{D2[job]} report", )
           f = open(D1[clint_name] + "_" + D2[job] + ".txt", "rt")
           contents=f.readlines()
           for line in contents:

               print(contents)
               f.close()
except Exception as e:

      print("invalid in put")