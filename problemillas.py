import streamlit as st
import funciones_pdf  
st.title("kiosquitotito")

cliente_nombre = st.text_input("Nombre del Cliente:", value="Juli")
producto_elegido = st.selectbox("Seleccioná el producto:", funciones_pdf.productos)
cantidad = st.number_input("Cantidad de unidades:", min_value=1, step=1, value=3)
forma_pago = st.radio("Forma de pago:", [funciones_pdf.EFECTIVO, funciones_pdf.TRANSFERENCIA])

col1, col2 = st.columns(2)
with col1:
    nro_factura = st.number_input("N° de Comprobante:", min_value=1, value=1001, step=1)
with col2:
    fecha_actual = st.text_input("Fecha:", value="05/11/2026")

pos = funciones_pdf.buscar_posicion(funciones_pdf.productos, producto_elegido)
precio_unitario = funciones_pdf.precios[pos]

subtotal = cantidad * precio_unitario
monto_con_descuento = funciones_pdf.aplicar_descuento(subtotal, forma_pago)
descuento_aplicado = round(subtotal - monto_con_descuento, 2)
iva_calculado = funciones_pdf.calcular_iva(monto_con_descuento)
total_neto = round(monto_con_descuento + iva_calculado, 2)

st.write("---")
st.subheader("Resumen de la compra")
st.write(f"Subtotal Bruto: `${subtotal:,.2f}`")
st.write(f"Descuento Otorgado: `-${descuento_aplicado:,.2f}`")
st.write(f"IVA Liquidado: `${iva_calculado:,.2f}`")
st.markdown(f"### **Total Facturado: ${total_neto:,.2f}**")

archivo_pdf = funciones_pdf.armar_pdf(
    numero=nro_factura,
    fecha=fecha_actual,
    cliente=cliente_nombre,
    producto=producto_elegido,
    cantidad=cantidad,
    precio=precio_unitario,
    subtotal=subtotal,
    descuento=descuento_aplicado,
    iva=iva_calculado,
    total=total_neto
)

st.write("")
st.download_button(
    label="Descargar presupuesto (PDF)",
    data=archivo_pdf,
    file_name=f"presupuesto_{nro_factura}.pdf",
    mime="application/pdf"
)
