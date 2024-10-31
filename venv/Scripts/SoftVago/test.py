import requests

# URL del endpoint
url = "https://api-softvago.page.resigrass.com.co/GetUsers"
# Parámetros de la solicitud
token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiYXNlV2ViQXBpU3ViamVjdCIsImp0aSI6ImNiYTA5MmNmLTY2MjQtNDllNS1iY2Y3LTBkMGY0NWY4Nzc0MiIsImlhdCI6IjE3MzAzNDI1NjYiLCJVc2VybmFtZSI6WyJqb2hhbiIsImpvaGFuIl0sImV4cCI6MTczMDQyODk2NiwiaXNzIjoic29mdHZhZ28uY29tLmNvIiwiYXVkIjoiYXRvbXBvcGV6LmNvbS5jbyJ9.GM-Bk9c6X0jvoNeJn-IaRqToTF5lNFPhu4ksjzwDCbA"

headers = {
    "Authorization": f"Bearer {token}"
}
# Hacer la solicitud GET
response = requests.get(url, headers=headers)

# Verificar que la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Si la solicitud fue exitosa, imprimimos los datos en formato JSON
    data = response.json()  # Convierte la respuesta en un diccionario
    print(data)
else:
    # Si no fue exitosa, mostramos el código de error
    print(f"Error en la solicitud: {response.status_code}")
