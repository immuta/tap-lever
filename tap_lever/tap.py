"""Lever tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_lever.streams import (
    ArchiveReasonsStream,
    OpportunitiesStream,
    OpportunityApplicationsStream,
    OpportunityOffersStream,
    OpportunityReferralsStream,
    OpportunityResumesStream,
    PostingsStream,
    SourcesStream,
    StagesStream,
    UsersStream,
)

STREAM_TYPES = [
    ArchiveReasonsStream,
    OpportunitiesStream,
    OpportunityApplicationsStream,
    OpportunityOffersStream,
    OpportunityReferralsStream,
    OpportunityResumesStream,
    PostingsStream,
    SourcesStream,
    StagesStream,
    UsersStream,
]


class TapLever(Tap):
    """Lever tap class."""

    name = "tap-lever"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
