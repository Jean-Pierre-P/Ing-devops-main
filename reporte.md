# DEVOPS CONTINUOUS FEEDBACK

## Resumen ejecutivo

Las siguientes mejoras ayudarán a incrementar la madurez DevOps del repositorio.

### 🟠 Prioridad media

- Coverage equivalente JaCoCo

---

## Roadmap sugerido para alcanzar el 100%

1. Coverage equivalente JaCoCo

---

## Cómo resolver los GAPs

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
| IE1 | Docker build funciona | ✅ IMPLEMENTADO |
| IE4 | Pipeline GitHub Actions | ✅ IMPLEMENTADO |
| IE2 | Pipeline ejecuta tests | ✅ IMPLEMENTADO |
| IE3 | SonarCloud/Snyk | ✅ IMPLEMENTADO |
| IE3 | Bloqueos seguridad needs | ✅ IMPLEMENTADO |
| IE4 | Deploy automático | ✅ IMPLEMENTADO |
| IE2 | Tecnología detectada | ✅ IMPLEMENTADO |
| IE2 | Coverage equivalente JaCoCo | ⚠️ MEJORA PENDIENTE |
| IE3 | Dependabot configurado | ✅ IMPLEMENTADO |
| IE5 | Docker Compose/K8s | ✅ IMPLEMENTADO |
| IE5 | Múltiples servicios | ✅ IMPLEMENTADO |
| IE5 | Healthchecks | ✅ IMPLEMENTADO |
| IE5 | Volumes | ✅ IMPLEMENTADO |
| IE5 | Networks | ✅ IMPLEMENTADO |
| IE3 | Limits CPU/MEM | ✅ IMPLEMENTADO |
| IE3 | Reservations CPU/MEM | ✅ IMPLEMENTADO |
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

- Estado: ✅ IMPLEMENTADO
- Detalle: Docker build exitoso

- Evidencia:
```
-
```


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

- Estado: ✅ IMPLEMENTADO
- Detalle: docker-compose encontrado

- Evidencia:
```
docker-compose.yml
```


### IE5 - Múltiples servicios

- Estado: ✅ IMPLEMENTADO
- Detalle: 2 servicios

- Evidencia:
```
app, db
```


### IE5 - Healthchecks

- Estado: ✅ IMPLEMENTADO
- Detalle: Tiene healthchecks

- Evidencia:
```
docker-compose revisado
```


### IE5 - Volumes

- Estado: ✅ IMPLEMENTADO
- Detalle: Tiene volumes

- Evidencia:
```
docker-compose revisado
```


### IE5 - Networks

- Estado: ✅ IMPLEMENTADO
- Detalle: Tiene networks

- Evidencia:
```
docker-compose revisado
```


### IE3 - Limits CPU/MEM

- Estado: ✅ IMPLEMENTADO
- Detalle: Tiene limits

- Evidencia:
```
docker-compose revisado
```


### IE3 - Reservations CPU/MEM

- Estado: ✅ IMPLEMENTADO
- Detalle: Tiene reservations

- Evidencia:
```
docker-compose revisado
```


### IE4 - README documentado

- Estado: ✅ IMPLEMENTADO
- Detalle: README encontrado

- Evidencia:
```
README.md
```
