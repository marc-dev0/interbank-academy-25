# Procesador de Transacciones Bancarias

## Introducción

Aplicación CLI que procesa transacciones bancarias desde un archivo CSV y genera un reporte con balance final, transacción de mayor monto y conteo de transacciones por tipo.

## Instrucciones de Ejecución

### Requisitos
- Python 3.7 o superior

### Ejecución
```bash
# Con archivo por defecto (data.csv)
python transactions.py

# Con archivo específico
python transactions.py mi_archivo.csv
```

No requiere instalación de dependencias externas.

## Enfoque y Solución

La aplicación lee un archivo CSV con transacciones bancarias y calcula:
- Balance total (créditos - débitos)
- Transacción con mayor monto
- Cantidad de transacciones por tipo

Se utiliza la librería `csv` para procesar el archivo y `Decimal` para manejar valores monetarios con precisión.

## Estructura del Proyecto

```
interbank-academy-25/
├── data.csv          # Archivo de datos
├── README.md         # Este archivo
└── transactions.py   # Programa principal
```