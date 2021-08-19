
""" Tasks are as following: 
    read texts files
    extract emails
    extract phones
"""
import re

file_path = "assets/potential-contacts.txt"
with open( file_path, 'r') as file:
    content = file.read()

# print(content)

def extract_emails(content): 
    pass
def extract_phones(content): 
    pass


if __name__ == "__main__":
    emails = extract_emails(content)
    phone_numbers = extract_phones(content)
    
