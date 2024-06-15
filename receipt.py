from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas

def generate_receipt(filaname,info):

    a = Canvas(filaname,pagesize=letter)
    width, height = letter
    print(width,height,letter)

    a.setFont('Helvetica-Bold', 24)
    a.drawString(250, height-100,'Transaction')

    a.setFont('Helvetica', 12)
    y_position = height - 150

    for x, y in info.items():
        a.drawString(100,y_position,f"{x}:{y}")
        y_position -= 20

    a.save()

info = {
    'Number':'101',
    'Date':'2024-06-10',
    'Customer Name':'David',
    'Amount':'Rs.15000',
    'Payment Method':'Credit Card',
    'Item':'items'
}

generate_receipt('receiptt.pdf',info)