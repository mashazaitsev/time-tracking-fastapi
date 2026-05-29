"""
Purpose: Define all SQLModel database tables and Pydantic API schemas for User, Item, Project, TimeEntry, and VacationRequest entities

Structure:
    User (table): entity - User account with auth and profile data
    Item (table): entity - User-owned content item
    Project (table): entity - Named grouping for time entries, owned by a User
    TimeEntry (table): entity - Time record against a Project, owned by a User
    VacationRequest (table): entity - Vacation request owned by a User
    UserBase, UserCreate, UserUpdate, UserRegister, UserUpdateMe, UpdatePassword: schema - User API schemas
    UserPublic, UsersPublic: schema - User response schemas
    ItemBase, ItemCreate, ItemUpdate: schema - Item API schemas
    ItemPublic, ItemsPublic: schema - Item response schemas
    ProjectBase, ProjectCreate, ProjectUpdate: schema - Project API schemas
    ProjectPublic, ProjectsPublic: schema - Project response schemas
    TimeEntryBase, TimeEntryCreate, TimeEntryUpdate: schema - TimeEntry API schemas
    TimeEntryPublic, TimeEntriesPublic: schema - TimeEntry response schemas
    VacationRequestBase, VacationRequestCreate, VacationRequestUpdate: schema - VacationRequest API schemas
    VacationRequestPublic, VacationRequestsPublic: schema - VacationRequest response schemas
    ProjectSummary, TimeSummary: schema - Aggregated time summary response schemas
    Token, TokenPayload, NewPassword, Message: schema - Auth and utility schemas

Relationships:
    Produces: user table, item table, project table, timeentry table, vacationrequest table
    Consumes: (consumed by) api.routes, crud, core.db

Semantics:
    Domain: identity, content, time-tracking, vacation-management
    Entity: User, Item, Project, TimeEntry, VacationRequest
    Logic: [Items cascade-delete with owner, Projects cascade-delete with owner, TimeEntries cascade-delete with project and owner, VacationRequests cascade-delete with owner, UUIDs as primary keys, created_at auto-set to UTC]

Important:
    All SQLModel table classes MUST be imported before Alembic or init_db runs,
    otherwise relationships fail to initialize. See core/db.py comment.
"""

import uuid
import datetime as dt
from datetime import datetime, timezone
from typing import Optional

from pydantic import EmailStr, model_validator
from sqlalchemy import DateTime
from sqlmodel import Field, Relationship, SQLModel


def get_datetime_utc() -> datetime:
    """Purpose: Return current UTC datetime for default timestamps"""
    return datetime.now(timezone.utc)


class UserBase(SQLModel):
    """Purpose: Shared user fields for all user schemas"""
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = Field(default=None, max_length=255)


class UserCreate(UserBase):
    """Purpose: Schema for admin user creation (includes role flags from UserBase)"""
    password: str = Field(min_length=8, max_length=128)


class UserRegister(SQLModel):
    """Purpose: Schema for public self-registration (no role flags)"""
    email: EmailStr = Field(max_length=255)
    password: str = Field(min_length=8, max_length=128)
    full_name: str | None = Field(default=None, max_length=255)


class UserUpdate(UserBase):
    """Purpose: Schema for admin user update (all fields optional)"""
    email: EmailStr | None = Field(default=None, max_length=255)  # type: ignore
    password: str | None = Field(default=None, min_length=8, max_length=128)


class UserUpdateMe(SQLModel):
    """Purpose: Schema for self-profile update (name and email only)"""
    full_name: str | None = Field(default=None, max_length=255)
    email: EmailStr | None = Field(default=None, max_length=255)


class UpdatePassword(SQLModel):
    """Purpose: Schema for authenticated password change"""
    current_password: str = Field(min_length=8, max_length=128)
    new_password: str = Field(min_length=8, max_length=128)


class User(UserBase, table=True):
    """Purpose: User database table with auth credentials and owned items, projects, and time entries"""
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str
    created_at: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),  # type: ignore
    )
    items: list["Item"] = Relationship(back_populates="owner", cascade_delete=True)
    projects: list["Project"] = Relationship(back_populates="owner", cascade_delete=True)
    time_entries: list["TimeEntry"] = Relationship(back_populates="owner", cascade_delete=True)
    vacation_requests: list["VacationRequest"] = Relationship(back_populates="owner", cascade_delete=True)


class UserPublic(UserBase):
    """Purpose: User response schema (excludes hashed_password)"""
    id: uuid.UUID
    created_at: datetime | None = None


class UsersPublic(SQLModel):
    """Purpose: Paginated user list response"""
    data: list[UserPublic]
    count: int


class ItemBase(SQLModel):
    """Purpose: Shared item fields for all item schemas"""
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)


class ItemCreate(ItemBase):
    """Purpose: Schema for item creation"""
    pass


class ItemUpdate(ItemBase):
    """Purpose: Schema for item update (all fields optional)"""
    title: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore


class Item(ItemBase, table=True):
    """Purpose: Item database table owned by a User (cascade-deletes with owner)"""
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),  # type: ignore
    )
    owner_id: uuid.UUID = Field(
        foreign_key="user.id", nullable=False, ondelete="CASCADE"
    )
    owner: User | None = Relationship(back_populates="items")


class ItemPublic(ItemBase):
    """Purpose: Item response schema with owner reference"""
    id: uuid.UUID
    owner_id: uuid.UUID
    created_at: datetime | None = None


class ItemsPublic(SQLModel):
    """Purpose: Paginated item list response"""
    data: list[ItemPublic]
    count: int


class Message(SQLModel):
    """Purpose: Generic API message response"""
    message: str


class Token(SQLModel):
    """Purpose: JWT access token response"""
    access_token: str
    token_type: str = "bearer"


class TokenPayload(SQLModel):
    """Purpose: Decoded JWT token payload (sub = user ID)"""
    sub: str | None = None


class NewPassword(SQLModel):
    """Purpose: Schema for token-based password reset"""
    token: str
    new_password: str = Field(min_length=8, max_length=128)


# ---------------------------------------------------------------------------
# Project schemas and table
# ---------------------------------------------------------------------------


class ProjectBase(SQLModel):
    """Purpose: Shared project fields for all project schemas"""
    name: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)


class ProjectCreate(ProjectBase):
    """Purpose: Schema for project creation"""
    pass


class ProjectUpdate(ProjectBase):
    """Purpose: Schema for project update (all fields optional)"""
    name: str | None = Field(default=None, min_length=1, max_length=255)  # type: ignore


class Project(ProjectBase, table=True):
    """Purpose: Project database table owned by a User; cascade-deletes time entries

    Relationships:
        Consumes: user.id (FK owner_id)
        Produces: project table; back-populates User.projects and TimeEntry.project
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),  # type: ignore
    )
    owner_id: uuid.UUID = Field(
        foreign_key="user.id", nullable=False, ondelete="CASCADE"
    )
    owner: User | None = Relationship(back_populates="projects")
    time_entries: list["TimeEntry"] = Relationship(
        back_populates="project", cascade_delete=True
    )


class ProjectPublic(ProjectBase):
    """Purpose: Project response schema with owner reference"""
    id: uuid.UUID
    owner_id: uuid.UUID
    created_at: datetime | None = None


class ProjectsPublic(SQLModel):
    """Purpose: Paginated project list response"""
    data: list[ProjectPublic]
    count: int


# ---------------------------------------------------------------------------
# TimeEntry schemas and table
# ---------------------------------------------------------------------------


class TimeEntryBase(SQLModel):
    """Purpose: Shared time entry fields for all time entry schemas"""
    project_id: uuid.UUID
    date: dt.date
    duration_minutes: int = Field(ge=1)
    description: str | None = Field(default=None, max_length=255)


class TimeEntryCreate(TimeEntryBase):
    """Purpose: Schema for time entry creation"""
    pass


class TimeEntryUpdate(SQLModel):
    """Purpose: Schema for time entry update (all fields optional)"""
    project_id: uuid.UUID | None = None
    date: Optional[dt.date] = None
    duration_minutes: int | None = Field(default=None, ge=1)
    description: str | None = Field(default=None, max_length=255)


class TimeEntry(TimeEntryBase, table=True):
    """Purpose: TimeEntry database table owned by a User and associated with a Project

    Relationships:
        Consumes: user.id (FK owner_id), project.id (FK project_id)
        Produces: timeentry table; back-populates User.time_entries and Project.time_entries
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),  # type: ignore
    )
    owner_id: uuid.UUID = Field(
        foreign_key="user.id", nullable=False, ondelete="CASCADE"
    )
    project_id: uuid.UUID = Field(
        foreign_key="project.id", nullable=False, ondelete="CASCADE"
    )
    owner: User | None = Relationship(back_populates="time_entries")
    project: Project | None = Relationship(back_populates="time_entries")


class TimeEntryPublic(TimeEntryBase):
    """Purpose: TimeEntry response schema with owner reference"""
    id: uuid.UUID
    owner_id: uuid.UUID
    created_at: datetime | None = None


class TimeEntriesPublic(SQLModel):
    """Purpose: Paginated time entry list response"""
    data: list[TimeEntryPublic]
    count: int


# ---------------------------------------------------------------------------
# Summary response schemas (no table)
# ---------------------------------------------------------------------------


class ProjectSummary(SQLModel):
    """Purpose: Per-project aggregated time summary"""
    project_id: uuid.UUID
    project_name: str
    total_minutes: int


class TimeSummary(SQLModel):
    """Purpose: Aggregated time summary across all projects for a user"""
    total_minutes: int
    by_project: list[ProjectSummary]


# ---------------------------------------------------------------------------
# VacationRequest schemas and table
# ---------------------------------------------------------------------------


class VacationRequestBase(SQLModel):
    """Purpose: Shared vacation request fields with date range validation

    Structure:
        start_date (date): input - Start date of vacation
        end_date (date): input - End date of vacation (must be >= start_date)
        reason (str): input - Reason for vacation request (1–500 chars)

    Semantics:
        Domain: vacation-management
        Entity: VacationRequest
        Logic: [end_date must be >= start_date]
    """
    start_date: dt.date
    end_date: dt.date
    reason: str = Field(min_length=1, max_length=500)

    @model_validator(mode="after")
    def validate_date_range(self) -> "VacationRequestBase":
        if self.end_date < self.start_date:
            raise ValueError("end_date must be greater than or equal to start_date")
        return self


class VacationRequestCreate(VacationRequestBase):
    """Purpose: Schema for vacation request creation"""
    pass


class VacationRequestUpdate(SQLModel):
    """Purpose: Schema for vacation request update (all fields optional)

    Structure:
        start_date (date | None): input - Updated start date
        end_date (date | None): input - Updated end date
        reason (str | None): input - Updated reason
        status (str | None): input - Updated status

    Semantics:
        Logic: [Date constraint checked only when both dates provided]
    """
    start_date: Optional[dt.date] = None
    end_date: Optional[dt.date] = None
    reason: str | None = Field(default=None, min_length=1, max_length=500)
    status: str | None = Field(default=None, max_length=20)

    @model_validator(mode="after")
    def validate_date_range(self) -> "VacationRequestUpdate":
        if self.start_date is not None and self.end_date is not None:
            if self.end_date < self.start_date:
                raise ValueError("end_date must be greater than or equal to start_date")
        return self


class VacationRequest(VacationRequestBase, table=True):
    """Purpose: VacationRequest database table owned by a User

    Relationships:
        Consumes: user.id (FK owner_id)
        Produces: vacationrequest table; back-populates User.vacation_requests
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    status: str = Field(default="pending", max_length=20)
    created_at: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),  # type: ignore
    )
    owner_id: uuid.UUID = Field(
        foreign_key="user.id", nullable=False, ondelete="CASCADE"
    )
    owner: User | None = Relationship(back_populates="vacation_requests")


class VacationRequestPublic(VacationRequestBase):
    """Purpose: VacationRequest response schema with owner reference"""
    id: uuid.UUID
    owner_id: uuid.UUID
    status: str
    created_at: datetime | None = None


class VacationRequestsPublic(SQLModel):
    """Purpose: Paginated vacation request list response"""
    data: list[VacationRequestPublic]
    count: int
