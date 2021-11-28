sample = 5 > 3
print(sample)

sample = 5 == 5
print(sample)

sample = 5 == 3
print(sample)

sample = 5 != 5
sample = 5 is not 5
print(sample)

sample = 5 == 5
sample = 5 is 5
print(sample)

sample = 5 > 3
sample = 5 >= 5
print(sample)

sample = 5 < 3
print(sample)
sample = 5 <= 3
print(sample)

# sample = "5000" < 4000
# print(sample)

sample = "5000" < "4000"
print(sample)

sample = "5000" > "4000"
print(sample)

sample = "삼성"
check = "삼성"
result = sample == check
print(result)



sample1 = "삼성"
sample2 = "LG"
sample3 = "LG"
result = sample1 == sample2 and sample2 == sample3
print(result)

result = sample1 == sample2 or sample2 == sample3
print(result)

sample1 = 5000
sample2 = 3000
sample3 = 2000
sample4 = 1000
sample5 = 500
price = 3500
result = (price > sample1 or price > sample2) \
and price > sample3
print(result)

result = (price == sample1 or price > sample2) \
and price > sample3 \
and (price < sample4 or price > sample5)
print("결과 %s" % result)


result = 5000 > 3000
if result:
    print("통과")

result = 5000 < 3000
if result:
    print("통과2")    
print("그냥넘김")


if 5000 > 3000:
    print("통과3")

if 5000 > 3000 \
    and 5000 == 3000:
    print("통과4")

elif 3000 == 2000:
    print("통과5")

else:
    print("통과6")
    
    
# 삼성전자, 등락율
# LG전자, 등락율
# 기타... 자기가 원하는 종목 3개와 등락율
# 위에 것들을 딕셔너리로 구성!
# if문을 활용해서~
# 등락율이 3% 이상인 것만 출력해라


# 삼성전자의 등락율이 1% 이상이라면 
# LG전자는 1% 이상인지 확인하고
# LG전자가 1% 이상이면 카카오의 등락율을 확인, 
# 이하이면 네이버의 등락율을 확인
# 구성 자체가 중요~


    

