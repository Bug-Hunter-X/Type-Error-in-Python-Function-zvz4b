def function(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        return "Error: Invalid input types"

result = function(5, "hello")
print(result)

result = function(5, 10)
print(result)