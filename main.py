def OR(a, b):
   if a == 1:
      return True
   elif b == 1:
      return True
   else:
      return False
# main function
if __name__=='__main__':
   print(OR(0,0))
   print(OR(1,0))
   print(OR(0,1))
   print(OR(1,1))