print("0이상, 100 이하의 성적을 입력해주세요.");
num = input();
num = int(num);

if (num >= 90):
    print("A");
elif (num >= 80):
    print("B");
elif (num >= 70):
    print("C");
else:
    print("F");
