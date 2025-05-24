import random

def get_styles():
    return {
        "Empathetic": [
            "I understand where you're coming from, but",
            "Let's try to look at this differently.",
            "I get your frustration, here's another view:"
        ],
        "Professional": [
            "Kindly note that",
            "It would be more effective if",
            "Let's aim for a respectful conversation:"
        ],
        "Funny": [
            "Let's not turn into internet warriors 😄",
            "No need to roast — we’re on the same team!",
            "Whoa, that escalated! Here’s a chill version:"
        ]
    }

def detoxify(sentence, style="Empathetic"):
    polite_intro = random.choice(get_styles()[style])
    core_rewrite = "Let’s try to keep it respectful. What you're saying is valid, but harsh."
    return f"{polite_intro} {core_rewrite}"
