from datetime import datetime

def convert_to_us_date(date_str: str) -> str:
    """
    Converte data do formato DD/MM/YYYY para YYYY-MM-DD
    """
    date_obj = datetime.strptime(date_str, "%d/%m/%Y")
    return date_obj.strftime("%Y-%m-%d")

def convert_to_br_date(date_str: str) -> str:
    """
    Converte data do formato YYYY-MM-DD para DD/MM/YYYY
    """
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%d/%m/%Y")

def format_phone_br(phone: str) -> str:
    """
    Formata telefone brasileiro no padrão:
    +55 11 90000-0010
    Aceita número com ou sem código do país e com caracteres especiais.
    """

    digits = "".join(c for c in phone if c.isdigit())

    # Se vier sem código do país, adiciona
    if len(digits) == 11:
        digits = "55" + digits

    if len(digits) != 13:
        raise ValueError("Telefone deve conter 11 dígitos (DDD+número) ou 13 com código do país")

    country = digits[:2]
    ddd = digits[2:4]
    first_part = digits[4:9]
    second_part = digits[9:]

    return f"+{country} {ddd} {first_part}-{second_part}"