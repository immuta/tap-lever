"""Stream type classes for tap-lever."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_lever.client import LeverStream
from tap_lever import schemas


class UsersStream(LeverStream):
    """Define custom stream."""

    name = "users"
    description = "Users in Lever include anyone who has been invited to join in on recruiting efforts. There are five different access roles in Lever. From most to least access, these roles are Super admin, Admin, Team member, Limited team member, and Interviewer."
    path = "/users"
    primary_keys = ["id"]
    replication_key = None
    schema = schemas.users
