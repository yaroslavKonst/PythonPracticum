from sys import * ; from math import *

a,b,c=map ( int,argv [ 1:4 ] )

d=b**2-4*a*c
if  d>0:
    x1,x2=( -b+sqrt ( d ) )/( 2*a ),( -b-sqrt ( d ) )/( 2*a )
    f=False
    if x1>0 :
    	x1,f=sqrt ( x1 ) ,True
    	print ( x1,-x1,end = ( " " if x2>=0 else "\n" ) )
    elif x1==0:
    	f=True
    	print ( x1,end = ( " " if x2>=0 else "\n" ) )
    if x2>0 :
    		x2,f=sqrt ( x2 ) ,True
    		print ( x2,-x2 )
    elif x2==0:
    	f=True
    	print ( x2 )
    if not f :
    	print ( "No roots" )
elif d==0 :
  x=-b/( 2*a )
  if x>0:
  	x=sqrt ( x )
  	print ( x,-x )
  elif x==0:
  	print ( x )  
  else :
  	print ( "No roots" )     
else:
	print ( "No roots" )    



