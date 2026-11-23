from datetime import time

from datos.modelos.horarioatencion import Horarioatencion
from datos.repositorio.repositorio_horarioatencion import (
    actualizar_horario,
    buscar_horario_por_id,
    guardar_horario,
    listar_horarios_activos,
)
from datos.repositorio.repositorio_restaurante import buscar_restaurante_por_id


def _convertir_hora(hora):
    try:
        return hora if isinstance(hora, time) else time.fromisoformat(hora)
    except (TypeError, ValueError):
        return None


def crear_horario(id_restaurante, dia_semana, hora_apertura, hora_cierre):
    restaurante = buscar_restaurante_por_id(id_restaurante)
    if not restaurante:
        return False, "No se encontró un restaurante activo."
    if not dia_semana.strip():
        return False, "El día de atención es obligatorio."

    apertura = _convertir_hora(hora_apertura)
    cierre = _convertir_hora(hora_cierre)
    if apertura is None or cierre is None or apertura == cierre:
        return False, "Las horas deben ser válidas y distintas (formato HH:MM)."

    horario = Horarioatencion(
        dia_semana=dia_semana.strip(),
        hora_apertura=apertura,
        hora_cierre=cierre,
        id_restaurante=restaurante,
        habilitado=True,
    )
    return guardar_horario(horario)


def obtener_horarios():
    return listar_horarios_activos()


def modificar_horario(
    id_horario,
    id_restaurante,
    dia_semana,
    hora_apertura,
    hora_cierre,
):
    horario = buscar_horario_por_id(id_horario)
    if not horario:
        return False, "Horario no encontrado."
    restaurante = buscar_restaurante_por_id(id_restaurante)
    if not restaurante:
        return False, "No se encontró un restaurante activo."
    if not dia_semana.strip():
        return False, "El día de atención es obligatorio."

    apertura = _convertir_hora(hora_apertura)
    cierre = _convertir_hora(hora_cierre)
    if apertura is None or cierre is None or apertura == cierre:
        return False, "Las horas deben ser válidas y distintas (formato HH:MM)."

    horario.id_restaurante = restaurante
    horario.dia_semana = dia_semana.strip()
    horario.hora_apertura = apertura
    horario.hora_cierre = cierre
    return actualizar_horario(horario)


def eliminar_horario_logico(id_horario):
    horario = buscar_horario_por_id(id_horario)
    if not horario:
        return False, "Horario no encontrado."

    horario.habilitado = False
    return actualizar_horario(horario)
