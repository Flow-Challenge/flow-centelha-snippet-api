from decouple import config


def get_key_from_env(key: str) -> str:
    return config(key)


def get_key_from_env_with_default(key: str, default: str) -> str:
    return config(key, default)


if __name__ == "__main__":
    print(get_key_from_env("KEY"))