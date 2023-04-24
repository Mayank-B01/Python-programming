#asking user to input marked price
m_price=float(input("Enter the marked price "))

#checking the price to apply discount
if m_price>=10000:
    discount=m_price*(20/100)
elif m_price>=5000 and m_price<10000:
    discount=m_price*(10/100)
else:
    discount=m_price*(5/100)

#calculating net amount
net_amount=m_price-discount

#displaying the amount to pay
print("The net amount to pay is",net_amount)