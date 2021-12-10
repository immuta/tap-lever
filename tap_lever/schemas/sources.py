from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("text", th.StringType),
    th.Property("count", th.IntegerType),
).to_dict()
