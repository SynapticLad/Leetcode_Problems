
'''Without using any string methods, try to print the following:
 if n is prvided then print a string from 1 to n in a signle string

Example the input n is 5 then output will be string 12345
if input is 10 output will be string 12345678910
'''


#My solution

res=""
if 1<=n<=150:
    for i in range(n):
        res+=str(i+1)

    

print(res)

