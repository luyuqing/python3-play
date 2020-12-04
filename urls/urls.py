"""
Utilities for working with URLs.

Copyright 2019, 2020 Boost AI AS
All rights reserved.
"""

from typing import (
    Any,
    Dict,
    Optional,
    overload,
)
import urllib.parse


@overload
def base_url(url: None) -> None:
    ...


@overload
def base_url(url: str) -> str:
    ...


def base_url(url: Optional[str]) -> Optional[str]:
    """
    Returns scheme and netloc from URL, thus normalizing somewhat the base URL.

    Examples:

        >>> base_url("https://xyz.boost.ai/search/?q=hi")
        'https://xyz.boost.ai'
        >>> base_url("https://xyz.boost.ai/")
        'https://xyz.boost.ai'
    """
    if url is None:
        return None

    parts = urllib.parse.urlparse(url.strip())
    return urllib.parse.urlunparse((parts[0], parts[1], "", "", "", ""))


def join(url: str, path: str) -> str:
    """
    Either replaces or appends path in URL.

    IMPORTANT: To append, `url` MUST end with a slash while `path` MUST NOT
    begin with one:

        >>> join("https://my.boost.ai/api/", "whatever")  # appends
        'https://my.boost.ai/api/whatever'

    In all other cases, the given path is overwritten:

        >>> join("https://my.boost.ai/api/", "/whatever")  # replaces
        'https://my.boost.ai/whatever'

        >>> join("https://my.boost.ai/api", "/whatever")  # replaces
        'https://my.boost.ai/whatever'

        >>> join("https://my.boost.ai/api", "whatever")  # replaces
        'https://my.boost.ai/whatever'
    """
    # NOTE: At some point we may want to remove this method and just rename
    # ``safe_join`` to ``join`` instead, because it's much more applicable and
    # easier to use.
    return urllib.parse.urljoin(url, path)


def safe_join(url: str, path: Optional[str]) -> str:
    """
    Appends ``path`` to ``url`` with slashes in between.

    This is nearly the same as the ``urls.join`` function, except for the
    extremely difficult-to-get-right edge cases.

    Examples:

        >>> join("https://my.boost.ai/api/", "whatever")
        'https://my.boost.ai/api/whatever'

        >>> join("https://my.boost.ai/api/", "/whatever")
        'https://my.boost.ai/api/whatever'

        >>> join("https://my.boost.ai/api", "/whatever")
        'https://my.boost.ai/api/whatever'

        >>> join("https://my.boost.ai/api", "whatever")
        'https://my.boost.ai/api/whatever'

        >>> join("https://my.boost.ai/api", None)
        'https://my.boost.ai/api'

        >>> join("https://my.boost.ai/api/", None)
        'https://my.boost.ai/api/'
    """
    if not path:
        return url

    # as a leading slash will create issues in paths, leading slashes are removed
    while path and path.startswith("/"):
        path = path[1:]

    # MUST end with slash
    if url[-1] != "/":
        url += "/"

    return urllib.parse.urljoin(url, path)


def base_url_join(url, path):
    """
    Transforms `url` into a base URL and adds a path.
    """
    return join(base_url(url), path)


def make_url(scheme: str,
             netloc: str,
             path: str = "",
             params: str = "",
             query: str = "",
             fragment: str = "") -> str:
    """
    Constructs a URL from components.

    :param scheme:
        URL scheme specifier, typically ``http`` or ``https``.

    :param netloc:
        Network location part. Port numbers are designated by a trailing colon
        and a number.

    :param path:
        Hierarchical path, e.g. "/api/chat/v2"

    :param params:
        Parameters for last path element.

    :param query:
        Query component.

    :param fragment:
        Fragment identifier.

    :return:
        URL after being put through a parsing roundtrip.
    """
    if not scheme.isalpha():
        raise ValueError("Invalid URL scheme: %r" % scheme)

    if "/" in netloc:
        raise ValueError("Invalid URL netloc: %r" % netloc)

    ps = urllib.parse.ParseResult(scheme=scheme,
                                  netloc=netloc,
                                  path=path,
                                  params=params,
                                  query=query,
                                  fragment=fragment)
    return ps.geturl()


def update_url_params(url: str, **kw) -> str:
    """
    Adds URL parameters given as key-value arguments. If the key
    already exists its overwritten by the new value.

    >>> update_url_params('http://127.0.0.1:8000/api/derp?arg1=arg1&arg2=arg2, arg2=newarg2, arg3=arg3)
    http://127.0.0.1:8000/api/derp?arg2=newarg2&arg1=arg1&arg3=arg3
    """

    scheme, netloc, path, query_string, fragment = urllib.parse.urlsplit(url)
    url_query = urllib.parse.parse_qs(query_string)
    url_query.update(kw)
    new_query_string = urllib.parse.urlencode(url_query, doseq=True)

    return urllib.parse.urlunsplit((scheme, netloc, path, new_query_string, fragment))


def make_path(args: Dict[str, Any]) -> str:
    """
    Converts dictionary to URL path.
    Iterable values are repeated with the same key.
    """
    flattened = []

    for key, value in args.items():
        if isinstance(value, (list, tuple)):
            for x in value:
                flattened.append(urllib.parse.urlencode({key: x}))
        else:
            flattened.append(urllib.parse.urlencode({key: value}))

    return "&".join(flattened)
