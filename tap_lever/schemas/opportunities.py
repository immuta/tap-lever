from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
    th.Property("headline", th.StringType),
    th.Property("contact", th.StringType),
    th.Property("stage", th.StringType),
    th.Property("stageChanges", th.ArrayType(th.StringType)),
    th.Property("location", th.StringType),
    th.Property("phones", th.ArrayType(
        th.ObjectType(
            th.Property("value", th.StringType),
            th.Property("type", th.StringType),
        )),
    ),
    th.Property("emails", th.ArrayType(th.StringType)),
    th.Property("links", th.ArrayType(th.StringType)),
    th.Property("archived", th.ObjectType(
        th.Property("archivedAt", th.StringType),
        th.Property("reason", th.StringType),
    )),
    th.Property("tags", th.ArrayType(th.StringType)),
    th.Property("sources", th.ArrayType(th.StringType)),
    th.Property("origin", th.StringType),
    th.Property("owner", th.StringType),
    th.Property("followers", th.ArrayType(th.StringType)),
    th.Property("applications", th.ArrayType(th.StringType)),
    th.Property("createdAt", th.StringType),
    th.Property("lastInteractionAt", th.StringType),
    th.Property("lastAdvancedAt", th.StringType),
    th.Property("snoozedUntil", th.StringType),
    th.Property("urls", th.ObjectType()),
    th.Property("dataProtection", th.ObjectType()),
    th.Property("isAnonymized", th.BooleanType),
).to_dict()
