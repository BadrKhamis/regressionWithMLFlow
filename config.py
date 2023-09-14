from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
blueFont = ParagraphStyle(
    name='TimesNewRoman',
    fontName='Times-Roman',
    fontSize=12,
    leading=14,
    textColor=colors.blue,  # Set your desired color here
    alignment=1,  # 0: left, 1: center, 2: right
)

contentText = ParagraphStyle(
    name='TimesNewRoman',
    fontName='Times-Roman',
    fontSize=12,
    leading=14,
    textColor=colors.black,  # Set your desired color here
    alignment=4,  # 0: left, 1: center, 2: right
)

headerTitle = ParagraphStyle(
    name='TimesNewRoman',
    fontName='Times-Roman',
    fontSize=16,
    leading=14,
    textColor=colors.blue,  # Set your desired color here
    alignment=1,  # 0: left, 1: center, 2: right
)

redFont = ParagraphStyle(
    name='TimesNewRoman',
    fontName='Times-Roman',
    fontSize=12,
    leading=14,
    textColor=colors.red,  # Set your desired color here
    alignment=1,  # 0: left, 1: center, 2: right
)

tableStyle = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
])

# Create a PDF document


# Define styles
styles = getSampleStyleSheet()
title_style = styles['Heading1']
normal_style = styles['Normal']

# Define a custom bold style
bold_style = ParagraphStyle(
    'BoldStyle',
    parent=normal_style,
    fontName='Helvetica-Bold',
    leading=14,
)

# Data for the objectives
