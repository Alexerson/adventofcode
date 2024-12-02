from pathlib import Path
from typing import Any, overload


@overload
def data_import(
    filename: str, cast=..., split_char: str = ..., rstrip: bool = ...
) -> list[list]: ...


@overload
def data_import(
    filename: str, cast=..., split_char: None = ..., rstrip: bool = ...
) -> list: ...


def data_import(
    filename: str,
    cast=str,
    split_char: str | None = None,
    rstrip: bool = False,
) -> list[Any] | list[list[Any]]:
    path = Path(filename)
    data = []
    with path.open(encoding='utf-8') as file:
        line = file.readline()
        while line:
            if (rstrip and line.rstrip()) or line.strip():
                if split_char is not None:
                    line = line.split(split_char)
                    data.append([cast(item.strip()) for item in line if item])
                else:
                    data.append(
                        cast((rstrip and line.rstrip()) or line.strip())
                    )

            line = file.readline()
    return data
