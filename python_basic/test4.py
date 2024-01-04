# dictionary 
var = {"key":"data"}
print(var)
print(type(var))

print(var["key"])

var = {"삼성":62000, "LG":73600}
print(var["LG"])
del var["삼성"]
print(var)


var2 = var.keys()
print(var2)


var = {"삼성":62000, "LG":73600, 
        "카카오":357500}
var2 = var.keys()
print(var2)
var3 = list(var)
print(var3)


var1 = {"삼성":62000, "LG":73600, 
        "카카오":357500}
var2 = var1.keys()
print(var2)
var1["아남전자"] = 2325
print(var1)
print(var2)

var3 = list(var1)
print(var3)

var3 = list(var1)
var1["셀리버리"] = 208500
print(var3)




var1 = {"삼성":62000, "LG":73600, 
        "카카오":357500}

var2 = var1.keys()
var1["아남전자"] = 2325
print(var2)


var1 = {"삼성":62000, "LG":73600, 
        "카카오":357500}
var2 = list(var1)
var1["아남전자"] = 2325
print(var2)

        
var1 = {"삼성":62000, "LG":73600, 
        "카카오":357500}

var1 = {"현재가": 62000, "등락율": 20.0}
var2 = {"삼성": var1}
# {"삼성": {"현재가": 62000, "등락율": 20.0}}
print(var2["삼성"]["현재가"])

var3:dict = var2["삼성"]
var3.keys()


price:int = var2["삼성"]["현재가"]
print(type(price))


print(var2)

# var2["네이버"]["전일대비"] = 3000
# print(var2)


 
var1 = {"현재가":62000, "거래량":300000}
var2 = {"삼성전자":var1}

price = var2["삼성전자"]["현재가"]
# price_error = var2["네이버"]["현재가"]
# var2["네이버"]["현재가"] = 200000

sample:dict = {"네이버":{"현재가":200000}}
var2.update(sample)
print(var2)

계좌 = {"A계좌":
        {"메소드1":
            {"종목1":
                {"현재가":23523}
            }
        },
      "B계좌":
        {"메소드1":
            {"종목1":
                {"현재가":1209}
            }
        }
     }

