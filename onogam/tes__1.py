
import win32com.client
import os
import sys



outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

accounts = outlook.Folders
for account in accounts:
    print(account)
    
