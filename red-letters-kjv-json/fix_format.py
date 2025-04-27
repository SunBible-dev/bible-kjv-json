import json

def fix_revelation_format():
    # Read the original files
    with open('revelation-red-letter.json', 'r') as f:
        rev_data = json.load(f)
    with open('revelation-red-letter-ids.json', 'r') as f:
        rev_ids = json.load(f)
    
    # Create new structure
    new_rev = {"Revelation": []}
    new_rev_ids = {"Revelation": []}
    
    # Convert each chapter
    for chapter_num in rev_data:
        chapter_data = {
            "chapter": chapter_num,
            "verses": []
        }
        chapter_ids = {
            "chapter": chapter_num,
            "verses": []
        }
        
        # Add verses
        for verse in rev_data[chapter_num]:
            verse_data = {
                "verse": verse["verse"],
                "red_words": verse["text"]
            }
            chapter_data["verses"].append(verse_data)
            
            # Find corresponding IDs
            if chapter_num in rev_ids and any(v["verse"] == verse["verse"] for v in rev_ids[chapter_num]):
                verse_id = next(v["word_ids"] for v in rev_ids[chapter_num] if v["verse"] == verse["verse"])
                verse_ids = {
                    "verse": verse["verse"],
                    "word_ids": verse_id
                }
                chapter_ids["verses"].append(verse_ids)
        
        new_rev["Revelation"].append(chapter_data)
        if chapter_ids["verses"]:  # Only add chapters that have verses with IDs
            new_rev_ids["Revelation"].append(chapter_ids)
    
    # Save the new files
    with open('revelation-red-letter.json', 'w') as f:
        json.dump(new_rev, f, indent=2)
    with open('revelation-red-letter-ids.json', 'w') as f:
        json.dump(new_rev_ids, f, indent=2)

def fix_corinthians_format():
    # The 1 Corinthians files are already in the correct format
    # Just need to standardize the key name from "red_words" to match IDs file
    with open('1Corinthians-red-letter.json', 'r') as f:
        cor_data = json.load(f)
    
    # No changes needed as it's already in the correct format
    with open('1Corinthians-red-letter.json', 'w') as f:
        json.dump(cor_data, f, indent=2)

if __name__ == "__main__":
    fix_revelation_format()
    fix_corinthians_format()