from pathlib import Path
from typing import Callable, TypeVar, overload

T = TypeVar('T')


@overload
def data_import(
    filename: str,
    cast: Callable[[str], T] = ...,
    split_char: str = ...,
    rstrip: bool = ...,
) -> list[list[T]]: ...


@overload
def data_import(
    filename: str,
    cast: Callable[[str], T] = ...,
    split_char: None = ...,
    rstrip: bool = ...,
) -> list[T]: ...


def data_import(
    filename: str,
    cast: Callable[[str], T] = str,
    split_char: str | None = None,
    rstrip: bool = False,
) -> list[T] | list[list[T]]:
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
