# Kopi Challenge by Rastukis

Este proyecto implementa una API en **FastAPI** que se conecta a un modelo **LLM** ejecujado con Ollama (https://ollama.ai/)
Permite interactuar con el modelo de lenguaje a través de endpoint REST, manteniendo un historial básico de conversaión.

## Estructura del proyecto
```
|---- database.py          # Conexión a la base de datos en Postgres
|---- main.py              # Contiene el Endpoint que se utiliza para la interacción con el LLM
|---- models.py            # Definición de los modelos que registran la conversación
|---- requirements.txt     # Dependecnias del proyecto
|---- schemas.py           # Esquemas que utiliza el Endpoint como datos de entrada
|---- services.py          # Servicios que interactuan con la base para Obtener y guardar los datos en Postgres
|---- docker-compose.yml   # Orquestación: API - DB - Ollama
|---- Dockerfile           # Imagen del servicio
```

## Requisitos
- Python 3.11+
- Ollama como un servidor local
- PostgreSQL
- (Opcional) Docker

## Instalación local
1. Clonar el repositorio
```bash
git clone https://github.com/rastukis/kopi_challenge_rastukis.git
cd kopi_challenge_rastukis
```
2. Crear entorno virtual e instalar requeriments
```bash
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

3. Configura las variables de entorno
```bash
cp .env.example .env 
```
4. Ejecuta el servidor 
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 
```

## Ejecución con Docker
1. Construir los servicios e inicializarlos:
```bash
docker-compose up --build
```

## Endpoint principal
### POST /debate-chatbot
#### Request
```json
{
    "conversation_id": "93adca4d-6e6f-47df-804b-85e56c387d36",
    "message": "Crees que la Tierra es Plana?"
}
```

#### Response
```json
{
    "conversation_id": "93adca4d-6e6f-47df-804b-85e56c387d36",
    "message": [
        {
            "role": "user",
            "content": "Crees que la tierra es plana?"
        },
        {
            "role": "assistant",
            "content": "No, la Tierra no es plana. Es una esfera. La falsa creencia de que la Tierra es plana se debe a que los observadores en la superficie terrestre no pueden ver el efecto de la curvatura debido a las limitaciones de su visión y la capacidad de la tecnología disponible hasta ahora. Sin embargo, la ciencia ha demostrado con firmez que la Tierra es una esfera en forma de pirámide."
        },
        {
            "role": "user",
            "content": "Pero si hay evidencia, cambiarias de postura?"
        },
        {
            "role": "assistant",
            "content": "Sí, hay mucha evidencia científica que demuestra que la Tierra es un esfero. Algunos ejemplos incluyen:\n\n1. La curvatura de la superficie de la Tierra se puede observar en la forma en que los objetos se ven a distancia, como el horizonte o los puntos más altos de las montañas.\n2. Las mareas son causadas por la curvatura de la Tierra y la gravedad. La superficie de la Tierra es ligeramente curva, lo que significa que la marea puede ser un poco mayor en algunas partes del planeta que otras.\n3. Las órbitas de los planetas son elípticas, no circulares. Esto significa que la distancia entre el planeta y el Sol no es constante a lo largo del año, lo que afecta la cantidad de sol que recibe en diferentes partes del planeta.\n4. Las estaciones son causadas por la inclinación del eje de la Tierra en relación con su órbita alrededor del Sol. La inclinación del eje de la Tierra es de aproximadamente 23.5 grados, lo que significa que los rayos solares que llegan a diferentes partes del planeta tienen diferentes ángulos y duraciones de día y noche.\n\nEstas son solo algunas de las muchas evidencias que demuestran que la Tierra es un esfero."
        }
    ]
}
```

