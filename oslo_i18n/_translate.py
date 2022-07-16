__all__ = [
    'translate',
]

def translate(obj, desired_locale=None):
    """Get the translated unicode representation of the given object.
    
    If the object is not translatable it is returned as-it.
    
    If the desired_locale argument is None the object is translated to
    the system locale.
    
    :param obj: the object to translate
    :param desired_locale: the locale to translate the message to, if None the
    """
    from oslo_i18n import _message
    message = obj
    if not isinstance(message, _message.Message):