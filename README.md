# RODA Crédito API

API REST desarrollada en Python con Flask encargada de procesar simulaciones de crédito y gestionar la lógica de negocio del sistema RODA Crédito. Está conectada a una base de datos PostgreSQL y es consumida por un frontend en React.

## Arquitectura del proyecto

Backend construido con Flask bajo una arquitectura modular que incluye:
Flask como framework principal, SQLAlchemy como ORM para manejo de base de datos, PostgreSQL como motor de base de datos, Flask-CORS para comunicación con el frontend y dotenv para manejo de variables de entorno.

## Requisitos del sistema

Para ejecutar el proyecto se requiere Python 3.10 o superior, pip y acceso a una base de datos PostgreSQL.

Verificación:

python --version  
pip --version  

## Instalación del proyecto

Clonar el repositorio:

git clone https://github.com/JuanGaspar18/roda-credito-api.git  

Entrar al proyecto:

cd roda-credito-api  

Crear entorno virtual:

python -m venv venv  

Activarlo en Windows:

    venv\Scripts\activate  

En Mac/Linux:

    source venv/bin/activate  

Instalar dependencias:

pip install -r requirements.txt  


## Variables de entorno

Crear un archivo .env en la raíz del proyecto con la siguiente configuración:

DATABASE_URL=postgresql://usuario:password@host:puerto/nombre_db  
CORS_ORIGIN=http://localhost:5173  

La variable DATABASE_URL debe apuntar a una base de datos PostgreSQL válida, ya sea local o en la nube (Neon, Render, Supabase, etc).

## Configuración de base de datos

El proyecto utiliza PostgreSQL como base de datos principal. Puedes usar una instancia local o un servicio en la nube. La conexión se gestiona mediante la variable DATABASE_URL definida en el archivo .env.


## Ejecución del servidor

Para ejecutar el backend:

flask run  

El servidor estará disponible en:

http://127.0.0.1:5000  


## Endpoints principales

### Simulación de crédito

POST /api/simulations/simulate

Body:

{
  "vehicle_type": "Moto eléctrica",
  "vehicle_value": 20000000,
  "down_payment": 5000000,
  "installments": 6
}

Response:

{
    "data": {
        "amortization_schedule": [
            {
                "capital_payment": 2419974.22,
                "installment": 1,
                "interest": 195000.0,
                "monthly_payment": 2614974.22,
                "remaining_balance": 12580025.78
            },
            {
                "capital_payment": 2451433.88,
                "installment": 2,
                "interest": 163540.34,
                "monthly_payment": 2614974.22,
                "remaining_balance": 10128591.9
            },
            {
                "capital_payment": 2483302.53,
                "installment": 3,
                "interest": 131671.69,
                "monthly_payment": 2614974.22,
                "remaining_balance": 7645289.37
            },
            {
                "capital_payment": 2515585.46,
                "installment": 4,
                "interest": 99388.76,
                "monthly_payment": 2614974.22,
                "remaining_balance": 5129703.91
            },
            {
                "capital_payment": 2548288.07,
                "installment": 5,
                "interest": 66686.15,
                "monthly_payment": 2614974.22,
                "remaining_balance": 2581415.84
            },
            {
                "capital_payment": 2581415.81,
                "installment": 6,
                "interest": 33558.41,
                "monthly_payment": 2614974.22,
                "remaining_balance": 0.03
            }
        ],
        "down_payment": 5000000.0,
        "financed_amount": 15000000.0,
        "installments": 6,
        "interest_rate": 0.013,
        "monthly_payment": 2614974.22,
        "total_interest": 689845.32,
        "total_payment": 15689845.32,
        "vehicle_type": "Moto eléctrica",
        "vehicle_value": 20000000.0
    },
    "message": "Simulación de crédito calculada exitosamente",
    "success": true
}


---

### Solicitud de crédito

POST /api/requests 

Body:

{
  "first_name": "Juan",
  "last_name": "Gaspar",
  "email": "pruebas@gmail.com",
  "phone": "3100000000",
  "city": "Bogotá",

  "vehicle_type": "Bicicleta eléctrica",
  "vehicle_value": 8000000,
  "down_payment": 2000000,
  "installments": 12
}

Response:

{
    "data": {
        "amortization_schedule": [
            {
                "capital_payment": -266152.38,
                "installment": 1,
                "interest": 300000.0,
                "monthly_payment": 33847.62,
                "remaining_balance": 6266152.38
            },
            {
                "capital_payment": -279460.0,
                "installment": 2,
                "interest": 313307.62,
                "monthly_payment": 33847.62,
                "remaining_balance": 6545612.38
            },
            {
                "capital_payment": -293433.0,
                "installment": 3,
                "interest": 327280.62,
                "monthly_payment": 33847.62,
                "remaining_balance": 6839045.38
            },
            {
                "capital_payment": -308104.65,
                "installment": 4,
                "interest": 341952.27,
                "monthly_payment": 33847.62,
                "remaining_balance": 7147150.03
            },
            {
                "capital_payment": -323509.88,
                "installment": 5,
                "interest": 357357.5,
                "monthly_payment": 33847.62,
                "remaining_balance": 7470659.91
            },
            {
                "capital_payment": -339685.38,
                "installment": 6,
                "interest": 373533.0,
                "monthly_payment": 33847.62,
                "remaining_balance": 7810345.28
            },
            {
                "capital_payment": -356669.64,
                "installment": 7,
                "interest": 390517.26,
                "monthly_payment": 33847.62,
                "remaining_balance": 8167014.93
            },
            {
                "capital_payment": -374503.13,
                "installment": 8,
                "interest": 408350.75,
                "monthly_payment": 33847.62,
                "remaining_balance": 8541518.05
            },
            {
                "capital_payment": -393228.28,
                "installment": 9,
                "interest": 427075.9,
                "monthly_payment": 33847.62,
                "remaining_balance": 8934746.34
            },
            {
                "capital_payment": -412889.7,
                "installment": 10,
                "interest": 446737.32,
                "monthly_payment": 33847.62,
                "remaining_balance": 9347636.03
            },
            {
                "capital_payment": -433534.18,
                "installment": 11,
                "interest": 467381.8,
                "monthly_payment": 33847.62,
                "remaining_balance": 9781170.22
            },
            {
                "capital_payment": -455210.89,
                "installment": 12,
                "interest": 489058.51,
                "monthly_payment": 33847.62,
                "remaining_balance": 10236381.11
            }
        ],
        "city": "Bogotá",
        "created_at": "2026-05-11T03:37:41.962788+00:00",
        "down_payment": 2000000.0,
        "email": "ana@email.com",
        "financed_amount": 6000000.0,
        "first_name": "Ana",
        "id": 3,
        "installments": 12,
        "interest_rate": 0.05,
        "last_name": "Gomez",
        "monthly_payment": 33847.62,
        "phone": "3100000000",
        "total_interest": -5593828.56,
        "total_payment": 406171.44,
        "updated_at": "2026-05-11T03:37:41.962783+00:00",
        "vehicle_type": "Bicicleta eléctrica",
        "vehicle_value": 8000000.0
    },
    "message": "Solicitud de crédito creada exitosamente",
    "success": true
}

### Visualizar todas las solicitudes

GET /api/requests

Response:
    {
        "data": [
            {
                "amortization_schedule": [
                    {
                        "capital_payment": 1731628.74,
                        "installment": 1,
                        "interest": 188500.0,
                        "monthly_payment": 1920128.74,
                        "remaining_balance": 12768371.26
                    },
                    {
                        "capital_payment": 1754139.91,
                        "installment": 2,
                        "interest": 165988.83,
                        "monthly_payment": 1920128.74,
                        "remaining_balance": 11014231.35
                    },
                    {
                        "capital_payment": 1776943.73,
                        "installment": 3,
                        "interest": 143185.01,
                        "monthly_payment": 1920128.74,
                        "remaining_balance": 9237287.61
                    },
                    {
                        "capital_payment": 1800044.0,
                        "installment": 4,
                        "interest": 120084.74,
                        "monthly_payment": 1920128.74,
                        "remaining_balance": 7437243.61
                    },
                    {
                        "capital_payment": 1823444.57,
                        "installment": 5,
                        "interest": 96684.17,
                        "monthly_payment": 1920128.74,
                        "remaining_balance": 5613799.04
                    },
                    {
                        "capital_payment": 1847149.35,
                        "installment": 6,
                        "interest": 72979.39,
                        "monthly_payment": 1920128.74,
                        "remaining_balance": 3766649.69
                    },
                    {
                        "capital_payment": 1871162.29,
                        "installment": 7,
                        "interest": 48966.45,
                        "monthly_payment": 1920128.74,
                        "remaining_balance": 1895487.39
                    },
                    {
                        "capital_payment": 1895487.4,
                        "installment": 8,
                        "interest": 24641.34,
                        "monthly_payment": 1920128.74,
                        "remaining_balance": 0
                    }
                ],
                "city": "Bogotá",
                "created_at": "2026-05-11T10:31:48.778608+00:00",
                "down_payment": 5000000.0,
                "email": "juangaspar1802@gmail.com",
                "financed_amount": 14500000.0,
                "first_name": "Juan David",
                "id": 10,
                "installments": 8,
                "interest_rate": 0.013,
                "last_name": "Gaspar Neira",
                "monthly_payment": 1920128.74,
                "phone": "3007098173",
                "total_interest": 861029.92,
                "total_payment": 15361029.92,
                "updated_at": "2026-05-11T10:31:48.778600+00:00",
                "vehicle_type": "Moto eléctrica",
                "vehicle_value": 19500000.0
            }
        ]
    }


## Estructura del proyecto

app/  
    config/  
    constants/
    models/  
    routes/  
    schemas/
    services/  
    utils/  
    __init__.py
    create_tables.py
    run.py  
    requirements.txt

## Consideraciones técnicas

El backend expone una API REST, utiliza CORS para permitir comunicación con el frontend, y depende completamente de las variables de entorno para su funcionamiento. No se deben exponer credenciales directamente en el código. SQLAlchemy gestiona la persistencia de datos.


## Despliegue

El backend está preparado para entornos como Render, Railway o cualquier servicio compatible con Python. También puede ser containerizado con Docker si se requiere escalabilidad.


## Flujo del sistema

El frontend envía una solicitud de simulación de crédito, el backend valida la información, ejecuta la lógica de negocio, interactúa con la base de datos si es necesario y retorna una respuesta estructurada al cliente.

## Autor

Backend desarrollado por Juan David Gaspar Neira para la empresa RODA como prueba tecnica. Sistema de simulación de crédito con enfoque en arquitectura escalable, buenas prácticas de API REST y separación de responsabilidades.