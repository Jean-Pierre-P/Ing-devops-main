import pytest
import os
import sys

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


# ---------------------------------------------------------------------------
# TESTS — Estado del servicio
# ---------------------------------------------------------------------------


def test_estado_servicio_activo():
    resultado = calcular_estado_servicio(True)
    assert resultado == "ok"


def test_estado_servicio_inactivo():
    resultado = calcular_estado_servicio(False)
    assert resultado == "degraded"


# ---------------------------------------------------------------------------
# TESTS — Construcción de respuesta
# ---------------------------------------------------------------------------


def test_respuesta_exitosa():
    resp = construir_respuesta(200, "operación completada")
    assert resp["status_code"] == 200
    assert "operación completada" in resp["message"]


def test_respuesta_error_cliente():
    resp = construir_respuesta(400, "parámetro inválido")
    assert resp["status_code"] == 400


def test_respuesta_error_servidor():
    resp = construir_respuesta(500, "error interno")
    assert resp["status_code"] == 500
    assert resp["message"] == "error interno"


def test_respuesta_tiene_claves_correctas():
    resp = construir_respuesta(201, "recurso creado")
    assert "status_code" in resp
    assert "message" in resp


# ---------------------------------------------------------------------------
# TESTS — Validación de payload
# ---------------------------------------------------------------------------


def test_payload_valido_con_todos_los_campos():
    datos = {"nombre": "test", "valor": 42, "activo": True}
    assert validar_payload(datos, ["nombre", "valor", "activo"]) is True


def test_payload_invalido_falta_campo():
    datos = {"nombre": "test"}
    assert validar_payload(datos, ["nombre", "valor"]) is False


def test_payload_vacio_falla():
    assert validar_payload({}, ["nombre"]) is False


def test_payload_sin_campos_requeridos_siempre_pasa():
    # Si no hay campos requeridos, cualquier dict es válido
    assert validar_payload({"x": 1}, []) is True


# ---------------------------------------------------------------------------
# TESTS — Sanitización de entrada
# ---------------------------------------------------------------------------


def test_sanitizar_elimina_menor_mayor():
    entrada = "<script>alert(1)</script>"
    resultado = sanitizar_entrada(entrada)
    assert "<" not in resultado
    assert ">" not in resultado


def test_sanitizar_elimina_comillas():
    entrada = "' OR '1'='1"
    resultado = sanitizar_entrada(entrada)
    assert "'" not in resultado


def test_sanitizar_elimina_doble_guion():
    entrada = "admin--"
    resultado = sanitizar_entrada(entrada)
    assert "--" not in resultado


def test_sanitizar_texto_limpio_no_cambia():
    entrada = "hola mundo"
    assert sanitizar_entrada(entrada) == "hola mundo"


def test_sanitizar_elimina_espacios_extremos():
    assert sanitizar_entrada("  texto  ") == "texto"


# ---------------------------------------------------------------------------
# TESTS — Paginación
# ---------------------------------------------------------------------------


def test_paginacion_primera_pagina():
    p = calcular_paginacion(total=50, pagina=1, por_pagina=10)
    assert p["total_paginas"] == 5
    assert p["tiene_siguiente"] is True
    assert p["tiene_anterior"] is False


def test_paginacion_ultima_pagina():
    p = calcular_paginacion(total=50, pagina=5, por_pagina=10)
    assert p["tiene_siguiente"] is False
    assert p["tiene_anterior"] is True


def test_paginacion_pagina_intermedia():
    p = calcular_paginacion(total=100, pagina=3, por_pagina=20)
    assert p["tiene_siguiente"] is True
    assert p["tiene_anterior"] is True


def test_paginacion_total_no_divisible():
    p = calcular_paginacion(total=25, pagina=1, por_pagina=10)
    assert p["total_paginas"] == 3


def test_paginacion_por_pagina_cero_lanza_error():
    with pytest.raises(ValueError):
        calcular_paginacion(total=10, pagina=1, por_pagina=0)


def test_paginacion_devuelve_metadatos_completos():
    p = calcular_paginacion(total=30, pagina=2, por_pagina=10)
    assert "total" in p
    assert "pagina_actual" in p
    assert "por_pagina" in p
    assert "total_paginas" in p