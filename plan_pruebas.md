# 🧪 Plan de Pruebas - ISBN Validator

## 1. Objetivo
Verificar que las funciones del proyecto `isbn-validator` validen correctamente los códigos ISBN-10 y ISBN-13.

## 2. Alcance
Las pruebas cubrirán:
- Función de validación de ISBN-10.
- Función de validación de ISBN-13.
- Casos válidos e inválidos.
- Manejo de errores (entradas vacías, caracteres no válidos, etc.).

## 3. Herramientas utilizadas
- Python 3.13
- pytest
- coverage

## 4. Estrategia de pruebas
Las pruebas se ejecutarán de forma automática con `pytest`, y se medirá la cobertura de código con `coverage`.

## 5. Casos de prueba

| ID | Descripción | Entrada | Resultado Esperado |
|----|--------------|---------|--------------------|
| TC01 | Validar ISBN-10 correcto | `0-306-40615-2` | Válido |
| TC02 | Validar ISBN-10 incorrecto | `0-306-40615-9` | Inválido |
| TC03 | Validar ISBN-13 correcto | `978-3-16-148410-0` | Válido |
| TC04 | Validar ISBN-13 incorrecto | `978-3-16-148410-9` | Inválido |
| TC05 | Entrada vacía | `""` | Error o mensaje de entrada inválida |

## 6. Resultados esperados
Todas las pruebas deben pasar (✔️) y la cobertura de código debe ser mayor al 90%.

## 7. Evidencias
- Archivo `.coverage`
- Reporte generado con `coverage report -m`
- Reporte HTML generado con `coverage html` (carpeta `htmlcov`)
