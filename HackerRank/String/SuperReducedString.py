def super_reduced_string(s):
    res = bytearray(s, "utf-8")
    n = res.__len__()
    i = 0
    while(i<res.__len__()-1):
        if(res[i] == res[i+1]):
            del res[i]
            del res[i]
            i = 0
        else:
            i = i + 1

    if(res.decode("utf-8") == ""):
        return "Empty String"
    else:
        return str(res.decode("utf-8"))

s = input().strip()
result = super_reduced_string(s)
print(result)
