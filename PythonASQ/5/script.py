def funk2():
    from module import funk 
    funk()
    
funk2()
# funk is not defined in the current scope
# its probably very rarely useful to import inside a function (as it obfuscates code quite a bit)
# it might be useful if the import takes a long time and the function is only rarely called
funk()

    