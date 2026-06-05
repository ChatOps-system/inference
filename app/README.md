# Inference Service - chatops

Construido con:

- uv
- FastAPI
- Ollama

## Setup

1. Instalar dependencias

```bash
uv sync
```

2. Activar entorno virtual

```bash
.venv\Scripts\activate
```

3. Iniciar el proyecto

```bash
fastapi dev
```

4. Ejecutar tests

```bash
pytest
```

5. Variables de entorno:

Descripción de variables:

- `MODEL_NAME`: Nombre del modelo que se utilizará para la generación del borrador de reporte de incidente.
- `BASE_URL`: URL del lugar donde estará servido el modelo.
- `API_KEY`: Clave de acceso al modelo.
