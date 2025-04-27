# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


The function `parse_music` will take a string representing music notes and durations and parse it into a list of tuples where each tuple contains a note and its corresponding duration. Here is the complete Python function:

```python
def parse_music(music_string):
    notes = []
    current_note = ""
    current_duration = ""
    
    for char in music_string:
        if char.isalpha():
            current_note += char
        elif char.isdigit():
            current_duration += char
        elif char == ',':
            if current_note and current_duration:
                notes.append((current_note, int(current_duration)))
                current_note = ""
                current_duration = ""
    
    if current_note and current_duration:
        notes.append((current_note, int(current_duration)))
    
    return notes

# Example usage
music_string = "C4, D8, E16, F32"
parsed_music = parse_music(music_string)
print(parsed_music)
```

This function will parse the input music string "C4, D8, E16, F32" into a list of tuples `parsed_music` where each tuple contains a note and its corresponding duration. The output of the example usage will be `[('C', 4), ('D', 8), ('E', 16), ('F', 32)]`.