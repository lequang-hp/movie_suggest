from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser

from src.services import MovieSuggestService
from .anonymous_base_controller import AnonymousBaseController
from src.controllers.common.http_exceptions import HTTPNotFoundException, HTTPServerInternalException
from src.controllers.common.http_exceptions import HTTPInvalidContentFormatException, HTTPInvalidFileFormatException, HTTPDataEmptyException
from src.exceptions import WebapiException
from src.exceptions import ErrorCode

from .schemas import TaskResponseSchema
from marshmallow import EXCLUDE

from flask import Response

movie_args = {
   "title": fields.Str(required=True)
}

@parser.error_handler
def handle_request_parsing_error(error, req, schema, *, error_status_code, error_headers):
    raise HTTPInvalidFileFormatException()

class MovieSuggestController(AnonymousBaseController):
    def __init__(self):
        super().__init__()

    @use_args(movie_args)
    def post(self,args):
        try:
            title = args["title"]
            movie_suggest_service = MovieSuggestService()
            response_file = movie_suggest_service.suggest_movie(title)
            return response_file
        except WebapiException as e:
            if e.code == ErrorCode.INVALID_CONTENT_FORMAT:
                raise HTTPInvalidContentFormatException()
            elif e.code == ErrorCode.DATA_EMPTY:
                raise HTTPDataEmptyException()
            else: 
                raise HTTPServerInternalException()