from typing import List


def as_string(file_path: str, separator=",") -> str:
    env_vars = _load_env_file(file_path)
    return separator.join(env_vars)


def as_list(file_path: str) -> List[str]:
    return _load_env_file(file_path)


def _load_env_file(file_path: str) -> List[str]:
    try:
        with open(file_path) as file:
            lines = file.readlines()

        env_vars = [
            line.strip() for line in lines if line.strip() and not line.startswith("#")
        ]
        return env_vars
    except FileNotFoundError:
        raise (
            f"File {file_path} was not found, please create it, file name can be set using env variable AWS_ENV_FILE."
        )


if __name__ == "__main__":
    pass
