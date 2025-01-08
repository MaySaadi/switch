def deepClone(obj):
    if isinstance(obj, dict):
        return {key: deepClone(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [deepClone(item) for item in obj]
    elif isinstance(obj, tuple):
        return tuple(deepClone(item) for item in obj)
    elif isinstance(obj, set):
        return {deepClone(item) for item in obj}
    else:
        return obj
    
x = {"a": "b", "a2": ["first", "second"]}
y = {"b": x, "b3": ["firtsY", x]}
z = deepClone(y)
print("Cloned z:", z)