from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
    th.Property("username", th.StringType),
    th.Property("email", th.StringType),
    th.Property("createdAt", th.StringType),
    th.Property("deactivatedAt", th.StringType),
    th.Property("accessRole", th.StringType),
    th.Property("photo", th.StringType),
    th.Property("externalDirectoryId", th.StringType),
).to_dict()
