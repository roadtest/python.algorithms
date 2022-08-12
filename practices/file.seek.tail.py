#!/usr/bin/env python3
def tail(f, window=20):
    """
    Returns the last `window` lines of file `f` as a list.
    f - a byte file-like object
    """
    if window == 0:
        return []
    BUFSIZ = 1024
    f.seek(0, 2)
    bytes = f.tell()
    size = window + 1
    block = -1
    data = []
    while size > 0 and bytes > 0:
        if bytes - BUFSIZ > 0:
            # Seek back one whole BUFSIZ
            f.seek(block * BUFSIZ, 2)
            # read BUFFER
            data.insert(0, f.read(BUFSIZ).decode("utf-8"))
        else:
            # file too small, start from begining
            f.seek(0, 0)
            # only read what was not read
            data.insert(0, f.read(bytes).decode("utf-8"))
        linesFound = data[0].count("\n")
        size -= linesFound
        bytes -= BUFSIZ
        block -= 1
    return "".join(data).splitlines()[-window:]


if __name__ == "__main__":
    with open("/tmp/data.txt", "rb") as file:
        print(tail(file, 5))
