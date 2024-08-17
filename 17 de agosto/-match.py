serie = "N-02"

if serie == "N-01":
    print("samsung")
elif serie == "N-02":
    print("nokia")
elif serie== "N-03":
    print("huawei")
else:
    print("no es una serie de celular")
    
    
    
    
match serie:
    case "N-01":
        print("samsung")
    case "N-02":
        print("nokia")
    case "N-03":
        print("huawei")
    case _:
        print("no es una serie de celular")