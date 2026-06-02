def calcular_estado_servicio(activo: bool) -> str:
    """Devuelve el string de estado según si el servicio está activo."""
    return "ok" if activo else "degraded"


def construir_respuesta(codigo: int, mensaje: str) -> dict:
    """Arma el dict de respuesta estándar que usa la API."""
    return {"status_code": codigo, "message": mensaje}


def validar_payload(datos: dict, campos_requeridos: list) -> bool:
    """Verifica que un payload tenga todos los campos obligatorios."""
    return all(campo in datos for campo in campos_requeridos)


def sanitizar_entrada(texto: str) -> str:
    """Elimina caracteres peligrosos de una entrada de usuario."""
    caracteres_peligrosos = ["<", ">", "'", '"', ";", "--"]
    resultado = texto
    for c in caracteres_peligrosos:
        resultado = resultado.replace(c, "")
    return resultado.strip()


def calcular_paginacion(total: int, pagina: int, por_pagina: int) -> dict:
    """Calcula metadatos de paginación para una lista de resultados."""
    if por_pagina <= 0:
        raise ValueError("por_pagina debe ser mayor que cero")
    total_paginas = (total + por_pagina - 1) // por_pagina
    return {
        "total": total,
        "pagina_actual": pagina,
        "por_pagina": por_pagina,
        "total_paginas": total_paginas,
        "tiene_siguiente": pagina < total_paginas,
        "tiene_anterior": pagina > 1,
    }
