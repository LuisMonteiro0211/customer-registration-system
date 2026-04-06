import logging
from datetime import date
from re import match
from string import digits
from src.utils.formatters import convert_to_us_date

def validate_is_integer(value: int) -> None:
    """
    Valida se o valor é um número inteiro e maior que 0
    
    Args:
        value: int - Valor a ser validado
        
    Raises:
        ValueError: Se o valor não for inteiro ou menor/igual a 0
    """
    if not isinstance(value, int):
        logging.warning("Valor deve ser um número inteiro")
        raise ValueError("Valor deve ser um número")
    if value <= 0:
        logging.warning("Valor deve ser maior que 0")
        raise ValueError("Valor deve ser maior que 0")
    
def validate_filled_string(value: str, message: str) -> None:
    """
    Valida se o valor é uma string não vazia e não contém somente espaços
    
    Args:
        value: str - Valor a ser validado
        message: str - Mensagem de erro customizada
        
    Raises:
        ValueError: Se a string estiver vazia ou contiver apenas espaços
    """
    if not value or value.isspace():
        logging.warning(message)
        raise ValueError(message.upper())

def validate_email(email: str) -> None:
    """
    Valida o formato do email
    
    Args:
        email: str - Email a ser validado
        
    Raises:
        ValueError: Se o email estiver vazio ou em formato inválido
    """
    validate_filled_string(email, "Email deve ser preenchido")
    
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not match(pattern, email):
        logging.warning("Email inválido")
        raise ValueError("Email inválido")

def validate_phone(phone: str) -> None:
    """
    Valida o formato do telefone
    
    Args:
        phone: str - Telefone a ser validado (até 11 dígitos, pode começar com +)
        
    Raises:
        ValueError: Se o telefone estiver vazio, inválido ou com mais de 11 dígitos
    """
    validate_filled_string(phone, "Telefone deve ser preenchido")
    
    if phone.startswith("+"):
        digits = phone[1:]
    else:
        digits = phone

    if len(digits) > 11:
        logging.warning("Telefone deve conter até 11 dígitos")
        raise ValueError("Telefone deve conter até 11 dígitos")

    if not all([c.isdigit() for c in digits]):
        logging.warning("Telefone deve conter apenas números (ou + no início)")
        raise ValueError("Telefone deve conter apenas números (ou + no início)")

def validate_birth_date(birth_date: str) -> None:
    """
    Valida a data de nascimento
    
    Args:
        birth_date: date - Data de nascimento a ser validada
        
    Raises:
        ValueError: Se a data for futura ou anterior a 1900
    """

    if birth_date > date.today() or birth_date < date(1900, 1, 1):
        logging.warning("Data de nascimento inválida")
        raise ValueError("Data de nascimento inválida")

def validate_date_format(date_str: str) -> None:
    """
    Valida se a data está no formato DD/MM/YYYY
    
    Args:
        date_str: str - Data a ser validada
        
    Raises:
        ValueError: Se a data não estiver no formato DD/MM/YYYY
    """
    validate_filled_string(date_str, "Data deve ser preenchida")

    pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    
    if not match(pattern, date_str):
        logging.warning("Data inválida, use o formato DD/MM/YYYY")
        raise ValueError("Data inválida, use o formato DD/MM/YYYY")