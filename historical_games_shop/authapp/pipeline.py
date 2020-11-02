import os
from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse
from django.conf import settings

import requests
import urllib.request
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'photo_200_orig')),
                                                access_token=response['access_token'],
                                                v='5.92')),
                          None
                          ))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]
    if data['sex']:
        user.shopuserprofile.gender = ShopUserProfile.MALE if data['sex'] == 2 else ShopUserProfile.FEMALE

    if data['about']:
        user.shopuserprofile.aboutMe = data['about']

    if data['bdate']:
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

        age = timezone.now().date().year - bdate.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')

    # if data['photo_200_orig']:
    #     fname = data['photo_200_orig'].split('/')[-1]
    #     fname = fname.split('?')[0]
    #     fpath =  os.path.join(settings.BASE_DIR, 'media/' + fname)
    #     f = open(fpath, 'wb')
    #     fcontent =  urllib.request.urlopen(data['photo_200_orig']).read()
    #     f.write(fcontent)
    #     f.close()
    #     user.avatar = fname

    if data['photo_200_orig']:
        print(data['photo_200_orig'])
        urllib.request.urlretrieve(data['photo_200_orig'], f'{settings.MEDIA_ROOT}/user_avatars/{user.pk}.jpg')
        user.avatar = f'user_avatars/{user.pk}.jpg'


    user.save()
