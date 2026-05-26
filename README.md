## Documentación del Pipeline CI/CD y Calidad

### Trazabilidad y Calidad Garantizada
Para asegurar la calidad del entregable, este repositorio implementa un flujo automatizado mediante GitHub Actions que valida cada cambio subido (`push`):

1. **Pruebas Unitarias:** Se ejecutan de manera automática con `pytest` antes de compilar cualquier componente.
2. **Seguridad Activa (DevSecOps):** Se integra un análisis estático con **Snyk** enfocado en código y dependencias. Está configurado para **bloquear y abortar** el despliegue si detecta fallas críticas de seguridad.
3. **Escaneo Automático:** Se configuró **Dependabot** para monitorear vulnerabilidades en las librerías de forma diaria.
4. **Orquestación y Despliegue:** Se incluye la configuración para levantar el microservicio usando **Docker Compose**, asegurando un entorno reproducible en la nube o local.

# Microservicio DevOps — Pipeline CI/CD

## Descripción general

Este repositorio implementa un microservicio Python con un pipeline de integración y entrega continua completo, construido sobre GitHub Actions. El objetivo es automatizar desde la validación del código hasta el despliegue en un entorno simulado con Docker Compose, garantizando calidad y trazabilidad en cada etapa.

---

## Arquitectura del sistema

El sistema está compuesto por dos servicios principales que se comunican dentro de una red privada de contenedores:

```
                        ┌─────────────────────────────────────┐
                        │          Docker Compose              │
                        │                                     │
  Internet / CI  ──────►│  ┌──────────────┐                  │
   (puerto 8000)        │  │     app      │  backend-network  │
                        │  │  Python 3.11 │◄───────────────►  │
                        │  │  puerto 8000 │                   │
                        │  └──────┬───────┘  ┌────────────┐  │
                        │         │           │     db     │  │
                        │         └──────────►│ PostgreSQL │  │
                        │                     │ puerto 5432│  │
                        │                     └────────────┘  │
                        │                                     │
                        │  Volúmenes: app-logs, db-data       │
                        └─────────────────────────────────────┘
```

### Servicio `app`

- Imagen base: `python:3.11-slim` (multi-stage build)
- Puerto expuesto: `8000`
- Responsable de recibir las peticiones HTTP y procesarlas
- Se conecta a la base de datos a través de la red interna `backend-network`
- Escribe logs en el volumen `app-logs`
- Límite de recursos: 0.75 CPU / 512 MB RAM

### Servicio `db`

- Imagen: `postgres:16-alpine`
- Puerto interno: `5432` (no expuesto al exterior)
- Almacena el estado persistente de la aplicación
- Datos guardados en el volumen `db-data`
- Límite de recursos: 0.50 CPU / 256 MB RAM

### Redes

| Red | Tipo | Propósito |
|---|---|---|
| `backend-network` | bridge / internal | Comunicación privada entre app y db |
| `frontend-network` | bridge | Exposición del servicio app hacia el exterior |

### Volúmenes

| Volumen | Montado en | Propósito |
|---|---|---|
| `db-data` | `/var/lib/postgresql/data` | Persistencia de base de datos |
| `app-logs` | `/app/logs` | Logs del microservicio |

---

## Pipeline CI/CD

El pipeline está implementado en GitHub Actions y se activa automáticamente en cada `push` o `pull_request` sobre `main`. Los jobs se ejecutan en cadena usando `needs`, de forma que un fallo en cualquier etapa detiene el proceso completo.

```
push / pull_request
       │
       ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────────────┐     ┌────────────┐
│ unit-tests  │────►│ security-snyk│────►│ build-and-orchestrate│────►│   deploy   │
│  (IE2)      │     │    (IE3)     │     │     (IE1, IE5)       │     │   (IE4)    │
└─────────────┘     └──────────────┘     └─────────────────────┘     └────────────┘
```

### Etapa 1 — Pruebas unitarias con cobertura

Ejecuta los tests del proyecto con `pytest` y genera un reporte de cobertura en formato XML. El reporte se publica como artefacto del workflow para revisión posterior.

```bash
pytest test_main.py --cov=. --cov-report=term-missing --cov-report=xml -v
```

### Etapa 2 — Análisis de seguridad con Snyk

Escanea las dependencias del proyecto buscando vulnerabilidades conocidas. El parámetro `continue-on-error: false` garantiza que el pipeline se **bloquea y aborta** si Snyk detecta problemas críticos, impidiendo que código inseguro llegue a producción.

El escaneo automático de dependencias está complementado por **Dependabot**, configurado para revisar actualizaciones de paquetes pip de forma diaria.

### Etapa 3 — Construcción y orquestación

Construye la imagen Docker del microservicio usando el Dockerfile multi-stage e inicia los servicios con Docker Compose. Se valida que la imagen se haya construido correctamente antes de pasar a la siguiente etapa.

### Etapa 4 — Despliegue automatizado

Levanta el entorno completo con `docker compose up -d --build`, espera a que los servicios estén operativos y ejecuta un health check para confirmar que el microservicio responde. Los logs del despliegue se publican como artefacto del workflow.

---

## Trazabilidad del proceso

Cada ejecución del pipeline queda registrada en GitHub Actions con:

- **Logs de cada job**: disponibles en tiempo real en la pestaña Actions del repositorio.
- **Artefactos publicados**: el reporte de cobertura (`coverage.xml`) y los logs de despliegue (`deploy-logs`) quedan adjuntos a cada ejecución.
- **Estado del pipeline**: cada commit muestra un ícono de estado (✅ / ❌) directamente en el historial de Git, permitiendo identificar qué cambio introdujo un fallo.
- **Bloqueo por seguridad**: si Snyk detecta vulnerabilidades, el job falla con código de salida distinto de cero, impidiendo que el flujo continúe. Esto queda registrado explícitamente en los logs.

---

## Instrucciones de uso local

### Requisitos

- Docker y Docker Compose instalados
- Python 3.11 o superior (solo para ejecutar tests localmente)

### Levantar el entorno

```bash
docker compose up -d
```

### Ejecutar tests

```bash
pip install -r requirements.txt
pytest test_main.py --cov=. -v
```

### Ver logs

```bash
docker compose logs -f app
```

### Detener el entorno

```bash
docker compose down
```

---

## Herramientas utilizadas

| Herramienta | Versión | Propósito |
|---|---|---|
| Python | 3.11 | Lenguaje del microservicio |
| pytest | 8.2.2 | Ejecución de tests unitarios |
| pytest-cov | 5.0.0 | Reporte de cobertura de código |
| Docker | 24+ | Contenedores |
| Docker Compose | v2 | Orquestación local |
| GitHub Actions | — | CI/CD automatizado |
| Snyk | — | Análisis de seguridad de dependencias |
| Dependabot | — | Monitoreo automático de vulnerabilidades | 
