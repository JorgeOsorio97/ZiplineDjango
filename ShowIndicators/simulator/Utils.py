from enum import Enum, auto


class FirstTransactionType(Enum):
    """
    Enum que define como se hara la primer practica
    """
    STOCK_QUANTITY = auto()
    INIT_CAPITAL = auto()

class TransactionType(Enum):
    """
    Enum para tipo de transaccion
    """
    BUY = auto()
    SELL = auto()