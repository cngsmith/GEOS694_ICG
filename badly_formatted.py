# This code was taken from ChatGPT after prompting it to write me bad code
# with "Can you generate me a script of Python code around 100 lines in length
# that does not use standard pep-8 formatting so that I can practice 
# identifying and fixing formatting and style issues? Please do not use classes
#  within the script"

import math,sys,random,time

def calcStuff(x,y,z):
    if x>y:
      result=x*y+z
    else:
          result=y*z-x
    return result

def printData(dataList):
  for i in range(0,len(dataList)):
        print("Index:",i,"Value:",dataList[i])

def generateNumbers(n):
 numbers=[]
 for i in range(n):
        numbers.append(random.randint(1,100))
 return numbers

def average(nums):
 total=0
 for n in nums:total+=n
 if len(nums)==0:return 0
 return total/len(nums)

def process(nums):
 processed=[]
 for i in range(len(nums)):
  if nums[i]%2==0:
        processed.append(nums[i]*2)
  else:
        processed.append(nums[i]+1)
 return processed

def main():
 print("Starting program")
 nums=generateNumbers(20)
 printData(nums)
 avg=average(nums)
 print("Average is",avg)
 processed=process(nums)
 print("Processed values:")
 printData(processed)
 for i in range(5):
  value=calcStuff(i,avg,processed[i])
  print("Calc",i,value)
 t=time.time()
 while time.time()-t<1:
  pass
 print("Done")

if __name__=="__main__":
    main()