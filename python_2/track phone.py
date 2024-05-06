import phonenumbers
from phonenumbers  import geocoder
phone_number1 = phonenumbers.parse("+233244177624")
phone_number2 = phonenumbers.parse("+233244887345")
phone_number3 = phonenumbers.parse("+233507232421")
phone_number4 = phonenumbers.parse("+233550293987")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
print(geocoder.description_for_number(phone_number3,"en"))
print(geocoder.description_for_number(phone_number4,"en"))