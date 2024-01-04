print("Hello world")
print("Hello world" + " Thank you")
print(900629)
print("%s 입니다." % "크루드오일")
print("%s원 입니다." % 30400.30)
print("거래소는 %s 상품은 %s입니다." % ("CME", "corn"))

print("%s %s %s" % (1, 2, 3))


###################
##### 변수 만들기
###################

stock_price = 3900
print(stock_price)
stock_price_type = type(stock_price)
print(stock_price_type)

stock_percent = 3.8
print(stock_percent)
stock_percent_type = type(stock_percent)
print(stock_percent_type)

stock_name = "항생"
print(stock_name)
stock_name_type = type(stock_name)
print(stock_name_type)

stock_name = "5030"
print(stock_name)
stock_name_type = type(stock_name)
print(stock_name_type)

stock_buy = False
print(stock_buy)
stock_buy_type = type(stock_buy)
print(stock_buy_type)

###################
##### 산수
###################

stock_price = 2000
stock_price2 = 5000
stock_result = stock_price + stock_price2
print(stock_result)

stock_price = 2000
stock_price2 = 1500
stock_result = stock_price - stock_price2
print(stock_result)

stock_price = 1000
stock_quantity = 5
stock_result = stock_price * stock_quantity
print(stock_result)

stock_price = 2000
stock_price2 = 2200
stock_result = stock_price / stock_price2
print(stock_result)
stock_result = stock_price // stock_price2
print(stock_result)

stock_price = 20
stock_quantity = 9
stock_result = stock_price % stock_quantity
print(stock_result)