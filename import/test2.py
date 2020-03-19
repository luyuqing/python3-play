from test1 import Some

s = Some()

print(s.interface)
print(s._internal)  # protected attr, can access but practice be refrained
print(s._Some__private)  # private attr, name mangling, can acess but practice be most refrained
