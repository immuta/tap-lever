from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("text", th.StringType),
    th.Property("createdAt", th.StringType),
    th.Property("updatedAt", th.StringType),
    th.Property("user", th.StringType),
    th.Property("owner", th.StringType),
    th.Property("hiringManager", th.StringType),
    th.Property("categories", th.ObjectType(
        th.Property("team", th.StringType),
        th.Property("department", th.StringType),
        th.Property("location", th.StringType),
        th.Property("commitment", th.StringType),
        th.Property("level", th.StringType),
    )),
    th.Property("content", th.ObjectType(
        th.Property("description", th.StringType),
        th.Property("lists", th.ArrayType(
            th.ObjectType(
                th.Property("text", th.StringType),
                th.Property("content", th.StringType),
            )),
        ),
        th.Property("closing", th.StringType),
        th.Property("customQuestions", th.ArrayType(th.StringType)),
    )),
    th.Property("tags", th.ArrayType(th.StringType)),
    th.Property("followers", th.StringType),
    th.Property("state", th.StringType),
    th.Property("distributionChannels", th.ArrayType(th.StringType)),
    th.Property("reqCode", th.StringType),
    th.Property("urls", th.ObjectType(
        th.Property("list", th.StringType),
        th.Property("show", th.StringType),
        th.Property("apply", th.StringType),
    )),
).to_dict()
