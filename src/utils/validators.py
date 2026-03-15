import logging
from datetime import date
from re import match
from string import digits
from src.utils.formatters import convert_to_us_date

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
        raise ValueError("Valor deve ser um número")
    if value <= 0:
        logging.warning("Valor deve ser maior que 0")
        raise ValueError("Valor deve ser maior que 0")
    
def validate_filled_string(value: str, message: str) -> None:
    """
    Valida se o valor é uma string não vazia e não contém espaços
    Args:
        value: str: Valor a ser validado
    Returns:
        None
    """
    if not value or value.isspace():
        logging.warning(message)
        raise ValueError(message.upper)

def validate_email(email: str) -> None:
    """
    Valida o email do cliente
    Args:
        email: str: Email do cliente a ser validado
    Returns:
        None
    """
    validate_filled_string(email, "Email deve ser preenchido")
    
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not match(pattern, email):
        logging.warning("Email inválido")
        raise ValueError("Email inválido")

def validate_phone(phone: str) -> None:
    """
    Valida o telefone do cliente

    Args:
        phone: str: Telefone do cliente a ser validado
    Returns:
        None
    """
    validate_filled_string(phone, "Telefone deve ser preenchido")
    
    if phone.startswith("+"):
        digits = phone[1:]
    else:
        digits = phone

    if not all([c.isdigit() for c in digits]):
        logging.warning("Telefone deve conter apenas números (ou + no início)")
        raise ValueError("Telefone deve conter apenas números (ou + no início)")

def validate_birth_date(birth_date: str) -> None:
    """
    Valida a data de nascimento do cliente

    Args:
        birth_date: date: Data de nascimento do cliente a ser validada
    Returns:
        None
    """

    if birth_date > date.today() or birth_date < date(1900, 1, 1):
        logging.warning("Data de nascimento invalido")
        raise ValueError("Data de nascimento invalido")

def validate_date_format(date_str: str) -> None:
    """
    Valida se a data está no formato DD/MM/YYYY
    
    Args:
        date_str: str: Data a ser validada
    Returns:
        None
    """
    validate_filled_string(date_str, "Data deve ser preenchida")

    pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    
    if not match(pattern, date_str):
        logging.warning("Data inválida, use o formato DD/MM/YYYY")
        raise ValueError("Data inválida, use o formato DD/MM/YYYY")