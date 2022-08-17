#!/usr/bin/env python3


def foo():
    """
    notice we use yield in both the
    traditional generator sense and
    also in the coroutine sense.
    """
    msg = yield "beep"  # coroutine feature
    yield msg  # generator feature


coro = foo()

# because a coroutine is a generator
# we need to advance the returned generator
# to the first yield within the generator function
print(next(coro))

# the .send() syntax is specific to a coroutine
# this sends "bar" to the first yield
# so the msg variable will be assigned that value
result = coro.send("bar")

# because our coroutine also yields the msg variable
# it means we can print that value
print(result)  # bar
