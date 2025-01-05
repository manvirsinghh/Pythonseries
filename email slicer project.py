#email slicer project .In this project we have to slice the name and domain from email 
print("EMAIL SLICER PROJECT")
email=input("enter any email here:")
username=""
domainname=""
found_at=False
for i in email:
    if i=='@':
        found_at=True
    elif not found_at:
        username+=i
    else:
        domainname+=i
print(f"username:{username}")
print(f"domainname:{domainname}")



 
