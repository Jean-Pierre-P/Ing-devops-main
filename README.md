## Documentación del Pipeline CI/CD y Calidad

### Trazabilidad y Calidad Garantizada
Para asegurar la calidad del entregable, este repositorio implementa un flujo automatizado mediante GitHub Actions que valida cada cambio subido (`push`):

1. **Pruebas Unitarias:** Se ejecutan de manera automática con `pytest` antes de compilar cualquier componente.
2. **Seguridad Activa (DevSecOps):** Se integra un análisis estático con **Snyk** enfocado en código y dependencias. Está configurado para **bloquear y abortar** el despliegue si detecta fallas críticas de seguridad.
3. **Escaneo Automático:** Se configuró **Dependabot** para monitorear vulnerabilidades en las librerías de forma diaria.
4. **Orquestación y Despliegue:** Se incluye la configuración para levantar el microservicio usando **Docker Compose**, asegurando un entorno reproducible en la nube o local.