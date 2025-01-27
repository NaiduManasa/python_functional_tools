# lambda
Used to create small, anonymous function(for temporary use without name) anf dor simple applications.

## syntax
***lambda arguments : expression***

**lambda:** keyword to define function<br>
**argumnets:** list of parameters given as input to the function<br>
**expression:** that is evaluated and returned

## What is key=lambda?
In Python, key is a parameter used in functions like sorted(), min(), max(), and map() to specify a custom sorting or comparison criterion. The lambda function is a way to define a small, anonymous function inline, without needing to define a full function.When you combine key with lambda, you can define how to extract or compute a value from each element of an iterable (like a list or tuple) that will be used for sorting or comparison.

**Syntax:**

function_name(iterable, key=lambda x: expression )

    iterable: The collection (like a list or tuple) you want to sort or process.
    key: A function that takes an element from the iterable and returns a value used for sorting/comparison.
    lambda x: <expression>: An anonymous function that returns a value from each element x in the iterable.
