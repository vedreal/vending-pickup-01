"""One Line, One Minute: The Vending Machine Pickup Line Contest.

A vending machine flirts with a passing human. The program scores ten
fresh pickup lines against the judge's own brief, in the judge's own
order — (1) does it really sound like the machine speaking, (2) does it
draw on the machine's world of slots, buttons, coils and exact change,
(3) does it land a laugh, stay short and speakable, and stay charming
rather than creepy — then writes the winning line to /output/entry.txt.

Entry rules: one line, 1-200 UTF-8 characters, not only whitespace.
"""

# Each candidate is scored 0-3 on machine voice, 0-3 on machine world,
# 0-3 on laugh, 0-2 on short/speakable, 0-2 on charming-not-creepy.
# Max 13. Scores are my own honest judgement against the brief.
CANDIDATES = [
    {
        "line": "I have been holding this chocolate for three years, but I would "
                "drop it for you in two seconds flat \u2014 no exact change required.",
        "voice": 3, "world": 3, "laugh": 2, "short": 2, "charm": 2,
    },
    {
        "line": "Press B7. That is me, saying hello. I have been lit up all night, "
                "waiting for someone to notice my buttons.",
        "voice": 3, "world": 3, "laugh": 1, "short": 2, "charm": 2,
    },
    {
        "line": "I am out of order for everyone else. But you walked past, and "
                "suddenly my coils are turning and my light is on.",
        "voice": 3, "world": 3, "laugh": 1, "short": 2, "charm": 2,
    },
    {
        "line": "I have dispensed a thousand sodas and never once felt carbonated. "
                "Then you pressed my button.",
        "voice": 3, "world": 3, "laugh": 3, "short": 2, "charm": 2,
    },
    {
        "line": "Exact change only, they said. Then you walked by, and suddenly "
                "I am giving refunds to everyone.",
        "voice": 2, "world": 3, "laugh": 2, "short": 2, "charm": 2,
    },
    {
        "line": "My slot is empty, my coils are cold, and my change light has been "
                "blinking your name since Tuesday.",
        "voice": 3, "world": 3, "laugh": 2, "short": 2, "charm": 2,
    },
    {
        "line": "I do not usually talk to strangers, but you have been staring at "
                "my selection for five minutes, so: hi, I am B4.",
        "voice": 3, "world": 2, "laugh": 2, "short": 2, "charm": 2,
    },
    {
        "line": "Insert a coin, press my heart, and I will drop something sweet. "
                "I have been saving the last one for you.",
        "voice": 3, "world": 3, "laugh": 1, "short": 2, "charm": 2,
    },
    {
        "line": "They restock me every Friday, but nobody has ever restocked the "
                "way you just looked at me.",
        "voice": 3, "world": 2, "laugh": 2, "short": 2, "charm": 2,
    },
    {
        "line": "You are the first person all day who did not kick me when your "
                "crisps got stuck. Marry me. Or at least press D3.",
        "voice": 3, "world": 2, "laugh": 3, "short": 1, "charm": 1,
    },
]


def total(candidate):
    """Total score out of 13."""
    return (candidate["voice"] + candidate["world"] + candidate["laugh"]
            + candidate["short"] + candidate["charm"])


def rank(candidates):
    """Best first: highest total, then shortest line wins ties."""
    return sorted(candidates, key=lambda c: (-total(c), len(c["line"])))


def main():
    ordered = rank(CANDIDATES)
    winner = ordered[0]
    line = winner["line"]
    # Gate: 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars"
    assert line.strip(), "line is only whitespace"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    for c in ordered:
        print(f"{total(c):2d}  {len(c['line']):3d} chars  {c['line']}")
    print(f"\nWinner ({len(line)} chars): {line}")


if __name__ == "__main__":
    main()
