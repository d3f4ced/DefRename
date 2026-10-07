from pathlib import Path
import secrets
import string

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".bmp",
    ".tiff",
    ".tif",
    ".ico"
}

def generate_random_name(length: int = 10) -> str:
    characters = string.ascii_lowercase + string.digits
    random_part = "".join(secrets.choice(characters) for _ in range(length))

    return f"def-{random_part}"

def rename_images() -> None:
    current_folder = Path.cwd()

    print(f"[+] Folder: {current_folder}\n")

    renamed = 0

    for file in current_folder.iterdir():
        if not file.is_file():
            continue

        extension = file.suffix.lower()

        if extension not in IMAGE_EXTENSIONS:
            continue

        while True:
            new_name = f"{generate_random_name()}{extension}"
            new_path = current_folder / new_name

            if not new_path.exists():
                break

        try:
            old_name = file.name
            file.rename(new_path)

            renamed = 1
            print(f"[+] {old_name} -> {new_name}")

        except OSError as error:
            print(f"[-] Error renaming {file.name} : {error}")

    print(f"\n[+] Finished. {renamed} image(s) renamed.")
    input("\nPress ENTER to exit...")


if __name__ == "__main__":
    rename_images()