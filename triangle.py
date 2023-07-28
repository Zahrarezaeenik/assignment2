adad_1=int(input("adad aval ra vared konid: "))
adad_2=int(input("adad dovom ra vared konid: "))
adad_3=int(input("adad sevom ra vared konid: "))
if adad_1+adad_3>adad_2:
    print("mosalas")
elif adad_1+adad_2>adad_3:
    print("mosalas")
elif adad_2+adad_3>adad_1:
    print("mosalas")
else:
    print("moasalas nist")