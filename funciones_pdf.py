from fpdf import FPDF

EFECTIVO = "Efectivo"
TRANSFERENCIA = "Transferencia"

productos = ["Alfajor", "Gaseosa", "Chicle", "Agua"]
precios = [1500, 2800, 500, 1800]

def buscar_posicion(lista, nombre):
    for i in range(len(lista)):
        if lista[i] == nombre:
            return i
    return -1

def aplicar_descuento(monto, forma_pago):
    if forma_pago == EFECTIVO:
        return round(monto - monto * 10 / 100, 2)
    return monto

def calcular_iva(monto):
    """Calcula el 21% de IVA"""
    return round(monto * 21 / 100, 2)

def renglon(pdf, texto, valor):
    pdf.cell(120, 9, texto)
    pdf.cell(0, 9, valor, align="R", new_x="LMARGIN", new_y="NEXT")

def armar_pdf(numero, fecha, cliente, producto, cantidad, precio, subtotal, descuento, iva, total):
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, "Kiosco Carlos Paz", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 11)
    pdf.cell(0, 7, f"Presupuesto Nro: {numero}", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 7, f"Fecha: {fecha}", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(15)
    
    pdf.set_font("Helvetica", "", 12)
    renglon(pdf, "Cliente", cliente)
    renglon(pdf, f"{cantidad} x {producto}", f"${precio:.2f} c/u")
    pdf.ln(4)
    
    renglon(pdf, "Subtotal", f"${subtotal:.2f}")
    renglon(pdf, "Descuento", f"-${descuento:.2f}")
    renglon(pdf, "IVA 21%", f"${iva:.2f}")
    pdf.set_font("Helvetica", "B", 14)
    renglon(pdf, "TOTAL", f"${total:.2f}")
    
    pdf.ln(10)
    pdf.set_font("Helvetica", "I", 9)
    pdf.cell(0, 6, "Presupuesto válido por 7 días.", new_x="LMARGIN", new_y="NEXT")
    
    return bytes(pdf.output())
