import random
import string
import xlsxwriter
from io import StringIO, BytesIO
from django.utils import timezone


def get_short_url_hash():
    """Generate token for short url from upper case and lower case letters and digits
    
    Return: short url token
    """
    random_hash = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
    return random_hash

def get_ip_address(request):
    """Get user IP address from HTTP request
    
    Keyword arguments:
    request -- HTTP request object HttpRequest
    Return: ip address
    """
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def write_excel_file(data, request):
    """Write data to excel file
    
    Keyword arguments:
    data -- data to write to excel file
    Return: return_description
    """
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)

    server_uri = request.build_absolute_uri('/')
            
    # create working sheet
    worksheet_s = workbook.add_worksheet("Статистика посещений")
    # create header
    header = workbook.add_format({
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
    })
    worksheet_s.write(0, 0, "Ссылка", header)
    worksheet_s.write(0, 1, "Короткая cсылка", header)
    worksheet_s.write(0, 2, "# посещений", header)
    for idx, data_row in enumerate(data):
        row = 2 + idx
        worksheet_s.write_string(row, 0, data_row.full_url)
        short_url = f'{server_uri}{data_row.slug}'
        worksheet_s.write_string(row, 1, short_url)
        worksheet_s.write_number(row, 2, data_row.statistics.total_visits)
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data

    