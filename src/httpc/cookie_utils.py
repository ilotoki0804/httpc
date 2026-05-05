from http.cookies import Morsel, SimpleCookie
import typing


def cookie_json_to_raw(cookies: dict, name: str = "name", value: str = "value") -> str:
    cookies_text = []
    for cookie in cookies:
        cookies_text.append(f'{cookie[name]}={cookie[value]}')
    return "; ".join(cookies_text)


def cookie_dict_to_raw(cookies: dict[str, Morsel] | dict[str, str]) -> str:
    cookies_text = []
    for name, value in cookies.items():
        if isinstance(value, Morsel):
            value = value.coded_value
        cookies_text.append(f'{name}={value}')
    return "; ".join(cookies_text)


def set_cookies(cookie_string: str, cookies: typing.Mapping[str, str] | dict[str, Morsel]) -> str:
    cookie = SimpleCookie(cookie_string)
    for name, value in cookies.items():
        cookie[name] = value
    return cookie_dict_to_raw(cookie)
