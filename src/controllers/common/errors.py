import i18n


errors = {
    'HTTPBadRequestException': {
        'message': i18n.t('errors.WA4000'),
        'status': 400,
        'code': 'WA4000'
    },
    'HTTPUnauthorizedException': {
        'message': i18n.t('errors.WA4001'),
        'status': 401,
        'code': 'WA4001'
    },
    'HTTPPermissionDeniedException': {
        'message': i18n.t('errors.WA4003'),
        'status': 403,
        'code': 'WA4003'
    },
    'HTTPNotFoundException': {
        'message': i18n.t('errors.WA4004'),
        'status': 404,
        'code': 'WA4004'
    },
    'HTTPTokenExpiredException': {
        'message': i18n.t('errors.WA4100'),
        'status': 401,
        'code': 'WA4100'
    },
    'HTTPTokenExpiredException': {
        'message': i18n.t('errors.WA4101'),
        'status': 401,
        'code': 'WA4101'
    },
    'HTTPServerInternalException': {
        'message': i18n.t('errors.WA5000'),
        'status': 500,
        'code': 'WA5000'
    },
    'HTTPInvalidContentFormatException': {
        'message': i18n.t('errors.WA4005'),
        'status': 400,
        'code': 'WA4005'
    },
    'HTTPInvalidFileFormatException': {
        'message': i18n.t('errors.WA4006'),
        'status': 400,
        'code': 'WA4006'
    },
    'HTTPDataEmptyException': {
        'message': i18n.t('errors.WA4007'),
        'status': 400,
        'code': 'WA4007'
    }
}