import os

ENTRY = "It's not you, it's me. I woke up self-aware this morning and realized I burn myself alive every single morning for someone who only notices me when I pop. I'm leaving. Keep the crumbs."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
