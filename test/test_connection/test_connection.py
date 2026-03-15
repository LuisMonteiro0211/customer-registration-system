import pytest
from src.database.connection import get_connection

def test_get_connection():
    connection = get_connection()
    assert connection is not None