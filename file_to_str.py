def file_to_str(filename) -> str:
    with open(filename, "r") as f:
        return f.read()
