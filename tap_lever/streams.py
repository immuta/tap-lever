"""Stream type classes for tap-lever."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_lever.client import LeverStream
from tap_lever import schemas


class ArchiveReasonsStream(LeverStream):
    """Archive reasons provide granularity behind to candidates who have exited your active hiring pipeline. Candidates exit your active pipeline either due to being hired at your company or due to being rejected for a specific reason. These dispositions allows you to track each and every candidate who is no longer active within your pipeline."""
    name = "archive_reasons"
    path = "/archive_reasons"
    primary_keys = ["id"]
    replication_key = None
    schema = schemas.archive_reasons


class OpportunitiesStream(LeverStream):
    """
    "Candidates" are individuals who have been added to your Lever account as potential fits for your open job positions. "Opportunities" represent each of an individual’s unique candidacies or journeys through your pipeline for a given job position, meaning a single Candidate can be associated to multiple Opportunities. A “Contact” is a unique individual who may or may not have multiple candidacies or Opportunities.

    Candidates enter your pipeline for a new Opportunity by:

    Applying to a posting on your jobs site,
    Being added by an external recruiting agency,
    Being referred by an employee,
    Being manually added by a Lever user, or
    Being sourced from an online profile.
    Each Opportunity can have their own notes, feedback, interview schedules, and additional forms. An opportunity may be “confidential” if it is moving through your pipeline for a job posting that has been created as confidential. Opportunities exit your pipeline by being archived for one of two reasons: (1) The candidate was rejected for the opportunity, or (2) The candidate was hired for the opportunity.

    A "Contact" is an object that our application uses internally to identify an individual person and their personal or contact information, even though they may have multiple opportunities. From this API, the "Contact" is exposed via the contact field, which returns the unique ID for a Contact across your account. Contact information will be shared and consistent across an individual person's opportunities, and will continue to be aggregated onto individual opportunities in the responses to all GET and POST requests to /opportunities.
    """
    name = "opportunities"
    path = "/opportunities"
    primary_keys = ["id"]
    replication_key = "updatedAt"
    schema = schemas.opportunities

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        context = {"opportunity_id": record["id"]}
        return context


class PostingsStream(LeverStream):
    """
    Job postings organize candidates based on the specific roles that they may fit into on your growing team. There are four different states of job postings: published, internal, closed, and draft. NOTE: In the Lever app, we refer to internal postings as “unlisted” postings. For organizations that have enabled job posting approvals, there are two additional states: pending and rejected.
    """
    name = "postings"
    path = "/postings"
    primary_keys = ["id"]
    replication_key = None
    schema = schemas.postings


class OpportunityApplicationsStream(LeverStream):
    """
    When a candidate applies to a job posting, an application is created.

    Lever is candidate-centric, meaning that candidates can exist in the system without being applied to a specific job posting. However, almost all candidates are applied to job postings, and thus almost all candidates have one or more applications.

    There are three different ways that applications can be created in Lever:

    Through a posting: An application is created when a candidate applies to a job posting through your company's public or internal job site, or is submitted by an agency.
    By a user: A team member at your company manually adds a job posting to a specific candidate in Lever.
    As a referral: A team member at your company refers the candidate into Lever for a specific job posting.
    Candidates can be applied to multiple job postings, meaning that candidates can have multiple applications. A candidate or contact may have multiple applications, each of which will be on a unique Opportunity. An Opportunity will have no more than one Application.    """
    name = "opportunity_applications"
    path = "/opportunities/{opportunity_id}/applications"
    primary_keys = ["id"]
    parent_stream_type = OpportunitiesStream
    ignore_parent_replication_keys = False
    schema = schemas.opportunity_applications


class OpportunityOffersStream(LeverStream):
    """
    Offers capture the data sent to a candidate about an Opportunity for a position they have been offered sent using Lever's offers feature. The status, creation date, creator, sent document, signed document, and all fields of an offer are exposed by the api.
    """
    name = "opportunity_offers"
    path = "/opportunities/{opportunity_id}/offers"
    primary_keys = ["id"]
    parent_stream_type = OpportunitiesStream
    ignore_parent_replication_keys = False
    schema = schemas.opportunity_offers


class OpportunityReferralsStream(LeverStream):
    """
    Referrals can be created by filling out a referral form[?]. Alternatively, if a candidate is created without a referral[?], the referral information can be added manually[?].
    """
    name = "opportunity_referrals"
    path = "/opportunities/{opportunity_id}/referrals"
    primary_keys = ["id"]
    parent_stream_type = OpportunitiesStream
    ignore_parent_replication_keys = False
    schema = schemas.opportunity_referrals

class OpportunityResumesStream(LeverStream):
    """
    Offers capture the data sent to a candidate about an Opportunity for a position they have been offered sent using Lever's offers feature. The status, creation date, creator, sent document, signed document, and all fields of an offer are exposed by the api.
    """
    name = "opportunity_resumes"
    path = "/opportunities/{opportunity_id}/resumes"
    primary_keys = ["id"]
    parent_stream_type = OpportunitiesStream
    ignore_parent_replication_keys = False
    schema = schemas.opportunity_resumes


class SourcesStream(LeverStream):
    """
    A source is the way that a candidate entered into your Lever account. The most common sources in your Lever account are:

    Posting - Candidate applied to a posting on your careers page.
    Referral - Candidate was referred by an employee at your company.
    Add New - Candidate was added manually into your Lever account in the app.
    Email Applicant - Candidate was added via applicant@hire.lever.co email address.
    Email Lead - Candidate was added via lead@hire.lever.co email address.
    LinkedIn - Candidate was added from LinkedIn using the Lever Chrome Extension.
    GitHub - Candidate was added from GitHub using the Lever Chrome Extension.
    AngelList - Candidate was added from AngelList using the Lever Chrome Extension.
    """
    name = "sources"
    path = "/sources"
    primary_keys = ["id"]
    replication_key = None
    schema = schemas.sources

class StagesStream(LeverStream):
    """Stages are steps in the recruiting workflow of your hiring pipeline. All candidates belong to a stage and change stages as they progress through the recruiting pipeline, typically in a linear fashion."""

    name = "stages"
    path = "/stages"
    primary_keys = ["id"]
    replication_key = None
    schema = schemas.stages

class UsersStream(LeverStream):
    """Users in Lever include anyone who has been invited to join in on recruiting efforts. There are five different access roles in Lever. From most to least access, these roles are Super admin, Admin, Team member, Limited team member, and Interviewer."""

    name = "users"
    path = "/users"
    primary_keys = ["id"]
    replication_key = None
    schema = schemas.users
