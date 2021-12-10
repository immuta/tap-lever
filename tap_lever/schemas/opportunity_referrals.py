from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("type", th.StringType),
    th.Property("text", th.StringType),
    th.Property("instructions", th.StringType),
    th.Property(
        "fields",
        th.ArrayType(
            th.ObjectType(
                th.Property("type", th.StringType),
                th.Property("text", th.StringType),
                th.Property("description", th.StringType),
                th.Property("required", th.BooleanType),
                th.Property("value", th.StringType),
                th.Property("prompt", th.StringType),
                th.Property(
                    "options",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("text", th.StringType),
                        )
                    ),
                ),
            )
        ),
    ),
    th.Property("baseTemplateId", th.StringType),
    th.Property("user", th.StringType),
    th.Property("referrer", th.StringType),
    th.Property("stage", th.StringType),
    th.Property("createdAt", th.StringType),
    th.Property("completedAt", th.StringType),
).to_dict()
