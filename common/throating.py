from rest_framework.throttling import SimpleRateThrottle, UserRateThrottle


class CreateContactApplicationPhoneNumberThrottle(SimpleRateThrottle):
    rate = '3/h'
    scope = 'create_contact_application'

    def get_cache_key(self, request, view):
        return request.data.get('phone')


class CreateContactApplicationIPThrottle(UserRateThrottle):
    rate = '3/m'
    scope = 'create_contact_application'


class ViewIPThrottle(UserRateThrottle):
    rate = '1/m'
    scope = 'viewed_news'