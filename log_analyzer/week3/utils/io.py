def read_lines(path: str) ->list[str]:
    list=[]
    try:
        with open(path, 'r') as file:
            for line in file:
                line.rstrip('\n')
                list.append(line)
        return list
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
    