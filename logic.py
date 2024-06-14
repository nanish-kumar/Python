def NAND (a, b):
   if a == 1 and b == 1:
      return False
   else:
      return True

# main function
if __name__=='__main__':
   print(NAND(0,0))
   print(NAND(1,0))
   print(NAND(0,1))
   print(NAND(1,1))