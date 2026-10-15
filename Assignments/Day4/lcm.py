def findLcm(n1, n2):
   i=1
   while True:
        if (n1*i)%n2==0:
            return n1*i
        i=i+1