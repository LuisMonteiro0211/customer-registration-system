import logging
from datetime import date

def validate_id(id: int) -> None:
    """
    Valida o ID do cliente
    Args:
        id: int: ID do cliente a ser validado
    Returns:
        None
    """
    if not isinstance(id, int):
        logging.warning("ID deve ser um número inteiro")
        raise ValueError("ID deve ser um número inteiro")
    if id <= 0:
        logging.warning("ID deve ser maior que 0")
        raise ValueError("ID deve ser maior que 0")
    
def validate_name(name: str) -> None:
    """
    Valida o nome do cliente
    Args:
        name: str: Nome do cliente a ser validado
    Returns:
        None
    """
    if not name or name.isspace():
        logging.warning("Nome invalido")
        raise ValueError("Nome invalido")

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