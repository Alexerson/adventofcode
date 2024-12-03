from pathlib import Path
from typing import Callable, TypeVar, overload

T = TypeVar('T')


@overload
def data_import(
    filename: str,
    cast: None = None,
    split_char: None = None,
    rstrip: bool = ...,
) -> list[str]: ...


@overload
def data_import(
    filename: str,
    cast: Callable[[str], T],
    split_char: None = None,
    rstrip: bool = ...,
) -> list[T]: ...


@overload
def data_import(
    filename: str,
    cast: None = None,
    split_char: str = ' ',
    rstrip: bool = ...,
) -> list[list[str]]: ...


@overload
def data_import(
    filename: str,
    cast: Callable[[str], T],
    split_char: str = ' ',
    rstrip: bool = ...,
) -> list[list[T]]: ...


def data_import(
    filename: str,
    cast: Callable[[str], T] | None = None,
    split_char: str | None = None,
    rstrip: bool = False,
) -> list[T] | list[list[T]]:
    if cast is None:
        cast = str
    path = Path(filename)
    data = []
    with path.open(encoding='utf-8') as file:
        for line in file:
            if (rstrip and line.rstrip()) or line.strip():
                if split_char is not None:
                    line = line.split(split_char)
                    data.append([cast(item.strip()) for item in line if item])
                else:
                    data.append(
                        cast((rstrip and line.rstrip()) or line.strip())
                    )

    return data
