from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from opencage.geocoder import OpenCageGeocode
from typing import Optional
import herepy
import uvicorn

app = FastAPI()

API_KEY = "0uU1kNW3QZuyhsxxq2Ma194iMUwrxhgut92XkdDlyDk"
geocoder = herepy.GeocoderApi(API_KEY)

# Modelo para la solicitud
class AddressRequest(BaseModel):
    direccion: str
    conjunto: Optional[str] = None  # Hacer conjunto opcional
    barrio: str
    ciudad: str

# Ruta principal para convertir direcciones a coordenadas
@app.post("/geocode")
def geocode_address(datos: AddressRequest):
    # Construir la dirección sin barrio
    if datos.conjunto:
        full_address = f"{datos.direccion}, {datos.conjunto}, {datos.barrio}, {datos.ciudad}, Colombia"
    else:
        full_address = f"{datos.direccion}, {datos.barrio}, {datos.ciudad}, Colombia"
     
    print(f"Se recibió la dirección: {full_address}")
    try:

        resultado = geocoder.free_form(full_address)
        print(resultado.items[0]['position'])
        if resultado:
            lat = resultado.items[0]['position']['lat']
            lon = resultado.items[0]['position']['lng']
            return {"latitud": lat, "longitud": lon}
        else:
            raise HTTPException(status_code=404, detail="No se encontraron coordenadas para la dirección proporcionada.")

    except GeocoderTimedOut:
        raise HTTPException(status_code=500, detail="Tiempo de espera excedido en la solicitud.")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")

@app.get("/")
def mensajeBienvenida():
    return {"mensaje": "Bienvenido a la API de geocodificación elaborada para CareConnect"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
