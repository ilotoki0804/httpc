# httpc

[![Sponsoring](https://img.shields.io/badge/Sponsoring-Patreon-blue?logo=patreon&logoColor=white)](https://www.patreon.com/ilotoki0804)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Filotoki0804%2Fhttpc&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://github.com/ilotoki0804/httpc)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/httpc)](https://pypi.org/project/httpc/)
[![image](https://img.shields.io/pypi/l/httpc.svg)](https://github.com/ilotoki0804/httpc/blob/main/LICENSE)
[![image](https://img.shields.io/pypi/pyversions/httpc.svg)](https://pypi.org/project/httpc/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/ilotoki0804/httpc/blob/main/pyproject.toml)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/ilotoki0804/httpc/blob/main/pyproject.toml)

**httpx with CSS**

## Installation

```console
pip install -U httpc
```

## Examples

```python
>>> import httpc
>>> response = httpc.get("https://www.python.org/")
>>> response.match("strong")  # CSS Matching
[<Node strong>, <Node strong>, <Node strong>]
>>> response.match("strong").bc.text()  # Broadcasting
['Notice:', 'A A', 'relaunched community-run job board']
>>> response.single("div")  # .single() method
ValueError: Query 'div' matched with 47 nodes (error from 'https://www.python.org/').
>>> response.single("div", remain_ok=True)  # .single() method
<Node div>
>>> response.single("#content")
<Node div>
>>> httpc.get("https://python.org")
<Response [301 Moved Permanently]>
>>> httpc.common.get("https://python.org")  # ClientOptions and httpc.common
<Response [200 OK]>
>>> httpc.common.get("https://hypothetical-unstable-website.com/", retry=5)  # retry parameter
Attempting fetch again (ConnectError)...
Attempting fetch again (ConnectError)...
Successfully retrieve 'https://hypothetical-unstable-website.com/'
<Response [200 OK]>
>>> httpc.get("https://httpbin.org/status/400")
<Response [400 BAD REQUEST]>
>>> httpc.get("https://httpbin.org/status/400", raise_for_status=True)  # raise_for_status as parameter
httpx.HTTPStatusError: Client error '400 BAD REQUEST' for url 'https://httpbin.org/status/400'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400
>>> httpc.get("https://httpbin.org/status/500", raise_for_status=True, retry=3)
Attempting fetch again (status code 500)...
Attempting fetch again (status code 500)...
Attempting fetch again (status code 500)...
httpx.HTTPStatusError: Server error '500 INTERNAL SERVER ERROR' for url 'https://httpbin.org/status/500'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500
```

## Release Note

* 0.7.0: Add httpc.catcher (from [httpx-catcher](https://github.com/ilotoki0804/httpx-catcher))
* 0.6.0: Remove deprecated parameters, remove ClientOptions
* 0.5.0: Use Lexbor as default backend, fix and improve retry and raise_for_status
* 0.4.0: Fix incorrect type hint, rename CSSTool to ParseTool, CSSResponse to Response, bugfixes and small improvements
* 0.3.0: Add `new` parameter, remove `select` method, rename `css` to `match` from CSSTool, remove cache_api.py (unused script), add url note, retry if server error on raise_for_status, bugfix
* 0.2.0: Initial release
