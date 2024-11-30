from cvss import CVSS3

# Cadena CVSS obtenida de un reporte (ejemplo)
cvss_vector = "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"

# Analiza la cadena CVSS
cvss = CVSS3(cvss_vector)

# Imprime detalles
print(f"Puntuación Base: {cvss.base_score}")
print(f"Vector: {cvss.vector}")
print(f"Impacto: {cvss.impact_subscore}")
print(f"Explotabilidad: {cvss.exploitability_subscore}")
