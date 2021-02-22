"""
Refs: https://marshmallow.readthedocs.io/en/stable/
"""

from marshmallow import fields, validate
from src.constants import TaskStatus
from src.utils import helper
from .base_response_schema import BaseResponseSchema

class MovieResponseSchema(BaseResponseSchema):
    title = fields.String(required=True)
    score = fields.Float(required=True)