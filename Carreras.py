import pdfplumber
import csv

def extract_unique_careers(pdf_path, output_csv):
    unique_careers = set()  # Usar un conjunto para almacenar carreras únicas
    
    # Abrir el PDF y extraer las tablas
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages):
            print(f"\n=== Tablas en la página {page_number + 1} ===")
            tables = page.extract_tables()  # Extraer tablas de la página
            for table_number, table in enumerate(tables):
                print(f"\nTabla {table_number + 1}:")
                for row in table:
                    # Obtener carrera (tercera columna)
                    career = row[2] if row[2] else None
                    if career:  # Si hay carrera, agregarla al conjunto
                        unique_careers.add(career)
    
    # Guardar las carreras únicas en un archivo CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Universidad', 'Carrera'])  # Escribir el encabezado
        for career in unique_careers:
            writer.writerow(['General', career])  # Escribir "General" en la columna de universidad
    
    print(f"\nLas carreras únicas se han guardado en: {output_csv}")

# Ejemplo de uso
pdf_path = r"C:\workspace\webScraping\Oferta-Academica.pdf"  # Reemplaza con la ruta de tu archivo PDF
output_csv = r"C:\workspace\webScraping\Carreras_Unicas.csv"  # Ruta para guardar el archivo CSV
extract_unique_careers(pdf_path, output_csv)
