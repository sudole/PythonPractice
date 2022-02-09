print("=" * 20)
print("immutable object")
print("(number, string, tuple)")
a = 10
b = a

print("a", a, id(a))
print("b", b, id(b))
b = b+1
print("b = b+1", b, id(b))
b = b-1
print("b = b-1", b, id(b))

print("-" * 20)
print("mutable object")
print("(array, list, dictionary)")
arr = [1, 2, 3, 4, 5]

print(arr, id(arr))

arr.append(1)
print("append 1", arr, id(arr))
for i in arr:
    print(i, id(i))
print("=" * 20)

dir = [{"first":1}, {"second":2}]

print(dir, id(dir))

dir.append({"first":1})
print(dir, id(dir))

for item in dir:
    print(item, id(item))