from bs4 import BeautifulSoup
import re
import os
import sys

def generate_markdown_links(output_file=None):
    """Generate markdown links from leetcode.xml file"""
    
    # Check if leetcode.xml exists
    xml_path = os.path.join(os.path.dirname(__file__), 'leetcode.xml')
    if not os.path.exists(xml_path):
        print("Error: leetcode.xml file not found!")
        return
    
    try:
        # Read the leetcode.xml file
        with open(xml_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        soup = BeautifulSoup(html_content, "html.parser")
        rows = soup.find_all("tr")
        
        markdown_links = []
        for row in rows:
            cells = row.find_all("td")
            if len(cells) >= 6:
                problem_cell = cells[2]
                solution_cell = cells[5]

                a_tag_problem = problem_cell.find("a")
                a_tag_solution = solution_cell.find("a")
                if a_tag_problem and a_tag_solution:
                    problem_name = a_tag_problem.text.strip()
                    problem_url = a_tag_problem.get("href")
                    solution_url = a_tag_solution.get("href")

                    markdown_key = re.sub(r'\s+', ' ', problem_name.strip())
                    markdown_links.append(f"[{markdown_key}]: {problem_url}")
                    markdown_links.append(f"[{markdown_key} Solution]: {solution_url}")
        
        # Remove duplicates and sort
        markdown_links = sorted(set(markdown_links))
        
        # Print all markdown links
        print(f"Generated {len(markdown_links)} markdown links:")
        print("-" * 50)
        for link in markdown_links:
            print(link)
        
        # Save to file if specified or ask user
        if output_file:
            filename = output_file
        else:
            save_to_file = input("\nSave to file? (y/n): ").lower().strip()
            if save_to_file == 'y':
                filename = input("Enter filename (default: markdown_links.txt): ").strip()
                if not filename:
                    filename = "markdown_links.txt"
            else:
                filename = None
        
        if filename:
            with open(filename, 'w', encoding='utf-8') as f:
                for link in markdown_links:
                    f.write(link + '\n')
            print(f"Links saved to {filename}")
            
    except Exception as e:
        print(f"Error processing leetcode.xml: {e}")

if __name__ == "__main__":
    # Check for command line arguments
    output_file = None
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-h', '--help']:
            print("Usage: python3 gen_markdown_links.py [output_file]")
            print("")
            print("Generate markdown links from leetcode.xml file")
            print("")
            print("Arguments:")
            print("  output_file    Optional. Save output to this file instead of prompting")
            print("")
            print("Examples:")
            print("  python3 gen_markdown_links.py")
            print("  python3 gen_markdown_links.py links.txt")
            sys.exit(0)
        else:
            output_file = sys.argv[1]
    
    generate_markdown_links(output_file)
