x=14
y=12
z=92
print("before swapping a = ",x," , b ",y," , c = ",z )
x=x + y + z
y= x - (y + z)
z= x - (y + z)
x= x - (y + z)
print("After swapping a = ",x," , b ",y," , z = ",z )