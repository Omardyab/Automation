""" Tasks are as following: 
    read texts files
    extract emails
    extract phones
    creat new files for both
"""
from os import WIFSTOPPED
import re

file_path = "assets/potential-contacts.txt"
with open( file_path, 'r') as file:
    content = file.read()
    # print(content)

def extract_emails(content): 
    email_extraction=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    email_content=re.findall(email_extraction,content)
    # removing duplicated using set
    email_content=list(set(email_content))
    email_content.sort()
    return(email_content)

def extract_phones(content): 
    phone_contacts=[]
    # phone_extraction=(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', content)
    phone_extraction=r"[0-9-+x.()]{7,}"
    phone_numbers = re.findall(phone_extraction, content)
    # print(phone_numbers)
    # print("newform is as following")
    for phone_number in phone_numbers:
        phone_number = phone_number.replace(".", "").replace("(", "").replace(")", "")
        # reshaping phone numbers
        if len(phone_number) == 10:
            phone_number = phone_number[:3]+"-"+phone_number[3:6]+"-"+phone_number[6:]
        phone_contacts.append(phone_number)
    phone_contacts = list(set(phone_contacts))
    # print(phone_contacts)
    return phone_contacts

def writing_new_file(path,fun): 
    with open(path,"w") as f:
        text=""
        for x in fun(content):
            text+=x+"\n"
        f.write(text)


if __name__ == "__main__":
    # emails = extract_emails(content)
    # print(emails)
    writing_new_file("assets/email_contacts.txt",extract_emails)
    # phone_numbers = extract_phones(content)
    # print(phone_numbers)
    writing_new_file("assets/phone_contacts.txt",extract_phones)
