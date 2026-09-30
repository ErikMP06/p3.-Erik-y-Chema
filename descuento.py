"""Práctica D3: Cálculo de descuentos en compras.

Este programa calcula el precio final de una compra aplicando un descuento
progresivo según el importe total introducido por el usuario.

Cumple con las directrices de estilo PEP 8.
"""

# ==============================================================================
# BLOQUE 1: DECLARACIÓN DE CONSTANTES
# ==============================================================================
DESCUENTO_TRAMO_1 = 0.10  # 10% a partir de 100 €
DESCUENTO_TRAMO_2 = 0.15  # 15% a partir de 300 €

UMBRAL_TRAMO_1 = 100.00
UMBRAL_TRAMO_2 = 300.00


# ==============================================================================
# BLOQUE 2: DECLARACIÓN DE FUNCIONES
# ==============================================================================
def calcular_descuento(importe: float) -> tuple[float, float, float]:
    """Calcula el Porcentaje, Monto de descuento y el Importe final a pagar.

    Args:
        importe (float): Monto total de la compra antes de descuento.

    Returns:
        tuple[float, float, float]: Porcentaje de descuento,
        monto del descuento e importe final.
    """
    if importe >= UMBRAL_TRAMO_2:
        porcentaje = DESCUENTO_TRAMO_2
    elif importe >= UMBRAL_TRAMO_1:
        porcentaje = DESCUENTO_TRAMO_1
    else:
        porcentaje = 0.0

    monto_descuento = importe * porcentaje
    precio_final = importe - monto_descuento

    return porcentaje, monto_descuento, precio_final


# ==============================================================================
# BLOQUE 3: PROGRAMA PRINCIPAL / ENTRADA, CONTROL Y SALIDA
# ==============================================================================
def main() -> None:
    """Función principal para la interacción con el usuario."""
    print("========================================")
    print("    SISTEMA DE CÁLCULO DE DESCUENTOS    ")
    print("========================================\n")

    try:
        # Entrada de datos
        mensaje_input = "Introduce el importe de la compra (€): "
        importe_compra = float(input(mensaje_input))

        # Validación de restricciones
        if importe_compra < 0:
            print("\nError: El importe de la compra no puede ser negativo.")
            return

        # Procesamiento
        porcentaje, descuento, total = calcular_descuento(importe_compra)

        # Salida de datos
        print("\n---------------- RESUMEN ----------------")
        print(f"Importe original : {importe_compra:8.2f} €")
        print(f"Descuento ({porcentaje * 100:2.0f} %) : {descuento:8.2f} €")
        print(f"Total a pagar    : {total:8.2f} €")
        print("-----------------------------------------")

    except ValueError:
        print("\nError: Debe ingresar un valor numérico válido.")


if __name__ == "__main__":
    main()
