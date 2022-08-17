#!/usr/bin/env python3

import io

stream_str = io.BytesIO(b"JournalDev Python: ")
# print(stream_str.getvalue())

data = io.StringIO()
data.write("JournalDev: ")
print("Python.", file=data)

# print(data.getvalue())

data.close()
