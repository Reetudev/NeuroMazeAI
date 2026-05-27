import random

hints = [
    "🧠 Look carefully at the hidden pattern.",
    "🎯 Sometimes the smallest clue matters.",
    "🚪 The answer may be connected to AI.",
    "🔮 Think futuristic.",
    "⚡ Observe the glowing symbols."
]

def get_hint():
    return random.choice(hints)