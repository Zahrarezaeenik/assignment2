name=input("name khod ra vared konid: ")
nomre_1=float(input("nomre aval khod ra vared konid: "))
nomre_2=float(input("nomre dovom khod ra vared konid: "))
nomre_3=float(input("nomre sevom khod ra vared konid: "))
moadel=(nomre_1+nomre_2+nomre_3)/3
if moadel>=17:
    print("Greate")
elif moadel>=12 and moadel<17:
    print("Normal")
elif moadel<12:
    print("Fail")