#Python Program to Create Invoice 

""" An invoice is a bill that serves as proof of a transaction between a buyer and a seller."""




""" To create an invoice with python we use basic python """




#Invoice for Apple Mobile shop


Mobile1,mobile1_Price="Iphone 11",899 #in USD
Mobile2,mobile2_Price="Iphone 13",1199
Mobile3,mobile3_Price="Iphone 6s",677
Mobile4,mobile4_Price="Iphone 5s",867
Mobile5,mobile5_Price="Iphone 4",456


company_name="Apple Inc"
company_Address="United State Of America"
company_city="Texas-68,street"

message='Thanks For Shoping with us !!! Have a Good Day😎'

#create a top border
print('='*50)

print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_Address.title()))
print('\t\t{}'.format(company_city.title()))


print('\tMobile Name\t Mobile Price')
print('\t{}\t\t${}'.format(Mobile1.title(),mobile1_Price))
print('\t{}\t\t${}'.format(Mobile2.title(),mobile2_Price))
print('\t{}\t\t${}'.format(Mobile3.title(),mobile3_Price))
print('\t{}\t\t${}'.format(Mobile4.title(),mobile4_Price))
print('\t{}\t\t${}'.format(Mobile5.title(),mobile5_Price))


print('='*50)
print('\t\t\tTotal')
total=mobile1_Price+mobile2_Price+mobile3_Price+mobile4_Price+mobile5_Price
print('\t\t\t${}'.format(total))
print('='*50)


print('\n{}\n'.format(message))