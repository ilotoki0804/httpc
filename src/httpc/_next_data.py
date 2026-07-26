# 편의상 "next data"라고 부르나 정식 명칭은 RSC payload임.
# 정식 설명을 확인하려면: https://github.com/vercel/next.js/discussions/42170#discussioncomment-8137079
# 다른 rsc parser를 확인해보려면: https://github.com/alvarlagerlof/rsc-parser
# 다른 rsc parser를 사용하고 싶으면: https://rsc-parser.vercel.app/
# 완전한 파싱을 확인하려면: https://github.com/alvarlagerlof/rsc-parser/blob/main/packages/react-client/src/ReactFlightClient.ts

from __future__ import annotations

import json
import re
import typing

from ._base import logger

next_f_data = re.compile(r"self\.__next_f\.push\(\[\d+,\s*(.*)\]\)", re.DOTALL)
# HL, I, "$"가 각각 어떤 역할을 하는지 알려면 https://roy-jung.github.io/250323-react-server-components/ 이 코드 참고
line_regex = re.compile(r"^\s*(?P<hexdigit>[0-9a-fA-F]+):(?P<data_prefix>[A-Z]*)(?P<data_raw>.*)")
impared_line_regex = re.compile(r".+>(?P<hexdigit>[0-9a-fA-F]+):(?P<data_prefix>[A-Z]*)(?P<data_raw>.*)")


class NextData(typing.NamedTuple):
    line_no: int
    hexdigit: str
    prefix: str
    value: typing.Any
    parsed: bool


def extract_next_data(scripts: typing.Iterable[str], prefix_to_ignore: typing.Container[str] | None = None, warn_not_parsed: bool = False) -> list[NextData]:
    line: str
    next_data = []
    joined = ""
    for script in scripts:
        matched = next_f_data.match(script)
        if not matched:
            continue
        joined += json.loads(matched[1])

    # FIXME
    # line_no = -1
    # line = ""
    # parse_left: str = joined
    # # for line_no, line in enumerate(joined.split("\n")):
    # while True:
    #     if not parse_left:  # 모든 Input 소비
    #         break
    #     line, sep, parse_left = parse_left.partition("\n")
    #     line_no += 1

    not_expected_format_lines = []
    for line_no, line in enumerate(joined.split("\n")):
        if not line:
            continue
        matched = line_regex.match(line)
        if not matched:
            if matched := impared_line_regex.match(line):
                logger.warning(f"Line {line_no} is impared. retrived {matched['hexdigit']}")
            else:
                # TODO: 형식 완전히 규명해서 이 문제 해결하기
                # 가끔 raw data가 수신될 때 \n을 포함해서 문제가 생기는 경우가 있음
                # 형식을 완전히 확인할 수 있을 때까지 일단 warning으로 처리하고 작동하도록 함
                not_expected_format_lines.append(str(line_no))
                # logger.warning(f"Line {line_no} does not match the expected format: {line!r}")
                continue
            # raise ValueError(f"Line {line_no} does not match the expected format: {line!r}")

        hexdigit = matched["hexdigit"]
        data_prefix = matched["data_prefix"]
        data_raw = matched["data_raw"]
        if prefix_to_ignore and data_prefix in prefix_to_ignore:
            continue
        try:
            json_data = json.loads(data_raw)
        except json.JSONDecodeError:
            if warn_not_parsed:
                logger.warning(f"Failed to parse following data to JSON: {data_raw}")
            if matched := impared_line_regex.match(data_raw):  # FIXME: 매우 매우 비정상적인 방법. T 타입을 파싱하는 방법을 반드시 찾아낼 것
                logger.warning(f"extracted impared data from {matched['hexdigit']}")
                json_data = json.loads(matched["data_raw"])
                parsed = True
            else:
                json_data = data_raw
                parsed = False
        else:
            parsed = True
        next_data.append(NextData(line_no, hexdigit, data_prefix, json_data, parsed))

    if not_expected_format_lines:
        logger.warning(f'Line {", ".join(not_expected_format_lines)} didn\'t match the expected format.')
    next_data.sort(key=lambda x: int(x.hexdigit, 16))
    return next_data
