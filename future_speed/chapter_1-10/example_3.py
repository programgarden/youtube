#################
##### 리스트
################

#################
##### 튜플
#################
a_tuple = ("크루드오일", "항생", "유료FX")
a_val = a_tuple[2]
print(a_val)
for i in a_tuple:
    print(i)

################
##### 리스트
################
a_list = ["크루드오일", "항생", "유료FX"]
for val in a_list:
    print(val)

a_list = ["크루드오일", "항생", "유료FX"]
a_list.append("금")
print(a_list)
for val in a_list:
    print(val)

a_list = ["크루드오일", "항생", "유료FX"]
a_list[2] = "호주달러"
print(a_list)

a_list = ["크루드오일", "항생", "유료FX"]
del a_list[1]
print(a_list)

################################
##### 딕셔너리
###############################

a_dict = {"크루드오일":1.000, "항생":23158, "유료FX":1.1504}
print(a_dict.get("크루드오일"))
print(a_dict["크루드오일"])

a_dict = {"크루드오일":1.000, "항생":23158, "유료FX":1.1504}
print(a_dict.keys())
for key in a_dict.keys():
    print(a_dict.get(key))

for key, value in a_dict.items():
    print("키 값: %s, value값 : %s" % (key, value))

a_dict = {"크루드오일":1.000, "항생":23158, "유료FX":1.1504}
a_dict["크루드오일"] = 5.200
print(a_dict)

a_dict = {"크루드오일":1.000, "항생":23158, "유료FX":1.1504}
a_dict.update({"아무거나":2500})
print(a_dict)

a_dict = {"크루드오일":1.000, "항생":23158, "유료FX":1.1504}
a_dict["크루드오일"] = 3.420
a_dict["항생"] = 30020
a_dict['유료FX'] = 2.0000
a_dict['천연가스'] = 1.6082
print(a_dict)

a_dict = {"크루드오일":1.000, "항생":23158, "유료FX":1.1504}
a_dict.update({"크루드오일":3.420, "항생":30020, "유료FX":2.0000, "천연가스":1.6082})
print(a_dict)

a_dict = {"크루드오일":{"현재가":2.000}, "항생":23158, "유료FX":1.1504}
print(a_dict["크루드오일"]["현재가"])

