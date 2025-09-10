#!/usr/bin/env python3
"""
Update leetcode.xml with all problems from src directory
"""

import os
import re
from bs4 import BeautifulSoup

def get_problem_name_from_path(path):
    """Extract problem name from file path"""
    # Extract directory name from path like src/easy/two_sum/solution.py
    parts = path.split('/')
    if len(parts) >= 3:
        return parts[2]  # e.g., 'two_sum'
    return None

def convert_to_problem_name(directory_name):
    """Convert directory name to proper problem name"""
    # Convert snake_case to Title Case
    words = directory_name.split('_')
    title_case = ' '.join(word.capitalize() for word in words)
    
    # Handle special cases
    special_cases = {
        '3_sum': '3Sum',
        '3_sum_closest': '3Sum Closest',
        '3_sum_ii': '3Sum II',
        'basic_calculator_II': 'Basic Calculator II',
        'binary_search_tree_iterator': 'Binary Search Tree Iterator',
        'binary_tree_level_order_traversal': 'Binary Tree Level Order Traversal',
        'combination_sum': 'Combination Sum',
        'combination_sum_ii': 'Combination Sum II',
        'combination_sum_II': 'Combination Sum II',
        'combination_sum_iii': 'Combination Sum III',
        'combination_sum_III': 'Combination Sum III',
        'container_with_most_water': 'Container With Most Water',
        'course_schedule': 'Course Schedule',
        'delete_and_earn': 'Delete and Earn',
        'diameter_of_binary_tree': 'Diameter of Binary Tree',
        'fibonacci_number': 'Fibonacci Number',
        'find_all_anagrams_in_a_string': 'Find All Anagrams in a String',
        'find_first_and_last_position_of_element_in_sorted_array': 'Find First and Last Position of Element in Sorted Array',
        'find_minimum_in_rotated_sorted_array_ii': 'Find Minimum in Rotated Sorted Array II',
        'find_minimum_in_rotated_sorted_array_II': 'Find Minimum in Rotated Sorted Array II',
        'first_bad_version': 'First Bad Version',
        'generate_parentheses': 'Generate Parentheses',
        'get_equal_substring_within_budget': 'Get Equal Substrings Within Budget',
        'group_anagrams': 'Group Anagrams',
        'grumpy_bookstore_owner': 'Grumpy Bookstore Owner',
        'house_robber': 'House Robber',
        'house_robberii': 'House Robber II',
        'house_robberII': 'House Robber II',
        'invert_binary_tree': 'Invert Binary Tree',
        'ktn_smallest_element_in_a_bst': 'Kth Smallest Element in a BST',
        'letter_case_permutation': 'Letter Case Permutation',
        'letter_combination_of_a_phone_number': 'Letter Combinations of a Phone Number',
        'linked_list_cycle': 'Linked List Cycle',
        'longest_substring_with_at_most_two_distinct_characters': 'Longest Substring with At Most Two Distinct Characters',
        'longest_substring_without_repeating_characters': 'Longest Substring Without Repeating Characters',
        'lowest_common_ancestor_of_a_binary_tree': 'Lowest Common Ancestor of a Binary Tree',
        'lru_cache': 'LRU Cache',
        'max_consecutive_onesii': 'Max Consecutive Ones II',
        'max_consecutive_onesII': 'Max Consecutive Ones II',
        'max_difference_you_can_get_from_changing_a_integer': 'Max Difference You Can Get From Changing an Integer',
        'maximum_average_subarrayi': 'Maximum Average Subarray I',
        'maximum_average_subarrayI': 'Maximum Average Subarray I',
        'maximum_depth_of_binary_tree': 'Maximum Depth of Binary Tree',
        'maximum_erasure_value': 'Maximum Erasure Value',
        'maximum_points_you_can_obtain_from_cards': 'Maximum Points You Can Obtain from Cards',
        'merge_two_sorted_lists': 'Merge Two Sorted Lists',
        'min_cost_climbing_stairs': 'Min Cost Climbing Stairs',
        'min_stack': 'Min Stack',
        'minimum_number_of_days_to_make_m_bouquets': 'Minimum Number of Days to Make m Bouquets',
        'minimum_size_subarray_sum': 'Minimum Size Subarray Sum',
        'minimum_swaps_to_group_all_1s_together': 'Minimum Swaps to Group All 1\'s Together',
        'minimum_window_substring': 'Minimum Window Substring',
        'minimum_with_substring': 'Minimum Window Substring',
        'missing_element_in_sorted_array': 'Missing Element in Sorted Array',
        'move_zeroes': 'Move Zeroes',
        'n_queens': 'N-Queens',
        'nth_tribonacci_number': 'Nth Tribonacci Number',
        'number_of_islands': 'Number of Islands',
        'palindrome_partitioning': 'Palindrome Partitioning',
        'parsing_a_boolean_expression': 'Parsing a Boolean Expression',
        'permutations': 'Permutations',
        'permutations_ii': 'Permutations II',
        'permutations_II': 'Permutations II',
        'premutation_in_string': 'Permutation in String',
        'product_of_array_except_self': 'Product of Array Except Self',
        'remove_duplicates_from_sorted_array': 'Remove Duplicates from Sorted Array',
        'remove_element': 'Remove Element',
        'reverse_linked_list': 'Reverse Linked List',
        'rotate_array': 'Rotate Array',
        'same_tree': 'Same Tree',
        'search_a_2d_matrix': 'Search a 2D Matrix',
        'search_in_a_binary_search_tree': 'Search in a Binary Search Tree',
        'search_in_rotated_sorted_array_ii': 'Search in Rotated Sorted Array II',
        'search_in_rotated_sorted_array_II': 'Search in Rotated Sorted Array II',
        'search_in_rotated-sorted_array': 'Search in Rotated Sorted Array',
        'simplify_path': 'Simplify Path',
        'single_number': 'Single Number',
        'single_number_ii': 'Single Number II',
        'single_number_II': 'Single Number II',
        'single_number_iii': 'Single Number III',
        'single_number_III': 'Single Number III',
        'sliding_window_maximum': 'Sliding Window Maximum',
        'sqrtx_x': 'Sqrt(x)',
        'subarray_sum_equals_k': 'Subarray Sum Equals K',
        'subset': 'Subsets',
        'subset_ii': 'Subsets II',
        'subset_II': 'Subsets II',
        'sudoku_solver': 'Sudoku Solver',
        'trapping_rain_water': 'Trapping Rain Water',
        'two_sum': 'Two Sum',
        'two_sumii': 'Two Sum II - Input array is sorted',
        'two_sumII': 'Two Sum II - Input array is sorted',
        'valid_anagram': 'Valid Anagram',
        'valid_palindrome': 'Valid Palindrome',
        'valid_parentheses': 'Valid Parentheses',
        'validate_binary_search_tree': 'Validate Binary Search Tree',
        'word_search': 'Word Search',
        'best_time_to_buy_and_sell_stock': 'Best Time to Buy and Sell Stock',
        'best_time_to_buy_and_sell_stock_ii': 'Best Time to Buy and Sell Stock II',
        'binary_search': 'Binary Search',
        'climbing_stairs': 'Climbing Stairs',
        'final_price_with_a_special_discount_in_a_shop': 'Final Price With a Special Discount in a Shop'
    }
    
    return special_cases.get(directory_name, title_case)

def get_leetcode_id_mapping():
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
        "Palindrome Partitioning": 131,
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
        "Sliding Window Maximum": 239,
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
        "Search in a Binary Search Tree": 700,
        "Binary Search": 704,
        "Delete and Earn": 740,
        "Min Cost Climbing Stairs": 746,
        "Letter Case Permutation": 784,
        "Grumpy Bookstore Owner": 1052,
        "Missing Element in Sorted Array": 1060,
        "Parsing a Boolean Expression": 1106,
        "Nth Tribonacci Number": 1137,
        "Minimum Swaps to Group All 1's Together": 1151,
        "Get Equal Substrings Within Budget": 1208,
        "Maximum Points You Can Obtain from Cards": 1423,
        "Max Difference You Can Get From Changing an Integer": 1432,
        "Final Price With a Special Discount in a Shop": 1473,
        "Minimum Number of Days to Make m Bouquets": 1482,
        "Maximum Erasure Value": 1695,
    }

def get_leetcode_url(problem_name):
    """Generate LeetCode URL from problem name"""
    # Convert to URL format
    url_name = problem_name.lower()
    url_name = re.sub(r'[^a-z0-9\s-]', '', url_name)
    url_name = re.sub(r'\s+', '-', url_name)
    return f"https://leetcode.com/problems/{url_name}/"

def get_solution_url(problem_path):
    """Generate GitHub solution URL from problem path"""
    return f"https://github.com/robinali34/leetcode_python/blob/main/{problem_path}"

def get_difficulty_from_path(path):
    """Extract difficulty from path"""
    if '/easy/' in path:
        return 'Easy'
    elif '/medium/' in path:
        return 'Medium'
    elif '/hard/' in path:
        return 'Hard'
    return 'Unknown'

def scan_src_directory():
    """Scan src directory for all problems"""
    problems = []
    src_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src')
    leetcode_id_mapping = get_leetcode_id_mapping()
    
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file == 'solution.py':
                rel_path = os.path.relpath(os.path.join(root, file), os.path.dirname(os.path.dirname(__file__)))
                directory_name = get_problem_name_from_path(rel_path)
                if directory_name:
                    problem_name = convert_to_problem_name(directory_name)
                    difficulty = get_difficulty_from_path(rel_path)
                    leetcode_url = get_leetcode_url(problem_name)
                    solution_url = get_solution_url(rel_path)
                    leetcode_id = leetcode_id_mapping.get(problem_name, 9999)
                    
                    problems.append({
                        'directory_name': directory_name,
                        'problem_name': problem_name,
                        'difficulty': difficulty,
                        'leetcode_url': leetcode_url,
                        'solution_url': solution_url,
                        'path': rel_path,
                        'leetcode_id': leetcode_id
                    })
    
    return sorted(problems, key=lambda x: x['leetcode_id'])

def update_leetcode_xml():
    """Update leetcode.xml with all problems from src directory"""
    problems = scan_src_directory()
    
    # Create HTML table
    html_content = """<table border="1" cellpadding="5" cellspacing="0">
  <thead>
    <tr>
      <th>idx</th>
      <th>leetcode_id</th>
      <th>Problem Name</th>
      <th>Difficulty</th>
      <th>LeetCode URL</th>
      <th>Solution URL</th>
    </tr>
  </thead>
  <tbody>
"""
    
    for i, problem in enumerate(problems, 1):
        html_content += f"""    <tr>
      <td>{i}</td>
      <td>{problem['leetcode_id']}</td>
      <td><a href="{problem['leetcode_url']}">{problem['problem_name']}</a></td>
      <td>{problem['difficulty'].lower()}</td>
      <td><a href="{problem['leetcode_url']}">LeetCode Link</a></td>
      <td><a href="{problem['solution_url']}">Solution</a></td>
    </tr>
"""
    
    html_content += """  </tbody>
</table>"""
    
    # Write to leetcode.xml
    xml_path = os.path.join(os.path.dirname(__file__), 'leetcode.xml')
    with open(xml_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Updated leetcode.xml with {len(problems)} problems")
    return problems

if __name__ == "__main__":
    problems = update_leetcode_xml()
    print(f"Found {len(problems)} problems in src directory")
