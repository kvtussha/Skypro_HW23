def tools(file, cmd, value):
    if cmd == 'filter':
        return list(filter(lambda line: value in line, file))
    elif cmd == 'map':
        return list(map(lambda line: line.split()[int(value)], file))
    elif cmd == 'unique':
        return iter(set(file))
    elif cmd == 'limit':
        return file[:int(value)]
    elif cmd == 'sort':
        return sorted(file, reverse=(value == 'desc'))
