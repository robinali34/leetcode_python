#!/usr/bin/env python3
"""
Generate a complete README table with all LeetCode problems and proper links
"""

from bs4 import BeautifulSoup
import re
import os

def generate_readme_table():
    """Generate complete README table from leetcode.xml"""
    
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
            difficulty = cells[1].text.strip()
            problem_name = cells[2].find('a').text.strip()
            problem_url = cells[2].find('a').get('href')
            solution_url = cells[5].find('a').get('href')
            
            problems.append({
                'idx': idx,
                'difficulty': difficulty,
                'name': problem_name,
                'problem_url': problem_url,
                'solution_url': solution_url
            })
    
    # Sort by idx
    problems.sort(key=lambda x: x['idx'])
    
    # Generate table
    table_lines = []
    table_lines.append("| Idx | ID    | [Google top questions]                                           | Difficulty | Wiki | Solution                                                  |")
    table_lines.append("|-----|-------|------------------------------------------------------------------|------------|------|-----------------------------------------------------------|")
    
    for p in problems:
        # Format difficulty with proper capitalization
        difficulty_formatted = p['difficulty'].capitalize()
        
        # Truncate long problem names to fit in table
        name = p['name']
        if len(name) > 50:
            name = name[:47] + "..."
        
        # Create the table row with proper spacing
        row = f"| {p['idx']:3d} | {p['idx']:3d} | [{name}]({p['problem_url']}) | {difficulty_formatted:10s} |      | [{name} Solution]({p['solution_url']}) |"
        table_lines.append(row)
    
    return '\n'.join(table_lines)

if __name__ == "__main__":
    table = generate_readme_table()
    print(table)
