def max_of_three(a,b,c):
  if a > b and a > c:
      return  a
  elif b > a and b > c:
    return  b
  else:
    return  c
sum=max_of_three(1,2,3)
print(sum)

print("----------------------------------------------------------------------------------------------")

def max_of_three(a,b,c):
    sum=(a,b,c)
    return  sum


num2=int(input("enter a number : "))
sum=max_of_three(1,2,3)
print(sum)

