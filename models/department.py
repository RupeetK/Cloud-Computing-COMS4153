from __future__ import annotations

from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field

class DepartmentBase(BaseModel):
    id: UUID = Field(
        default_factory=uuid4,
        description="Persistent Address ID (server-generated).",
        json_schema_extra={"example": "550e8400-e29b-41d4-a716-446655440000"},
    )
    dept_name: str = Field(
        ...,
        description="Department name",
        json_schema_extra={"example": "Comp. Sci."},
    )
    building: str = Field(
        ...,
        description="Department building",
        json_schema_extra={"example": "Mudd"},
    )
    budget: Optional[int] = Field(
        None,
        description="Department budget",
        json_schema_extra={"example": 100000},
    )
    location: Optional[str] = Field(
        None,
        description="Department location",
        json_schema_extra={"example": "500W 120th St"},
    )

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                'id':'550e8400-e29b-41d4-a716-446655440000',
                'dept_name':'Comp. Sci.',
                'building':'Mudd',
                'budget':'100000',
                'location':'500W 120th St',
            }
        ]
        }
    }

class DepartmentCreate(DepartmentBase):
    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'id': '550e8400-e29b-41d4-a716-446655440000',
                    'dept_name': 'Comp. Sci.',
                    'building': 'Mudd',
                    'budget': '100000',
                    'location': '500W 120th St',
                }
            ]
        }
    }

class DepartmentUpdate(BaseModel):
    dept_name: Optional[str] = Field(
        None, description="Department name", json_schema_extra={"example": "Comp. Sci."}
    )
    building: Optional[str] = Field(
        None, description="Department building", json_schema_extra={"example": "Mudd"}
    )
    budget: Optional[int] = Field(
        None, description="Department budget", json_schema_extra={"example": 100000}
    )
    location: Optional[str] = Field(
        None, description="Department location", json_schema_extra={"example": "500W 120th St"}
    )
    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'dept_name': 'Comp. Sci.',
                    'building': 'Mudd',
                    'budget': '100000',
                    'location': '500W 120th St',
                },
                {
                    'dept_name': 'Biology',
                }
            ]
        }
    }

class DepartmentRead(DepartmentBase):
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
                    'id': "550e8400-e29b-41d4-a716-446655440000",
                    'dept_name': 'Comp. Sci.',
                    'building': 'Mudd',
                    'budget': '100000',
                    'location': '500W 120th St',
                    "created_at": "2025-01-15T10:20:30Z",
                    "updated_at": "2025-01-16T12:00:00Z",
                }
            ]
        }
    }

