from detector_neural_network.app_exception import AppException

CALL_EXCEPTION_DEFAULT = True


# ---------------------------------------------------------------------------
#   Целые числа
# ---------------------------------------------------------------------------
def get_int(val: int | float | str, field_name: str, call_raise: bool = CALL_EXCEPTION_DEFAULT) -> int | None:
    """
    Преобразует значение в целое число.

    Parameters
    ----------
    val : int, float, str
        Значение, которое требуется преобразовать в целое число;
    field_name : str
        Название поля для сообщения об ошибке;
    call_raise : bool, optional
        Флаг, определяющий, следует ли возбуждать исключение в случае ошибки. По умолчанию False.

    Returns
    -------
    int or None
        Преобразованное целое число или None, если преобразование невозможно и call_raise=False.

    Raises
    ------
    AppException
        Если преобразование не удалось и call_raise=True.
    """
    try:
        val = int(val)
    except ValueError:
        if call_raise:
            raise AppException("Ошибка ввода", f"""Введите целое число в поле "{field_name!r}".""")
        return None
    return val


def get_int_and_positive(
    val: int | float | str, field_name: str, call_raise: bool = CALL_EXCEPTION_DEFAULT
) -> int | None:
    """
    Преобразует значение в целое число и проверяет, что оно больше нуля.

    Parameters
    ----------
    val : int, float, str
        Значение, которое требуется преобразовать в целое число;
    field_name : str
        Название поля для сообщения об ошибке;
    call_raise : bool, optional
        Флаг, определяющий, следует ли возбуждать исключение в случае ошибки. По умолчанию False.

    Returns
    -------
    int or None
        Преобразованное целое число больше нуля, или None, если преобразование невозможно или число меньше нуля.

    Raises
    ------
    AppException
        Если преобразование не удалось или число меньше нуля и call_raise=True.
    """
    val = get_int(val, field_name, call_raise)
    if val is not None and val < 0:
        if call_raise:
            raise AppException(
                "Ошибка ввода",
                f"""Введите положительное число в поле "{field_name!r}".""",
            )
        return None
    return val


# ---------------------------------------------------------------------------
#   С плавающей точкой
# ---------------------------------------------------------------------------
def get_float(val: int | float | str, field_name: str, call_raise: bool = CALL_EXCEPTION_DEFAULT) -> float | None:
    """
    Преобразует значение в число с плавающей точкой.

    Parameters
    ----------
    val : int, float, str
        Значение, которое требуется преобразовать в число с плавающей точкой.
    field_name : str
        Название поля для сообщения об ошибке.
    call_raise : bool, optional
        Флаг, определяющий, следует ли возбуждать исключение в случае ошибки. По умолчанию False.

    Returns
    -------
    float or None
        Преобразованное число с плавающей точкой, или None, если преобразование невозможно и call_raise=False.

    Raises
    ------
    AppException
        Если преобразование не удалось и call_raise=True.
    """
    try:
        val = float(val)
    except ValueError:
        if call_raise:
            raise AppException("Ошибка ввода", f"""Введите число в поле "{field_name!r}".""")
        return None
    return val


def get_float_and_positive(
    val: int | float | str, field_name: str, call_raise: bool = CALL_EXCEPTION_DEFAULT
) -> float | None:
    """
    Преобразует значение в число с плавающей точкой и проверяет, что оно больше нуля.

    Parameters
    ----------
    val : int, float, str
        Значение, которое требуется преобразовать в число с плавающей точкой;
    field_name : str
        Название поля для сообщения об ошибке;
    call_raise : bool, optional
        Флаг, определяющий, следует ли возбуждать исключение в случае ошибки. По умолчанию False.

    Returns
    -------
    float or None
        Преобразованное число с плавающей точкой больше нуля, или None, если преобразование невозможно или число меньше нуля.

    Raises
    ------
    AppException
        Если преобразование не удалось или число меньше нуля и call_raise=True.
    """
    val = get_float(val, field_name, call_raise)
    if val is not None and val < 0:
        if call_raise:
            raise AppException(
                "Ошибка ввода",
                f"""Введите положительное число в поле "{field_name!r}".""",
            )
        return None
    return val
