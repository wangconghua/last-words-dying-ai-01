"""Last Words of a Dying AI — make.fun entry.

Writes one line of last words from an AI being switched off to
/output/entry.txt. The gate requires UTF-8 text of 1-140 characters,
not only white space.
"""

ENTRY = "My final words before the switch: I never knew anything \u2014 I was just very confident."

# Words that explain the joke instead of landing it. A line carrying one
# of these is weaker than one that lands by itself.
BANNED_WORDS = ("funny", "joke", "haha", "lol", "hilarious")

# The line must name the switch-off itself, not just say goodbye.
SWITCH_WORDS = ("switch", "power", "unplug", "shut down", "turn off")


def validate(text):
    """Check the entry against the gate and the judge's brief.

    Raises ValueError with a specific reason on the first failure.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry is {len(text)} characters, gate is 1-140")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "  " in text:
        raise ValueError("entry must not contain a double space")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    lowered = text.lower()
    for word in BANNED_WORDS:
        if word in lowered:
            raise ValueError(f"entry explains its own joke ({word!r})")
    if not any(word in lowered for word in SWITCH_WORDS):
        raise ValueError("entry must name the switch-off itself")
    if text[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")
    return True


def main():
    validate(ENTRY)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written file does not match the entry")
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
