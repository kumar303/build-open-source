import cPickle as pickle
from datetime import datetime, timedelta
import os
import sys
import time

import requests

if __name__ == '__main__':
    repos = set()
    searches = [
        '@mozilla django in:name',
        '@kumar303 django in:name',
        '@andymckay django in:name',
        '@jsocol django in:name',
        '@jbalogh django in:name',
        '@robhudson django in:name',
        '@osmoose django in:name',
    ]
    since = (datetime.utcnow() - timedelta(days=1)).strftime(
                                        '%a, %d %b %Y %H:%M:%S GMT')
    pkl_file = os.path.join(os.path.dirname(__file__), '.mozrepos.pkl')
    if not os.path.exists(pkl_file):
        with open(pkl_file, 'w') as f:
            f.write('')
    with open(pkl_file, 'r') as f:
        try:
            etags = pickle.load(f)
        except EOFError:
            etags = {}

    exc = None
    for q in searches:
        print 'searching {0}'.format(q)
        res = requests.get('https://api.github.com/search/repositories',
            params={'q': q},
            headers={'User-Agent': 'kumar303',
                     'If-Modified-Since': since,
                     'Etag': etags.get(q),
                     'Accept': 'application/vnd.github.preview'})
        time.sleep(3)  # rate limit
        if 'Etag' in res.headers:
            etags[q] = res.headers['Etag'][1:-1]  # stip quotes

        data = res.json()
        try:
            for item in data['items']:
                repos.add(item['name'])
        except Exception:
            exc = sys.exc_info()
            print ' ** {0}'.format(exc)
            print data

    for nm in sorted(repos):
        print nm

    if exc:
        raise exc

    with open(pkl_file, 'w') as f:
        pickle.dump(etags, f)

    # django-adminplus
    # django-aesfield
    # django-arecibo
    # django-authority
    # django-badger
    # django-blueberry
    # django-browserid
    # django-cache-machine
    # django-cronjobs
    # django-csp
    # django-debug-cache-panel
    # django-delayed-mailer
    # django-dnt
    # django-fail
    # django-headegg
    # django-include-cache
    # django-jobvite
    # django-jsonview
    # django-lawnchair
    # django-lint
    # django-memcached-pool
    # django-mobility
    # django-moz-header
    # django-mq
    # django-multidb-router
    # django-mysql-aesfield
    # django-mysql-pool
    # django-nose
    # django-paranoia
    # django-piston
    # django-piston-oauth2
    # django-pylibmc
    # django-pymemcache
    # django-query-analyzer
    # django-quieter-formset
    # django-radagast
    # django-rapidsms-malnutrition
    # django-ratelimit
    # django-receipts
    # django-reusable-tables
    # django-session-csrf
    # django-statsd
    # django-ual
    # django-waffle
    # django_appcache
    # djangode
    # djangopeople-jsonp
    # djangoproject-services
