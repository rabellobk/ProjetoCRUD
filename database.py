# Responsavel por conectar ao SQlite e executar operações CRUD simples.

import sqlite3
from typing import Optional, List, Tuple

DB_PATH = "cadatro.db"

def get_connection() -> sqlite3.Connection:
