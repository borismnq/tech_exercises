def calculate_happiness(base_array, set_a, set_b):
    happiness = 0
    for element in base_array:
        if element in set_a:
            happiness+=1
        elif element in set_b:
            happiness-=1
    return happiness


def start():
    n_m_values = list(map(int,input().split()))
    if len(n_m_values)!=2:
        print("Error: Please enter just 2 sizes (array_size, set_size)")
        exit()
    n = n_m_values[0]
    m = n_m_values[1]

    base_array = list(map(int,input().split()))
    if n!=len(base_array):
        print("Error: Array size doesn't match")
        exit()
    set_a = set(map(int,input().split()))
    set_b = set(map(int,input().split()))
    if m!= len(set_a) or m!= len(set_b):
        print(len(set_a))
        print(len(set_b))
        print("Error, Sets size doesn't match")
        exit()

    happiness = calculate_happiness(base_array, set_a, set_b)
    print(happiness)

start()