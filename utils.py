import re
from typing import Union, TextIO, Iterator, Generator

def slice_limit(limit: int, it: Union[str, TextIO, Iterator, Generator]) -> Generator:
    i = 0
    for item in it:
        if i < limit:
            yield item
        else:
            break
        i += 1

def commands(it: Union[str, TextIO, Iterator, Generator], cmd: str, value: str) -> Union[str, Iterator, Generator]:
    if cmd == 'filter':
        return filter(lambda line: value in line, it)
    elif cmd == 'map':
        return map(lambda line: line.split()[int(value)], it)
    elif cmd == 'unique':
        return iter(set(it))
    elif cmd == 'limit':
        return slice_limit(int(value), it)
    elif cmd == 'sort':
        return iter(sorted(it, reverse=value == 'desc'))
    elif cmd == 'regex':
        regexp: re.Pattern = re.compile(value)
        return filter(lambda v: regexp.findall(v), it)
    return ''
