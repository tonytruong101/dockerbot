import fnmatch

def validate_version(version, exact_match=False):
    if exact_match:
        valid_versions = [f"{i}.*.*" for i in range(1, 100)]
        valid_versions += [f"{i}.{j}.*" for i in range(1, 100) for j in range(1, 100)]
        valid_versions += [f"{i}.{j}.{k}" for i in range(1, 100) for j in range(1, 100) for k in range(1, 100)]
    else:
        valid_versions = [f"{i}" for i in range(1, 100)]
        valid_versions += [f"{i}.{j}" for i in range(1, 100) for j in range(1, 100)]
        valid_versions += [f"{i}.{j}.*" for i in range(1, 100) for j in range(1, 100)]

    while not any(fnmatch.fnmatch(version, v) for v in valid_versions):
        version = input(f"Invalid input. Please enter a valid option from the list ({', '.join(valid_versions)}): ")
    return version

