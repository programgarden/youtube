# while True:
    # print("while 무한 루프")
    
    # continue
    # print("continue 이후")    
# print("while을 빠져나옴")

# earning_rate = 20.2
# while earning_rate < 30.5:
    # print("계속주시")
    # earning_rate += 1
# print("수익률이 30.5 이상이여서 매도함")

# stock_dict = {}
# tick_cnt = 0
# while True:
    # if tick_cnt > 5:
        # print("이 종목을 주시할거다")
        # stock_dict["삼성"] = True
    
    # if "삼성" in stock_dict.keys():
        # print("매수? 매도?")
        # break
        
    # tick_cnt += 1
    
# print("%s" % stock_dict)
        
        
stock_list = ["삼성", "LG", "카카오", "네이버", "대우"]
stock_dict = {"삼성":{"매수여부":False, "매매제한":3, "매수횟수":0, "매도횟수":0},
                "LG":{"매수여부":False, "매매제한":2, "매수횟수":0, "매도횟수":0},
                "카카오":{"매수여부":False, "매매제한":5, "매수횟수":0, "매도횟수":0},
                "네이버":{"매수여부":False, "매매제한":0, "매수횟수":0, "매도횟수":0},
                "대우":{"매수여부":False, "매매제한":1, "매수횟수":0, "매도횟수":0}}
                
while True:
    for stock_name in stock_list:
        unit_dict = stock_dict[stock_name]
        
        if unit_dict["매수여부"] is False:
            if unit_dict["매매제한"] > unit_dict["매수횟수"]:
                unit_dict["매수횟수"] = unit_dict["매수횟수"]+1
                
                if stock_name in stock_list:
                    print("%s 매수 %s" % (stock_name, unit_dict["매수횟수"]), flush=True)
                    unit_dict["매수여부"] = True
                    
        elif unit_dict["매수여부"] is True:
            if unit_dict["매매제한"] > unit_dict["매도횟수"]:
                unit_dict["매도횟수"] = unit_dict["매도횟수"]+1
                
                if stock_name in stock_list:
                    print("%s 매도 %s" % (stock_name, unit_dict["매도횟수"]), flush=True)
                    unit_dict["매수여부"] = False
                    

stock_name = "삼성"
price = 10000
mesu_price = 0
kospi_unit = 50

while True:
    if mesu_price == 0:
        mesu_price = price
    else:
        price = price + kospi_unit
        drate = (price - mesu_price) / mesu_price * 100
        if drate >= 30.0:
            print("%s의 30%s부근의 가격은 %s이다. %s" % (stock_name, "%", price, drate), flush=True)
            break

        









       
               
                    
            
            
            





