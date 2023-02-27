'''
Topic: List Comprehension
You are given three integers  and  representing the dimensions of a cuboid along with an integer x, y and z .
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of n is not equal to i+j+k.

Sample Input 0

1
1
1
2
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
'''


#Code 

if __name__ == '__main__':
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))
    z = int(input("Enter the third number"))
    n = int(input("Enter the number"))
 
    
output  = [ [i,j,k] for i in range(x+1)  for j in range(y+1) for k in range(z+1) if i+j+k!= n]    
print(output)
    