'''dictonary = {"Book":5,"Pen":10,"Pencil":7}
d=dictonary.copy()
print(d)
#fromkey
ak = dict.fromkeys(["Bookk","Penn","Bottle","Etc"],5)
print(ak)
d = {"a": 1, "b": 2}
print(d.get(1))
     
print(d.get("c", 0))    # 0
print(d.items())
print(d.popitem())'''
d = {"a": 1}
print(d.setdefault("a",5))
print(d.setdefault("z",5))
print(d)
print("Z" in d)

            


