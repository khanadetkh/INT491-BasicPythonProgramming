import mymoduel
mymoduel.add(2,3)

import mymoduel as m 
m.add(7,3)

from mymoduel import add
add(5,6)

from mymoduel import MyClass
obj = MyClass("Harry")
obj.my_function()