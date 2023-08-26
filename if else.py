money=int(input("total_money= "))
juice = 30
snacks =50
meals = 80
tea = 15
if money>=30 and money<=49:
  print("juice only")
elif money>=50 and money<=150:
  print("juice and snacks or meals or tea")
elif money>=150:
  print("juice,snacks,meals,tea")
else:
  print("nothing in that price range")
