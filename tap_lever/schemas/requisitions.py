from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("requisitionCode", th.StringType),
    th.Property("name", th.StringType),
    th.Property("backfill", th.BooleanType),
    th.Property("createdAt", th.StringType),
    th.Property("creator", th.StringType),
    th.Property("headcountHired", th.IntegerType),
    th.Property("headcountTotal", th.StringType),
    th.Property("status", th.StringType),
    th.Property("hiringManager", th.StringType),
    th.Property("owner", th.StringType),
    th.Property("compensationBand", th.StringType),
    th.Property("employmentStatus", th.StringType),
    th.Property("location", th.StringType),
    th.Property("internalNotes", th.StringType),
    th.Property("postings", th.ArrayType(th.StringType)),
    th.Property("department", th.StringType),
    th.Property("team", th.StringType),
    th.Property("offerIds", th.ArrayType(th.StringType)),
    th.Property("customFields", th.StringType),
).to_dict()
