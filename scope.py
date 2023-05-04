# This area is the global or module scope
number = 100

def outer_func():
    number = 200
    print(f"Outer Function: {number}")
     # This block is the local scope of outer_func()
     # It's also the enclosing scope of inner_func()
    def inner_func():
        # This block is the local scope of inner_func()
        number = 400
        print(f"Inner Function {number}")
inner_func()

print(f"Global Scope:{number}")
outer_func()