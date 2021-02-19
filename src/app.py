import i18n
from pathlib import Path

from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from src.config import Config
# from src.database import Database
from src.controllers import MovieSuggestController


def create_app():
    from src.controllers.common import errors
    # flask app config
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    # Database()
    app.app_context().push()
    api = Api(app, errors=errors.errors)

    # Register api endpoint
    api.add_resource(MovieSuggestController, '/movie')

    
    flask_restfull_default_handle_error = api.handle_error

    def webapi_default_error_handler(error):
        '''Default error handler'''
        try:
            if error.custom_message is not None:
                if error.api_code is not None:
                    code = '{}.{}'.format(
                        error.api_code,
                        api.errors[error.__class__.__name__]['code']
                    )
                else:
                    code = api.errors[error.__class__.__name__]['code']

                return {
                    'message': error.custom_message, 
                    'status': api.errors[error.__class__.__name__]['status'],
                    'code': code
                }, getattr(error, 'code', 500)
            else:
                return flask_restfull_default_handle_error(error)
        except:
            return flask_restfull_default_handle_error(error)

    api.handle_error = webapi_default_error_handler
    return app

# setup i18n
i18n.load_path.append(Path(__file__).parent.joinpath('locales'))
i18n.set('filename_format', '{locale}.{format}')
i18n.set('locale', Config.LOCALE)
i18n.set('enable_memoization', True)

app = create_app()

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
