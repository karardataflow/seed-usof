import pdfkit

# Set the path to wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf=r'C:\Users\rf\Desktop\wkhtmltopdf\bin\wkhtmltopdf.exe')

# Reviewer data
reviewer_name = 'أحمد علي'
profession = 'مراجع مالي'
id_number = '123456'
issue_date = '2024-11-01'
issue_place = 'بغداد'
review_status = 'مكتملة'
reviewing_entity = 'وزارة المالية'
birth_date = '1990-05-15'  # تاريخ الميلاد
address = 'شارع 123، بغداد'  # العنوان
phone_number = '07123456789'  # رقم الهاتف
email = 'ahmed.ali@example.com'  # البريد الإلكتروني

# Set up HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>بيانات المراجع</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            direction: rtl;
        }}
    </style>
</head>
<body>
    <h1>معلومات المراجع</h1>
    <p>اسم المراجع: {reviewer_name}</p>
    <p>المهنة: {profession}</p>
    <p>رقم الهوية: {id_number}</p>
    <p>تاريخ الإصدار: {issue_date}</p>
    <p>مكان الإصدار: {issue_place}</p>
    <p>حالة المراجعة: {review_status}</p>
    <p>الجهة المراجعة: {reviewing_entity}</p>
    <p>تاريخ الميلاد: {birth_date}</p>
    <p>العنوان: {address}</p>
    <p>رقم الهاتف: {phone_number}</p>
    <p>البريد الإلكتروني: {email}</p>
</body>
</html>
"""

# PDF options
options = {
    'no-stop-slow-scripts': '',
    'debug-javascript': '',
    'disable-smart-shrinking': '',
    'enable-local-file-access': '',
    'zoom': '1.3',
    'disable-javascript': '',
}

# Generate PDF from HTML content
try:
    pdfkit.from_string(html_content, 'reviewer_data.pdf', configuration=config, options=options)
    print("PDF created successfully.")
except Exception as e:
    print("An error occurred while creating the PDF:", e)
