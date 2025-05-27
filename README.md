# CareConnect Geocoding API

## Descripción
La **CareConnect Geocoding API** es una aplicación desarrollada con FastAPI que convierte direcciones en Colombia a coordenadas geográficas (latitud y longitud) utilizando el servicio de geocodificación de HERE Maps. Esta API está diseñada para integrarse con el proyecto CareConnect, permitiendo obtener coordenadas precisas a partir de información de dirección proporcionada.

## Características
- Convierte direcciones completas (dirección, conjunto opcional, barrio y ciudad) en coordenadas geográficas.
- Utiliza la API de HERE Maps para geocodificación precisa.
- Soporta solicitudes POST con validación de datos mediante Pydantic.
- Manejo de errores robusto para tiempos de espera y otros problemas de geocodificación.
- Endpoint de bienvenida para verificar el funcionamiento de la API.

## Requisitos previos
- Python 3.8 o superior
- Una clave de API válida de HERE Maps (`API_KEY`)
- Acceso a internet para realizar solicitudes a la API de HERE Maps

## Instalación
1. **Clona el repositorio o descarga el código fuente**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_DIRECTORIO>
   ```

2. **Crea y activa un entorno virtual** (opcional, pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install fastapi uvicorn geopy herepy pydantic opencage-geocoder
   ```

4. **Configura la clave de API**:
   Reemplaza el valor de `API_KEY` en el archivo `app.py` con tu clave de API de HERE Maps:
   ```python
   API_KEY = "TU_CLAVE_DE_API_AQUÍ"
   ```

## Reconstruir el entorno virtual en otra máquina
Si otra persona (o tú mismo en otro equipo) clona el repositorio, deberá seguir estos pasos para configurar el entorno virtual correctamente:

1. **Crear un nuevo entorno virtual**:
   ```bash
   python -m venv venv
   ```
   O
   ```bash
   python3 -m venv venv
   ```

2. **Activar el entorno virtual**:
   - **Windows (CMD o PowerShell)**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la clave de API**:
   Asegúrate de reemplazar el valor de `API_KEY` en el archivo `app.py` con una clave válida de HERE Maps.

5. **Inicializar el web service**:
   ```bash
   python app.py
   ```
   O
   ```bash
   python3 app.py
   ```

Estos pasos aseguran que el entorno virtual esté correctamente configurado y que todas las dependencias necesarias sean instaladas para ejecutar el proyecto sin problemas.

## Uso
1. **Inicia el servidor**:
   Ejecuta el siguiente comando para iniciar la API:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8001
   ```

2. **Accede a la documentación interactiva**:
   Una vez que el servidor esté en ejecución, abre tu navegador y visita:
   ```
   http://localhost:8001/docs
   ```
   Esto mostrará la interfaz de Swagger UI, donde puedes probar los endpoints de la API.

3. **Endpoints disponibles**:
   - **GET /**: Devuelve un mensaje de bienvenida.
     - Ejemplo de respuesta:
       ```json
       {"mensaje": "Bienvenido a la API de geocodificación elaborada para CareConnect"}
       ```
   - **POST /geocode**: Convierte una dirección en coordenadas geográficas.
     - Cuerpo de la solicitud (JSON):
       ```json
       {
           "direccion": "Calle 123 #45-67",
           "conjunto": "Conjunto Residencial Los Pinos",
           "barrio": "El Poblado",
           "ciudad": "Medellín"
       }
       ```
       Nota: El campo `conjunto` es opcional.
     - Ejemplo de respuesta exitosa:
       ```json
       {"latitud": 6.123456, "longitud": -75.654321}
       ```
     - Ejemplo de respuesta de error:
       ```json
       {"detail": "No se encontraron coordenadas para la dirección proporcionada."}
       ```

4. **Prueba con cURL**:
   Ejemplo de solicitud POST:
   ```bash
   curl -X POST "http://localhost:8001/geocode" -H "Content-Type: application/json" -d '{"direccion":"Calle 123 #45-67","conjunto":"Conjunto Residencial Los Pinos","barrio":"El Poblado","ciudad":"Medellín"}'
   ```

## Estructura del proyecto
```
careconnect-geocoding-api/
├── app.py          # Código principal de la API
├── requirements.txt # Lista de dependencias
├── README.md       # Este archivo
```

## Notas
- Asegúrate de que la clave de API de HERE Maps esté configurada correctamente para evitar errores de autenticación.
- La API está diseñada específicamente para direcciones en Colombia, por lo que siempre se agrega ", Colombia" a la consulta de geocodificación.
- Maneja los errores de tiempo de espera (`GeocoderTimedOut`) y otros errores inesperados con códigos de estado HTTP adecuados.

## Contacto
Para soporte o consultas, contacta al equipo de CareConnect a través de [correo electrónico] o [otro medio de contacto].