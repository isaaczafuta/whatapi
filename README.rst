whatapi
=======

This project is a simple wrapper around the What.cd AJAX API.

Example usage:

::

    >>> import whatapi
    >>> apihandle = whatapi.WhatAPI(username='me', password='secret')
    >>> apihandle.request("browse", search="Belle & Sebastian")

API available at  `Gwindow's API page <https://github.com/Gwindow/WhatAPI>`_.
