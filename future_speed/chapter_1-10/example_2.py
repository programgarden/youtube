########################
#### 제어문
########################

########################
#### if문
########################
stock_name = "가스"
if stock_name == "가스":
    print("매수!")
print("밖이다")

stock_price = 6000
if stock_price < 3000:
    print("매수_1")
elif stock_price <= 3000:
    print("매수_2")
elif stock_price <= 5000:
    print("매수_3")
else:
    print("조건에 해당하는 게 없음!")


stock_price = 3000
if stock_price < 3000 or stock_price >= 3000:
    print("둘 중 아무거나 맞으면 출력")

stock_price = 3000
if stock_price < 2000 or stock_price < 2500:
    print("2000또는 2500 사이")
elif stock_price >= 2500 and stock_price <= 3000:
    print("2500 ~ 3000 사이")


##################
##### for
##################

for i in range(5, 100):
    print(i)


for i in range(5, 100):
    print(i)

    if i == 50:
        break

for i in range(0, 10):
    for k in range(0, 10):
        print("%s x %s = %s" % (i, k, i*k))

######################
##### while
#####################
count = 0
while True:
    count = count + 1

    if count == 10:
        break

    print("%s번째 매수" % count)

stock_buy = True
count = 0
while stock_buy:
    count = count + 1

    if count == 10:
        # break
        stock_buy = False

    print(count)


