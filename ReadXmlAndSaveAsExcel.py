#Read the XML file and get one attribute and save in excel file

import xml.etree.ElementTree as ET
import openpyxl

# Specify the path to your XML file
xml_file_path = 'sitemap.xml'

# Parse the XML file
tree = ET.parse(xml_file_path)
root = tree.getroot()
print(root)
# Create an Excel workbook
workbook = openpyxl.Workbook()
sheet = workbook.active

# Add a header to the Excel sheet
sheet['A1'] = 'loc'

# Iterate through the XML data and add <loc> values to the Excel sheet
row = 2
for url in root.findall('.//url'):
    print(url)
    loc = url.find('loc').text
    sheet.cell(row=row, column=1, value=loc)
    row += 1

# Specify the Excel file path where you want to save the data
excel_file_path = 'output.xlsx'

# Save the Excel workbook
workbook.save(excel_file_path)

# Close the workbook
workbook.close()

print(f'Data saved to {excel_file_path}')
