"""REST client handling, including LeverStream base class."""

from datetime import datetime
from dateutil import parser
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from memoization import cached

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream
from singer_sdk.authenticators import BasicAuthenticator


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class LeverStream(RESTStream):
    """Lever stream class."""

    url_base = "https://api.lever.co/v1"
    records_jsonpath = "$.data[*]"
    next_page_token_jsonpath = "$.next"

    @property
    def authenticator(self) -> BasicAuthenticator:
        """Return a new authenticator object."""
        return BasicAuthenticator.create_for_stream(
            self, username=self.config["api_key"], password=""
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {"Content-Type": "application/json"}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        return headers

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params = {"limit": 100}
        if next_page_token:
            params["offset"] = next_page_token
        if self.replication_key:
            start_value = self.get_starting_replication_key_value(context)
            params[f"updated_at_start"] = self._try_timestamp_to_epoch(start_value)
        return params

    def _try_timestamp_to_epoch(self, ts_value):
        "Converts to 13-digit epoch with milliseconds."
        try:
            parsed = parser.parse(ts_value)
            return parsed.strftime("%s%f")[:-3]
        except parser.ParserError:
            return ts_value
