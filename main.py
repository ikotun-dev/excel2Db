import pandas as pd
import os
import openpyxl
from nse.settings import DATABASES  # Replace with your project's settings module

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nse.settings")
import django
django.setup()

from api.models import DemoEngineer

def excel_to_database(excel_file):
    wb = openpyxl.load_workbook(excel_file)
    sheet = wb.active  # Assume the active sheet is the one you're interested in
    try :
        for row in sheet.iter_rows(min_row=2, values_only=True):  # Assuming headers are in row 1
            name = row[1]  # Column B (NAMES)
            phone_number = row[2]  # Column C (PHONE-NUMBER)
            email_address = row[3]  # Column D (EMAIL-ADDRESS)
        
            DemoEngineer.objects.create(
            name=name,
            phone_number=phone_number,
            email_address=email_address
            )
    except Exception as e:
        print('error', str(e))

if __name__ == '__main__':
    excel_file_path = 'dues.xlsx'
    excel_to_database(excel_file_path)
