#(1) RETURNS ALL CUSTOMERS FORM CUSTOMER TABLE
userinfo = userinfo.object.all()

#(2) RETURNS FIRST userinfo IN TABLE
firstuser = userinfo.object.first()
#but if u have a variable now
#print(firstuser.first())

#(3)Returns last userinfo in table 
lastuser = userinfo.objects.last()

#(4)Returns single customer by name
userbyname = userinfo.object.get(name="ivan")

#(5)Returns single customer by name
userbyid = userinfo.objects.get(id=4)

#(6) RETURNS ALL USERINFO RELATED TO CUSTOMER(FIRST USER)
userinfo = userinfo.object.all()

#(2) RETURNS FIRST userinfo IN TABLE
firstuser = userinfo.object.first()
#but if u have a variable now
#print(firstuser.first())

#(3)Returns last userinfo in table 
lastuser = userinfo.objects.last()

#(4)Returns single customer by name
userbyname = userinfo.object.get(name="ivan")

#(5)Returns single customer by name
userbyid = userinfo.objects.get(id=4)


