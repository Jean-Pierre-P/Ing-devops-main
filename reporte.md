# DEVOPS CONTINUOUS FEEDBACK

## Resumen ejecutivo

Las siguientes mejoras ayudarán a incrementar la madurez DevOps del repositorio.

### 🔴 Alta prioridad

- Docker build funciona

### 🟠 Prioridad media

- Coverage equivalente JaCoCo

---

## Roadmap sugerido para alcanzar el 100%

1. Docker build funciona
2. Coverage equivalente JaCoCo
3. Docker Compose/K8s

---

## Cómo resolver los GAPs

### Docker build funciona

Impacto: El contenedor no puede construirse correctamente.

#### Cómo resolver

- Validar sintaxis Dockerfile
- Ejecutar docker build localmente
- Revisar COPY y CMD

#### Ejemplo

```

FROM node:20-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm","start"]

```

### Coverage equivalente JaCoCo

Impacto: No existe medición de cobertura.

#### Cómo resolver

- Agregar coverage
- Publicar cobertura pipeline

#### Ejemplo

```

npm test -- --coverage

```

---

## Tabla evaluación


| IE | Qué se revisará |
|---|---|
| IE1 | Dockerfile existe |
| IE1 | Docker build funciona |
| IE1 | Imágenes optimizadas |
| IE1 | Multi-stage build |
| IE2 | Existen tests |
| IE2 | Pipeline ejecuta tests |
| IE2 | Coverage equivalente JaCoCo |
| IE3 | Dependabot configurado |
| IE3 | SonarCloud/Snyk |
| IE3 | Bloqueos seguridad needs |
| IE3 | Limits CPU/MEM |
| IE3 | Reservations CPU/MEM |
| IE4 | Deploy automático |
| IE4 | README documentado |
| IE5 | Docker Compose/K8s |
| IE5 | Múltiples servicios |
| IE5 | Healthchecks |
| IE5 | Volumes |
| IE5 | Networks |


---

## Resultado revisión


| IE | Evaluación | Estado |
|---|---|---|
| IE1 | Dockerfile existe | ✅ IMPLEMENTADO |
| IE1 | Multi-stage build | ✅ IMPLEMENTADO |
| IE1 | Imágenes optimizadas | ✅ IMPLEMENTADO |
| IE1 | Docker build funciona | ⚠️ MEJORA PENDIENTE |
| IE4 | Pipeline GitHub Actions | ✅ IMPLEMENTADO |
| IE2 | Pipeline ejecuta tests | ✅ IMPLEMENTADO |
| IE3 | SonarCloud/Snyk | ✅ IMPLEMENTADO |
| IE3 | Bloqueos seguridad needs | ✅ IMPLEMENTADO |
| IE4 | Deploy automático | ✅ IMPLEMENTADO |
| IE2 | Tecnología detectada | ✅ IMPLEMENTADO |
| IE2 | Coverage equivalente JaCoCo | ⚠️ MEJORA PENDIENTE |
| IE3 | Dependabot configurado | ✅ IMPLEMENTADO |
| IE5 | Docker Compose/K8s | ⚠️ MEJORA PENDIENTE |
| IE4 | README documentado | ✅ IMPLEMENTADO |


---

## Detalle validaciones

### IE1 - Dockerfile existe

- Estado: ✅ IMPLEMENTADO
- Detalle: Dockerfile encontrado

- Evidencia:
```
Dockerfile
```


### IE1 - Multi-stage build

- Estado: ✅ IMPLEMENTADO
- Detalle: Usa multi-stage

- Evidencia:
```
Dockerfile revisado
```


### IE1 - Imágenes optimizadas

- Estado: ✅ IMPLEMENTADO
- Detalle: Usa imágenes optimizadas

- Evidencia:
```
Dockerfile revisado
```


### IE1 - Docker build funciona

- Estado: ⚠️ MEJORA PENDIENTE
- Detalle: Docker build falló

- Evidencia:
```
#0 building with "default" instance using docker driver

#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 377B done
#1 DONE 0.0s

#2 [auth] library/python:pull token for registry-1.docker.io
#2 DONE 0.0s

#3 [internal] load metadata for docker.io/library/python:3.11-slim
#3 DONE 0.4s

#4 [internal] load .dockerignore
#4 transferring context: 2B done
#4 DONE 0.0s

#5 [internal] load build context
#5 transferring context: 7.07MB 0.1s done
#5 DONE 0.1s

#6 [builder 1/
```

- Qué falta: Corregir Docker build


### IE4 - Pipeline GitHub Actions

- Estado: ✅ IMPLEMENTADO
- Detalle: 2 workflow(s) detectados

- Evidencia:
```
/home/runner/work/Ing-devops-main/Ing-devops-main/.github/workflows/ep02-devops-continuous-feedback.yml.yml, /home/runner/work/Ing-devops-main/Ing-devops-main/.github/workflows/ci-cd.yml
```


### IE2 - Pipeline ejecuta tests

- Estado: ✅ IMPLEMENTADO
- Detalle: Ejecuta tests

- Evidencia:
```
Workflow revisado
```


### IE3 - SonarCloud/Snyk

- Estado: ✅ IMPLEMENTADO
- Detalle: Tiene seguridad

- Evidencia:
```
Workflow revisado
```


### IE3 - Bloqueos seguridad needs

- Estado: ✅ IMPLEMENTADO
- Detalle: Usa needs

- Evidencia:
```
Workflow revisado
```


### IE4 - Deploy automático

- Estado: ✅ IMPLEMENTADO
- Detalle: Tiene deploy

- Evidencia:
```
Workflow revisado
```


### IE2 - Tecnología detectada

- Estado: ✅ IMPLEMENTADO
- Detalle: node

- Evidencia:
```
Archivos proyecto
```


### IE2 - Coverage equivalente JaCoCo

- Estado: ⚠️ MEJORA PENDIENTE
- Detalle: Coverage NO detectado para node

- Evidencia:
```

Tecnología: node

Coverage esperado:
Jest Coverage / NYC

Keywords:
--coverage, collectCoverage, coverageThreshold, nyc, istanbul, jest
      
```

- Qué falta: Agregar Jest Coverage / NYC


### IE3 - Dependabot configurado

- Estado: ✅ IMPLEMENTADO
- Detalle: Dependabot encontrado

- Evidencia:
```
.github/dependabot.yml
```


### IE5 - Docker Compose/K8s

- Estado: ⚠️ MEJORA PENDIENTE
- Detalle: No existe docker-compose

- Evidencia:
```
docker-compose.yml
```

- Qué falta: Agregar docker-compose


### IE4 - README documentado

- Estado: ✅ IMPLEMENTADO
- Detalle: README encontrado

- Evidencia:
```
README.md
```
