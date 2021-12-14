from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("opportunity_id", th.StringType),
    th.Property("opportunityId", th.StringType),
    th.Property("id", th.StringType),
    th.Property("candidateId", th.StringType),
    th.Property("type", th.StringType),
    th.Property("posting", th.StringType),
    th.Property("user", th.StringType),
    th.Property("name", th.StringType),
    th.Property("email", th.StringType),
    th.Property("createdAt", th.NumberType),
    th.Property("phone", th.ObjectType()),
    th.Property("company", th.StringType),
    th.Property("links", th.ArrayType(th.StringType)),
    th.Property("comments", th.StringType),
    th.Property("resume", th.StringType),
    th.Property("customQuestions", th.ArrayType(th.ObjectType())),
    th.Property("archived", th.ObjectType()),
    th.Property("postingHiringManager", th.StringType),
    th.Property("postingOwner", th.StringType),
    th.Property("requisitionForHire", th.StringType),
).to_dict()
