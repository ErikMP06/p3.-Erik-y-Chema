# Práctica D3 — Del enunciado al programa

**Módulo / Asignatura:** Programación / Desarrollo de Software  
**Integrantes del grupo:** Erik y Jose María  
**Fecha:** 29 de septiembre de 2026  

---

##  Enunciado del problema
Una tienda aplica un descuento del 10 % a partir de 100 € de compra y del 15 % a partir de 300 €.  
El objetivo es desarrollar un programa interactivo en Python que reciba el importe total de la compra, aplique las reglas de descuento correspondientes y muestre el importe final a pagar junto con el descuento aplicado.

---

## 1. Análisis

En esta fase se identifican y estructuran los requisitos del sistema:

* **Entradas:**
  * `importe_compra` (*Float*): Importe total bruto de la compra en euros (€).

* **Salidas:**
  * `porcentaje_descuento` (*Float*): Porcentaje del descuento aplicado (0 %, 10 % o 15 %).
  * `monto_descuento` (*Float*): Cantidad ahorrada en euros (€).
  * `precio_final` (*Float*): Importe definitivo a pagar tras aplicar el descuento (€).

* **Restricciones y Reglas de Negocio:**
  1. El importe de la compra debe ser un valor numérico mayor o igual a cero (`importe_compra >= 0`). No se permiten importes negativos.
  2. **Tramos de descuento:**
     * Si `importe_compra < 100.00 €` $\rightarrow$ Descuento del **0 %**.
     * Si `100.00 € <= importe_compra < 300.00 €` $\rightarrow$ Descuento del **10 %**.
     * Si `importe_compra >= 300.00 €` $\rightarrow$ Descuento del **15 %**.
  3. Todos los importes monetarios mostrados deben formatearse con dos decimales.

---

## 2. Diseño

### A) Pseudocódigo (PSeInt / Estándar)

```text
Algoritmo CalculoDescuentoTienda
    // Declaración de constantes
    PORCENTAJE_TRAMO1 <- 0.10
    PORCENTAJE_TRAMO2 <- 0.15
    UMBRAL_TRAMO1 <- 100.0
    UMBRAL_TRAMO2 <- 300.0

    // Entrada de datos
    Escribir "Ingrese el importe de la compra (€): "
    Leer importe_compra

    // Control de restricciones
    Si importe_compra < 0 Entonces
        Escribir "Error: El importe no puede ser negativo."
    Sino
        // Evaluación de tramos de descuento
        Si importe_compra >= UMBRAL_TRAMO2 Entonces
            porcentaje_descuento <- PORCENTAJE_TRAMO2
        Sino Si importe_compra >= UMBRAL_TRAMO1 Entonces
            porcentaje_descuento <- PORCENTAJE_TRAMO1
        Sino
            porcentaje_descuento <- 0.0
        FinSi

        // Procesamiento / Cálculos
        monto_descuento <- importe_compra * porcentaje_descuento
        precio_final <- importe_compra - monto_descuento

        // Salida de datos
        Escribir "Porcentaje de descuento aplicado: ", porcentaje_descuento * 100, "%"
        Escribir "Monto de descuento: ", monto_descuento, " €"
        Escribir "Importe final a pagar: ", precio_final, " €"
    FinSi
FinAlgoritmo