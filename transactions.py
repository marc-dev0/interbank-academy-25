#!/usr/bin/env python3

import csv
import sys
from decimal import Decimal


def procesar_transacciones(archivo='data.csv'):
    transacciones = []

    # Lectura del archivo CSV
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                transacciones.append({
                    'id': int(row['id']),
                    'tipo': row['tipo'],
                    'monto': Decimal(row['monto'])
                })
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}")
        sys.exit(1)

    # Cálculo del balance: suma de créditos menos suma de débitos
    creditos = sum(t['monto'] for t in transacciones if t['tipo'] == 'Crédito')
    debitos = sum(t['monto'] for t in transacciones if t['tipo'] == 'Débito')
    balance = creditos - debitos

    # Búsqueda de la transacción con mayor monto
    max_transaccion = max(transacciones, key=lambda t: t['monto'])

    # Conteo de transacciones por tipo
    conteo = {'Crédito': 0, 'Débito': 0}
    for t in transacciones:
        conteo[t['tipo']] += 1

    # Reporte
    print("Reporte de Transacciones")
    print("-" * 45)
    print(f"Balance Final: {balance:.2f}")
    print(f"Transacción de Mayor Monto: ID {max_transaccion['id']} - {max_transaccion['monto']:.2f}")
    print(f"Conteo de Transacciones: Crédito: {conteo['Crédito']} Débito: {conteo['Débito']}")


if __name__ == "__main__":
    # Permite especificar un archivo como argumento o usa 'data.csv' por defecto
    if len(sys.argv) > 1:
        procesar_transacciones(sys.argv[1])
    else:
        procesar_transacciones()