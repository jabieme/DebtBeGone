from fastmcp import FastMCP
import csv
from pypdf import PdfReader

server: FastMCP = FastMCP(name="Debt")

# Data Ingesting Tools
# Input: Credit Card Statement, Mortage Loan, Auto Loan
# Process:
# Scans files into a data structure
# transformers file data 
# returns file data

def csv_parse(file_id: str, delimiter: str = ',') -> list:
    """
    TOOL: csv.parse
    Input JSON:
      { "file_id": "<upload-handle>", "delimiter": "," }
    Output JSON:
      { "rows": [ [ "name","balance","apr", ... ], ... ],
        "detected_headers": ["name","balance","apr", ...] }
    """
    reader = PdfReader(file_id)

    
    print(len(reader.pages))
    # transactions = []
    page1 = reader.pages[0]
    page3 = reader.pages[2]
    
    print(page1)

    # with open(file_id, 'r', newline='') as csvfile:
    #     reader = csv.DictReader(csvfile, delimiter=delimiter)
    #     for row in reader:
    #         transactions.append(row)
    # return transactions

async def sheets_read_range(sheet_id: str, cell_range: str) -> dict:
    """
    TOOL: sheets.read_range
    Input:
      { "sheet_id": "abc123", "range": "Debts!A1:H1000" }
    Output:
      { "headers": ["name","type","balance","apr","min_payment","due_day","credit_limit","promo"],
        "rows": [ {"name":"Amex","balance":"5200", ...}, ... ] }
    """ 

if __name__ == '__main__':
    filePath = './test/data/statement.pdf'
    print(csv_parse(filePath))
