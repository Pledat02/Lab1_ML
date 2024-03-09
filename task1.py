# task1.1
print("input: ")
n = input()
list =[]
for i in range(int(n)) :
    x= input()
    list.append(int(x))
print(list)

def max() :
  max = list[0]
  for i in range(int(n)):
    if list[i]> max:
      max = list[i]
  return int(max)
print(max())
def min() :
  min = list[0]
  for i in range(int(n)):
    if list[i]< min:
      min = list[i]
  return int(min)
print(min())


print(sum(list))

list.sort()
print(list)

def count_positive():
  count =0
  for i in range(int(n)):
    if list[i] > 0:
      count = count+1
  return count
print(count_positive())

def count_negative():
  count =0
  for i in range(int(n)):
    if list[i] < 0:
      count = count+1
  return count
print(count_negative())

# task1.2
def s(n):
    mul = 1
    if(n==1):
        return n
    for i in range(int(n+1)):
      if i > 0:
       mul*=i
    return s(n-1)+mul
print(s(3))