print("🎸 Welcome to Chord Explorer!")
print("Discover notes and chord vibes.\n")

chord = input("Enter a chord: ")

chords = {
    "C": "C Major", "Cm": "C Minor", "C7": "C7",
    "C#": "C# Major", "C#m": "C# Minor", "C#7": "C#7",
    "D": "D Major", "Dm": "D Minor", "D7": "D7",
    "D#": "D# Major", "D#m": "D# Minor", "D#7": "D#7",
    "E": "E Major", "Em": "E Minor", "E7": "E7",
    "F": "F Major", "Fm": "F Minor", "F7": "F7",
    "F#": "F# Major", "F#m": "F# Minor", "F#7": "F#7",
    "G": "G Major", "Gm": "G Minor", "G7": "G7",
    "G#": "G# Major", "G#m": "G# Minor", "G#7": "G#7",
    "A": "A Major", "Am": "A Minor", "A7": "A7",
    "A#": "A# Major", "A#m": "A# Minor", "A#7": "A#7",
    "B": "B Major", "Bm": "B Minor", "B7": "B7"
}

chord_notes = {
    "C Major": "C, E, G", "C Minor": "C, Eb, G", "C7": "C, E, G, Bb",
    "C# Major": "C#, F, G#", "C# Minor": "C#, E, G#", "C#7": "C#, F, G#, B",
    "D Major": "D, F#, A", "D Minor": "D, F, A", "D7": "D, F#, A, C",
    "D# Major": "D#, G, A#", "D# Minor": "D#, F#, A#", "D#7": "D#, G, A#, C#",
    "E Major": "E, G#, B", "E Minor": "E, G, B", "E7": "E, G#, B, D",
    "F Major": "F, A, C", "F Minor": "F, Ab, C", "F7": "F, A, C, Eb",
    "F# Major": "F#, A#, C#", "F# Minor": "F#, A, C#", "F#7": "F#, A#, C#, E",
    "G Major": "G, B, D", "G Minor": "G, Bb, D", "G7": "G, B, D, F",
    "G# Major": "G#, C, D#", "G# Minor": "G#, B, D#", "G#7": "G#, C, D#, F#",
    "A Major": "A, C#, E", "A Minor": "A, C, E", "A7": "A, C#, E, G",
    "A# Major": "A#, D, F", "A# Minor": "A#, C#, F", "A#7": "A#, D, F, G#",
    "B Major": "B, D#, F#", "B Minor": "B, D, F#", "B7": "B, D#, F#, A"
}

chord_progressions = {
    "🔆  Bright": [
        ["C", "F", "G", "C"],
        ["G", "C", "D", "G"],
        ["A", "D", "E", "A"],
        ["D", "G", "A", "D"],
        ["F", "C", "G", "F"],
        ["C", "G", "Am", "F"],
        ["G", "D", "Em", "C"]
    ],
    "🥀  Sad": [
        ["Am", "Em", "Dm", "Am"],
        ["Dm", "Gm", "Am", "Dm"],
        ["Em", "Bm", "C", "Em"],
        ["Cm", "Gm", "Fm", "Cm"],
        ["Fm", "Cm", "D#", "Fm"],
        ["Am", "Dm", "E7", "Am"],
        ["Em", "Am", "Bm", "Em"]
    ],
    "⁉️  Suspenseful": [
        ["Cm", "G#", "F", "Cm"],
        ["D#m", "A#", "F#", "D#m"],
        ["Fm", "C#", "G#", "Fm"],
        ["Gm", "D#", "A#", "Gm"],
        ["C#m", "G#", "F#", "C#m"],
        ["Am", "F", "E7", "Am"]
    ],
    "☁️  Dreamy": [
        ["F", "G", "Am", "F"],
        ["C", "Em", "F", "G"],
        ["Dm", "G", "C", "Am"],
        ["Am", "F", "C", "G"],
        ["C", "F", "Dm", "G"],
        ["Em", "Am", "F", "G"],
        ["F", "Dm", "G", "C"]
    ],
    "💞  Romantic": [
        ["C", "Am", "F", "G"],
        ["G", "Em", "C", "D"],
        ["F", "Dm", "Gm", "C"],
        ["Am", "F", "C", "G"],
        ["Dm", "G", "C", "Am"],
        ["C", "G", "Am", "Em"],
        ["F", "C", "Dm", "G"]
    ],
    "💢  Raw & Aggressive": [
        ["E", "G", "A", "B"],
        ["F#", "B", "C#", "F#"],
        ["G#", "D#", "A#", "G#"],
        ["C", "G", "F", "C"],
        ["D", "A", "G", "D"],
        ["A", "E", "D", "A"],
        ["B", "F#", "E", "B"]
    ],
    "‼️  Dramatic": [
        ["Cm", "G", "A#", "Fm"],
        ["D#m", "A#", "C#", "G#"],
        ["Fm", "C", "D#", "G#"],
        ["Am", "F", "G", "Em"],
        ["Em", "C", "D", "Bm"],
        ["Gm", "D#", "A#", "F"],
        ["C#m", "A", "B", "E"]
    ]
}

if chord in chords:
    full_name = chords[chord]
    notes = chord_notes.get(full_name, "Unknown notes")
    print(f"\nYour chord: {full_name} 🎶")
    print(f"Notes in {full_name}: {notes}\n")

    full_to_short = {
        "C Major": "C", "C Minor": "Cm", "C7": "C7",
        "C# Major": "C#", "C# Minor": "C#m", "C#7": "C#7",
        "D Major": "D", "D Minor": "Dm", "D7": "D7",
        "D# Major": "D#", "D# Minor": "D#m", "D#7": "D#7",
        "E Major": "E", "E Minor": "Em", "E7": "E7",
        "F Major": "F", "F Minor": "Fm", "F7": "F7",
        "F# Major": "F#", "F# Minor": "F#m", "F#7": "F#7",
        "G Major": "G", "G Minor": "Gm", "G7": "G7",
        "G# Major": "G#", "G# Minor": "G#m", "G#7": "G#7",
        "A Major": "A", "A Minor": "Am", "A7": "A7",
        "A# Major": "A#", "A# Minor": "A#m", "A#7": "A#7",
        "B Major": "B", "B Minor": "Bm", "B7": "B7"
    }

    chord_symbol = full_to_short.get(full_name, full_name)

    found = False
    for emotion, progressions_list in chord_progressions.items():
        filtered = [progression for progression in progressions_list if chord_symbol in progression]
        if filtered:
            found = True
            print(f"{emotion} Progressions:")
            for progression in filtered:
                print(" - " + " - ".join(progression))
            print()

    if not found:
        print("Sorry, couldn't find a progression with that chord. 😅")
else:
    print("\nSorry, I don't know that chord yet. 😅")
