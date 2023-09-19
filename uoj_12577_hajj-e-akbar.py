# Tedious

counter = 1

while True:
    try: 
        s = input()
    except EOFError:
        break

    match s:
        case "*":
            break
        case "Hajj":
            print(f"Case {counter}: Hajj-e-Akbar")
        case "Umrah":
            print(f"Case {counter}: Hajj-e-Asghar")
        
    counter +=1

    
    
