#!/usr/bin/env python3
"""
Fix README table with correct LeetCode problem IDs
"""

from bs4 import BeautifulSoup
import re
import os

def get_correct_leetcode_ids():
    """Get the correct LeetCode problem IDs"""
    return {
        "Two Sum": 1,
        "Longest Substring Without Repeating Characters": 3,
        "Median of Two Sorted Arrays": 4,
        "Container With Most Water": 11,
        "3Sum": 15,
        "3Sum Closest": 16,
        "Letter Combinations of a Phone Number": 17,
        "Valid Parentheses": 20,
        "Merge Two Sorted Lists": 21,
        "Generate Parentheses": 22,
        "Remove Duplicates from Sorted Array": 26,
        "Remove Element": 27,
        "Search in Rotated Sorted Array": 33,
        "Find First and Last Position of Element in Sorted Array": 34,
        "Search Insert Position": 35,
        "Sudoku Solver": 37,
        "Combination Sum": 39,
        "Combination Sum II": 40,
        "Trapping Rain Water": 42,
        "Permutations": 46,
        "Permutations II": 47,
        "Group Anagrams": 49,
        "N-Queens": 51,
        "Sqrt(x)": 69,
        "Climbing Stairs": 70,
        "Simplify Path": 71,
        "Search a 2D Matrix": 74,
        "Minimum Window Substring": 76,
        "Subsets": 78,
        "Word Search": 79,
        "Search in Rotated Sorted Array II": 81,
        "Subsets II": 90,
        "Validate Binary Search Tree": 98,
        "Same Tree": 100,
        "Binary Tree Level Order Traversal": 102,
        "Maximum Depth of Binary Tree": 104,
        "Best Time to Buy and Sell Stock": 121,
        "Best Time to Buy and Sell Stock II": 122,
        "Valid Palindrome": 125,
        "Single Number": 136,
        "Single Number II": 137,
        "Linked List Cycle": 141,
        "LRU Cache": 146,
        "Find Minimum in Rotated Sorted Array II": 154,
        "Min Stack": 155,
        "Longest Substring with At Most Two Distinct Characters": 159,
        "Two Sum II - Input array is sorted": 167,
        "Binary Search Tree Iterator": 173,
        "Rotate Array": 189,
        "House Robber": 198,
        "Number of Islands": 200,
        "Reverse Linked List": 206,
        "Course Schedule": 207,
        "Minimum Size Subarray Sum": 209,
        "House Robber II": 213,
        "Combination Sum III": 216,
        "Invert Binary Tree": 226,
        "Basic Calculator II": 227,
        "Kth Smallest Element in a BST": 230,
        "Lowest Common Ancestor of a Binary Tree": 236,
        "Product of Array Except Self": 238,
        "Valid Anagram": 242,
        "Single Number III": 260,
        "First Bad Version": 278,
        "Move Zeroes": 283,
        "Word Pattern": 290,
        "Valid Perfect Square": 367,
        "Find All Anagrams in a String": 438,
        "Max Consecutive Ones II": 487,
        "Fibonacci Number": 509,
        "Diameter of Binary Tree": 543,
        "Subarray Sum Equals K": 560,
        "Permutation in String": 567,
        "Maximum Average Subarray I": 643,
        "Binary Search": 704,
        "Search in a Binary Search Tree": 700,
        "Delete and Earn": 740,
        "Min Cost Climbing Stairs": 746,
        "Letter Case Permutation": 784,
        "Missing Element in Sorted Array": 1060,
        "Nth Tribonacci Number": 1137,
        "Minimum Swaps to Group All 1's Together": 1151,
        "Get Equal Substrings Within Budget": 1208,
        "Palindrome Partitioning": 131,
        "Maximum Points You Can Obtain from Cards": 1423,
        "Final Price With a Special Discount in a Shop": 1473,
        "Minimum Number of Days to Make m Bouquets": 1482,
        "Maximum Erasure Value": 1695,
        "Maximum Difference You Can Get From Changing an Integer": 1432,
        "Grumpy Bookstore Owner": 1052,
        "Sliding Window Maximum": 239,
        "Parsing a Boolean Expression": 1106
    }

def generate_corrected_table():
    """Generate table with correct LeetCode IDs"""
    
    # Read leetcode.xml
    xml_path = os.path.join(os.path.dirname(__file__), 'leetcode.xml')
    with open(xml_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    rows = soup.find_all('tr')[1:]  # Skip header
    
    # Get correct ID mapping
    id_mapping = get_correct_leetcode_ids()
    
    problems = []
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 6:
            idx = int(cells[0].text.strip())
            difficulty = cells[1].text.strip()
            problem_name = cells[2].find('a').text.strip()
            problem_url = cells[2].find('a').get('href')
            solution_url = cells[5].find('a').get('href')
            
            # Get correct LeetCode ID
            leetcode_id = id_mapping.get(problem_name, 9999)
            
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
    
    # Generate table
    table_lines = []
    table_lines.append("| Idx | ID    | Problem Name                                           | Difficulty | Wiki | Solution                                                  |")
    table_lines.append("|-----|-------|--------------------------------------------------------|------------|------|-----------------------------------------------------------|")
    
    for i, p in enumerate(problems, 1):
        difficulty_formatted = p['difficulty'].capitalize()
        name = p['name']
        if len(name) > 40:
            name = name[:37] + "..."
        
        row = f"| {i:3d} | {p['leetcode_id']:3d} | [{name}]({p['problem_url']}) | {difficulty_formatted:10s} |      | [Solution]({p['solution_url']}) |"
        table_lines.append(row)
    
    return '\n'.join(table_lines)

def update_readme():
    """Update README with corrected table"""
    # Get the parent directory (one level up from tools/)
    parent_dir = os.path.dirname(os.path.dirname(__file__))
    readme_path = os.path.join(parent_dir, 'README.md')
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    table_start = content.find('| Idx |')
    table_end = content.find('\n\n[3Sum Closest Solution]:')
    
    new_table = generate_corrected_table()
    new_content = content[:table_start] + new_table + content[table_end:]
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("README updated with correct LeetCode IDs!")

if __name__ == "__main__":
    update_readme()
