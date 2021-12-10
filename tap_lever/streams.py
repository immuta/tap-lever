"""Stream type classes for tap-lever."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_lever.client import LeverStream
from tap_lever import schemas


class UsersStream(LeverStream):
    """Define custom stream."""
    name = "users"
    path = "/users"
    primary_keys = ["id"]
    replication_key = None
    schema = schemas.users
