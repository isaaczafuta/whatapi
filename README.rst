whatapi
=======

This project is a simple wrapper around the What.cd AJAX API. Also compatible
with what-like trackers such as pth/apollo.

Available via PyPI via pip:

::

    # pip install whatapi


Example usage:

::

    >>> import whatapi
    >>> apihandle = whatapi.WhatAPI(username='me', password='secret')
    >>> apihandle.request("browse", searchstr="Talulah Gosh")
    ...
    >>> apihandle.get_torrent(1234567)
    ...


To use another tracker:

::

    >>> import whatapi
    >>> apihandle = whatapi.WhatAPI(username='me', password='secret',
                                    server='https://passtheheadphones.me')
    >>> apihandle.request("browse", searchstr="The Beatles")
    ...


It's strongly recommended that your script implements saving/loading session cookies to prevent overloading the server.

Example:

::

    >>> import whatapi
    >>> import cPickle as pickle
    >>> cookies = pickle.load(open('cookies.dat', 'rb'))
    >>> apihandle = whatapi.WhatAPI(username='me', password='me', cookies=cookies)
    ...
    >>> pickle.dump(apihandle.session.cookies, open('cookies.dat', 'wb'))

API available at  `Gwindow's API page <https://github.com/Gwindow/WhatAPI>`_ or via the JSON API page on What.
