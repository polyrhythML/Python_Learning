# Raise Statement
"""
* Used to raise an exception explicitly.
eg. raise instance
    raise class
    raise

"""

# Scope of variable assigned using as
"""
* It does so because it would otherwise retain a reference to the runtime
call stack, which would defer garbage collection and thus retain excess memory space.
This removal occurs, though, even if you’re using the name elsewhere, and is more
extreme policy than that used for comprehensions.

* Therefore, use unique variable names in your try statement.
"""


def scope_as():
    # Example-1, All references of the X are garbage collected
    X = 99
    try:
        1/0
    except Exception as X:
        print(X)
    print(X)                # output : X not defined

    # Example-2, Comprehension does not do it that way.

    X = 99
    out_dict = {X for X in "spam"}
    print(X)                # output : 99

    # Save the instance variable into another variable for further use
    try:
        1/0
    except Exception as X:
        print(X)
        saveit = X      # Use this for further use in the code


def prop_raise():
    """
    Running a raise this way reraises the exception and propagates it to a higher handler
    (or the default handler at the top, which stops the program with a standard error mes-
    sage)

    """
    try:
        raise IndexError("spam")    # Exception remember arguments
    except IndexError:
        print("propagating")
        raise                       # Reraise the most recent exception


def exception_chain():
    # raise newexception from otherexception
    """
    When the from is used in an explicit raise request, the expression
    following from specifies another exception class or instance to attach
    to the __cause__ attribute of the new exception being raised.
    If the raised exception is not caught, Python prints both exceptions
    as part of the standard error message:
    """
    try:
        try:
            raise IndexError()
        except Exception as E:
            raise TypeError from E
    except Exception as E:
        raise SyntaxError() from E


# None as exception name
# "raise Exception from None"

"""
    This allows the display of the chained exception context described in
    the preceding section to be disabled. This makes for less cluttered error
    messages in applications that convert between exception types while
    processing exception chains. 
"""



