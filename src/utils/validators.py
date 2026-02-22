import logging
from datetime import date

def validate_is_integer(value: int) -> None:
    """
    Valida se o valor é um número inteiro e maior que 0
    Args:
        value: int: Valor a ser validado
    Returns:
        None
    """
    if not isinstance(value, int):
        logging.warning("Valor deve ser um número inteiro")
        raise ValueError("Valor deve ser um número inteiro")
    if value <= 0:
        logging.warning("Valor deve ser maior que 0")
        raise ValueError("Valor deve ser maior que 0")
    
def validate_filled_string(value: str) -> None:
    """
    Valida se o valor é uma string não vazia e não contém espaços
    Args:
        value: str: Valor a ser validado
    Returns:
        None
    """
    if not value or value.isspace():
        logging.warning("Valor invalido")
        raise ValueError("Valor invalido")

def validate_email(email: str) -> None:
    """
    Valida o email do cliente
    Args:
        email: str: Email do cliente a ser validado
    Returns:
        None
    """
    if not email or email.isspace() or "@" not in email:
        logging.warning("Email invalido")
        raise ValueError("Email invalido")

def validate_phone(phone: str) -> None:
    """
    Valida o telefone do cliente
    Args:
        phone: str: Telefone do cliente a ser validado
    Returns:
        None
    """
    if not phone or phone.isspace() or len(phone) != 15:
        logging.warning("Telefone invalido")
        raise ValueError("Telefone invalido")

def validate_birth_date(birth_date: date) -> None:
    """
    Valida a data de nascimento do cliente
    Args:
        birth_date: date: Data de nascimento do cliente a ser validada
    Returns:
        None
    """
    if not birth_date or birth_date > date.today() or birth_date < date(1900, 1, 1):
        logging.warning("Data de nascimento invalido")
        raise ValueError("Data de nascimento invalido")
