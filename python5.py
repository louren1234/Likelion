num = input();
num = int(num);

for j in range(1, num):
    print(" "*(num-j),"*"*(2*j-1));

for i in range(num):
    print(" "*i, "*"*(2*(num-i)-1));
