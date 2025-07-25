import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field


class ContentType(str, Enum):
    """Enumeration for the supported types of content."""

    TEXT = "text"
    IMAGE_URI = "image_uri"
    VIDEO_URI = "video_uri"
    AUDIO_URI = "audio_uri"
    FILE_URI = "file_uri"


class ContentLink(BaseModel):
    """Represents a single piece of content within a turn."""

    content_type: ContentType = Field(
        ..., description="The type of content this part represents."
    )
    payload: str = Field(
        ...,
        description="The content itself (if text) or a URI pointer to the content (if a file).",
    )


class Turn(BaseModel):
    """Represents a single turn in a conversation."""

    turn_id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="A unique identifier for this specific turn.",
    )
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="The UTC timestamp when the turn was recorded.",
    )
    actor_id: str = Field(
        ...,
        description="The unique identifier of the actor (user or system) who generated the text for this turn.",
    )
    content: List[ContentPart] = Field(
        ..., description="A list of content parts that make up this turn."
    )
    reply_to_turn_id: Optional[str] = Field(
        None,
        description="ID of the turn this turn is replying to, if any, to extend or continue in a branch.",
    )


class BranchSummary(BaseModel):
    """A validated, strucured summary of part of a conversation."""

    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="The UTC timestamp when the summary was recorded.",
    )
    summary_text: str = Field(
        ..., description="A concise summary of a series of turns."
    )


class Branch(BaseModel):
    """Represents a single 'branch' of a conversation."""

    branch_id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="A unique identifier for this branch of conversation.",
    )
    summaries: List[BranchSummary] = Field(
        default_factory=list,
        description="A chronological list of all summaries created for this branch.",
    )
    verbatim_turns: List[Turn] = Field(
        default_factory=list, description="Most recent turns in a branch."
    )
    forked_from_branch_id: Optional[str] = Field(
        None, description="ID of the branch this branch was forked from, if any."
    )
    forked_from_turn_id: Optional[str] = Field(
        None,
        description="The turn within the parent branch that this branch was forked from, if any.",
    )


class Session(BaseModel):
    """The main object, representing an entire session history."""

    session_id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="A unique identifier for this session.",
    )
    active_branch_id: Optional[str] = Field(
        None,
        description="ID of the currently active branch. None if no branches exist or none are active.",
    )
    branch_ids: List[str] = Field(
        default_factory=list,
        description="The list of all IDs for branches that have been created within this session.",
    )


class ContextRequest(BaseModel):
    """Defines the schema for requesting a custom context window from the API."""

    request_id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="A unique ID for this specific context request, generated by the client.",
    )
    branch_ids: List[str] = Field(
        ..., description="A list of branch IDs to pull context from."
    )


class ContextResponse(BaseModel):
    """Defines the structure of the completed context window returned by the service"""

    request_id: str = Field(
        ..., description="The unique ID of the request this response corresponds to."
    )
    retrieved_summaries: List[BranchSummary] = Field(
        ...,
        description="An ordered list of all summaries retrieved from the requested branches.",
    )
    retrieved_turns: List[Turn] = Field(
        ...,
        description="An ordered list of all verbatim turns retrieved from the requested branches.",
    )
