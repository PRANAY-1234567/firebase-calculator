import firebase_admin
from firebase_admin import credentials ,db
cred=credentials.Certificate("C:/Users/ASUS/Desktop/python basic/new-python-36518-firebase-adminsdk-fbsvc-fa7a5c5d87.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred,{"databaseURL":"https://new-python-36518-default-rtdb.firebaseio.com/"})







a=float(input("Enter the first number"))
b=input("Enter the Operator")
c=float(input("Enter the second number"))
d=0
if b=="+":
    d=a+c
elif b=="*":
    d=a*c
elif b=="/":
    if c!=0:
        d=a/c
    else:
        print("cannot divide by zero")
elif b=="-":
    d=a-c
else:
    print("Fail")




ref=db.reference('Calsi')
ref.push({"calculate the number":d})
print("data sent ")