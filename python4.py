print("가격을 입력하세요.");
price = input();
price = int(price);

print("할인률을 입력하세요. 몇퍼센트 할인입니까?");
sale = input();
sale = int(sale);

total = price - price * sale/100;

print("할인된 가격은 : ", total ,"입니다.");
