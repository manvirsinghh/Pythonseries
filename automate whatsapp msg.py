#Automate whatsapp messages
import pywhatkit as kit
phone_number="+919915803830"
message="Hi,Manvir ,How are you?"
time_hour=1
time_minute = 5
kit.sendwhatmsg(phone_number,message,time_hour,time_minute)