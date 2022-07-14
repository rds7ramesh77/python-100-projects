#Python Program for Email Slice


""" An Email slicer is a very useful program for separating the username and domain name of email address"""


""" To create an email slicer with Python... """

email=input("Enter Your email::").strip()

username=email[:email.index("@")]
domain_name=email[email.index("@")+1:]

Eformat=(f"Your username is '{username}' and your domain is '{domain_name}'")

print(Eformat)