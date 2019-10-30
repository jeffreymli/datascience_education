# Google Python Style Guide Notes 

[Link](http://google.github.io/styleguide/pyguide.html)

### Raising Exceptions
- Avoid wrapping Try/Except statements in long lines of code. Long lines of code within a try, makes it more likely to raise an exception. 
- When a program violates a specific programming mistake, raise an exception, like this `raise ValueError("Error Message")`. Avoid using an assert. 

### Line Length
- The maximum line length should be 80 characters. Exceptions are long import statements, URL's, comments. 

### Comments and Docstrings 
- Every file should contain license boilerplate. 
- Files should start with a docstring summarizing what the file does. 

**Function Docstrings**
- In general, every function should also have a docstring, unless:
	- Not externally visible
	- Very short
	- Obvious
- A docstring should give the reader enough information to run the function without explicitly rewriting the entire function. 

### Block and Inline Comments 

- If you're going to have to explain multiple lines of code, this means you should write a comment. 
- Comments should start at least 2 spaces away from the code. 
- Never describe code, assume the person reading it knows how to code in Python. 

```
# We use a weighted dictionary search to find out where i is in
# the array.  We extrapolate position based on the largest num
# in the array and the array size and then do binary search to
# get the exact number.

if i & (i-1) == 0:  # True if i is 0 or a power of 2.
```