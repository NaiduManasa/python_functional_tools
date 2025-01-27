# reduce
Used when a particular function is passed to all iterator elements.<br>
Returns a single final value.
This function is defined in “functools” module.

## syntax

***functools.reduce(function, iterable[, initializer])***<br>

**function:** A function that takes two arguments and performs an operation on them.<br>
**iterable:** An iterable whose elements are processed by the function.<br>
**initializer (optional):** A starting value for the operation. If provided, it is placed before the first element in the iterable.

## Using reduce() with operator functions
reduce() can also be combined with operator functions to achieve the similar functionality as with lambda functions and makes the code more readable.
