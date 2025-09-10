#!/usr/bin/env python3
"""
Update README.md with complete table from leetcode.xml
"""

from bs4 import BeautifulSoup
import re
import os

def generate_compact_table():
    """Generate compact README table from leetcode.xml"""
    
    # Read leetcode.xml
    xml_path = os.path.join(os.path.dirname(__file__), 'leetcode.xml')
    with open(xml_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    rows = soup.find_all('tr')[1:]  # Skip header
    
    problems = []
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 6:
            idx = int(cells[0].text.strip())
            leetcode_id = int(cells[1].text.strip())  # Get LeetCode ID from XML
            difficulty = cells[3].text.strip()  # Difficulty is now in column 3
            problem_name = cells[2].find('a').text.strip()
            problem_url = cells[2].find('a').get('href')
            solution_url = cells[5].find('a').get('href')
            
            problems.append({
                'idx': idx,
                'leetcode_id': leetcode_id,
                'difficulty': difficulty,
                'name': problem_name,
                'problem_url': problem_url,
                'solution_url': solution_url
            })
    
    # Sort by LeetCode ID
    problems.sort(key=lambda x: x['leetcode_id'])
    
    # Generate compact table
    table_lines = []
    table_lines.append("| Idx | ID    | Problem Name                                           | Difficulty | Wiki | Solution                                                  |")
    table_lines.append("|-----|-------|--------------------------------------------------------|------------|------|-----------------------------------------------------------|")
    
    for i, p in enumerate(problems, 1):
        # Format difficulty with proper capitalization
        difficulty_formatted = p['difficulty'].capitalize()
        
        # Truncate long problem names to fit in table
        name = p['name']
        if len(name) > 40:
            name = name[:37] + "..."
        
        # Create the table row
        row = f"| {i:3d} | {p['leetcode_id']:3d} | [{name}]({p['problem_url']}) | {difficulty_formatted:10s} |      | [Solution]({p['solution_url']}) |"
        table_lines.append(row)
    
    return '\n'.join(table_lines)

def update_readme():
    """Update README.md with new table"""
    
    # Get the parent directory (one level up from tools/)
    parent_dir = os.path.dirname(os.path.dirname(__file__))
    readme_path = os.path.join(parent_dir, 'README.md')
    
    # Read current README
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the table section (from | Idx | to the end of table)
    table_start = content.find('| Idx |')
    if table_start == -1:
        print("Could not find table start")
        return
    
    # Find the end of the table (before the markdown links section)
    table_end = content.find('\n\n[3Sum Closest Solution]:')
    if table_end == -1:
        print("Could not find table end")
        return
    
    # Generate new table
    new_table = generate_compact_table()
    
    # Replace the table section
    new_content = content[:table_start] + new_table + content[table_end:]
    
    # Write updated README
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("README.md updated successfully!")

if __name__ == "__main__":
    update_readme()
