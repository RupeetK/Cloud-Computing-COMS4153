from __future__ import annotations

from typing import Optional, List, Annotated
from uuid import UUID, uuid4
from datetime import date, datetime
from pydantic import BaseModel, Field, EmailStr, StringConstraints

from .department import DepartmentBase

UNIType = Annotated[str, StringConstraints(pattern=r"^[a-z]{2,3}\d{1,4}$")]

class InstructorBase(BaseModel):
    uni: UNIType = Field(
        ...,
        description="Columbia University UNI (2–3 lowercase letters + 1–4 digits).",
        json_schema_extra={"example": "abc1234"},
    )
    first_name: str = Field(
        ...,
        description="Given name.",
        json_schema_extra={"example": "Ada"},
    )
    last_name: str = Field(
        ...,
        description="Family name.",
        json_schema_extra={"example": "Lovelace"},
    )
    email: EmailStr = Field(
        ...,
        description="Primary email address.",
        json_schema_extra={"example": "ada@example.com"},
    )
    phone: Optional[str] = Field(
        None,
        description="Contact phone number in any reasonable format.",
        json_schema_extra={"example": "+1-212-555-0199"},
    )
    departments: List[DepartmentBase] = Field(
        default_factory=list,
        description="Departments linked to this instructor",
        json_schema_extra= {
        'example': [
            {
                'id': '550e8400-e29b-41d4-a716-446655440000',
                'dept_name': 'Comp. Sci.',
                'building': 'Mudd',
                'budget': '100000',
                'location': '500W 120th St',
            }
        ]
    },
    )
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "uni": "abc1234",
                    "first_name": "Ada",
                    "last_name": "Lovelace",
                    "email": "ada@example.com",
                    "phone": "+1-212-555-0199",
                    "departments": [
                        {
                            'id': '550e8400-e29b-41d4-a716-446655440000',
                            'dept_name': 'Comp. Sci.',
                            'building': 'Mudd',
                            'budget': '100000',
                            'location': '500W 120th St',
                        }
                    ],
                }
            ]
        }
    }

class InstructorCreate(InstructorBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "uni": "abc1234",
                    "first_name": "Ada",
                    "last_name": "Lovelace",
                    "email": "ada@example.com",
                    "phone": "+1-212-555-0199",
                    "departments": [
                        {
                            'id': '550e8400-e29b-41d4-a716-446655440000',
                            'dept_name': 'Comp. Sci.',
                            'building': 'Mudd',
                            'budget': '100000',
                            'location': '500W 120th St',
                        }
                    ],
                }
            ]
        }
    }

class InstructorUpdate(BaseModel):
    uni: Optional[UNIType] = Field(
        None, description="Columbia UNI.", json_schema_extra={"example": "ab1234"}
    )
    first_name: Optional[str] = Field(None, json_schema_extra={"example": "Augusta"})
    last_name: Optional[str] = Field(None, json_schema_extra={"example": "King"})
    email: Optional[EmailStr] = Field(None, json_schema_extra={"example": "ada@newmail.com"})
    phone: Optional[str] = Field(None, json_schema_extra={"example": "+44 20 7946 0958"})
    departments: Optional[List[DepartmentBase]] = Field(
        None,
        description="Replace the entire set of departments with this list.",
        json_schema_extra={
            "example": [
                {
                    'id': '550e8400-e29b-41d4-a716-446655440000',
                    'dept_name': 'Comp. Sci.',
                    'building': 'Mudd',
                    'budget': '100000',
                    'location': '500W 120th St',
                }
            ],
        }
    )
    model_config = {
        "json_schema_extra": {
            "examples": [
                {"first_name": "Ada", "last_name": "Byron"},
                {"phone": "+1-412-555-0199"},
                {'departments': [
                    {
                        'id': '550e8400-e29b-41d4-a716-446655440000',
                        'dept_name': 'Comp. Sci.',
                        'building': 'Mudd',
                        'budget': '100000',
                        'location': '500W 120th St',
                    }
                ]
                },
            ]
        }
    }

class InstructorRead(InstructorBase):
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated Instructor ID.",
        json_schema_extra={"example": "99999999-9999-4999-8999-999999999999"},
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-01-15T10:20:30Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp (UTC).",
        json_schema_extra={"example": "2025-01-16T12:00:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "99999999-9999-4999-8999-999999999999",
                    "uni": "abc1234",
                    "first_name": "Ada",
                    "last_name": "Lovelace",
                    "email": "ada@example.com",
                    "phone": "+1-212-555-0199",
                    "departments": [
                        {
                            'id': '550e8400-e29b-41d4-a716-446655440000',
                            'dept_name': 'Comp. Sci.',
                            'building': 'Mudd',
                            'budget': '100000',
                            'location': '500W 120th St',
                        }
                    ],
                    "created_at": "2025-01-15T10:20:30Z",
                    "updated_at": "2025-01-16T12:00:00Z",
                }
            ]
        }
    }







