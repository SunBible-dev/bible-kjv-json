import json
import os

def count_words(text):
    return len(text.split())

def process_book(book_path):
    with open(book_path, 'r') as f:
        book_data = json.load(f)
    
    book_name = book_data['book']
    chapters = book_data['chapters']
    verse_counts = []
    total_words = 0
    
    for chapter in chapters:
        verse_count = len(chapter['verses'])
        verse_counts.append(verse_count)
        
        # Count words in each verse
        for verse in chapter['verses']:
            total_words += count_words(verse['text'])
    
    return {
        'name': book_name,
        'chapters': len(chapters),
        'verses': verse_counts,
        'word_count': total_words
    }

def generate_contents():
    # Read Books.json to get the correct order
    with open('json/Books.json', 'r') as f:
        book_order = json.load(f)
    
    contents = {'books': []}
    
    for index, book_name in enumerate(book_order, 1):
        # Handle special case for Song of Solomon
        if book_name == 'Song of Solomon':
            filename = 'SongofSolomon.json'
        else:
            filename = f'{book_name.replace(" ", "")}.json'
        
        book_path = os.path.join('json', filename)
        book_data = process_book(book_path)
        
        # Add book ID and data to contents
        book_entry = {
            'id': f'b{index}',
            'name': book_name,
            'chapters': book_data['chapters'],
            'verses': book_data['verses'],
            'word_count': book_data['word_count']
        }
        contents['books'].append(book_entry)
    
    # Write the contents to a JSON file
    with open('contents.json', 'w') as f:
        json.dump(contents, f, indent=2)

if __name__ == '__main__':
    generate_contents()