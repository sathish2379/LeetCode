'''
6. Zigzag Conversion
Medium Hard

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if num_rows == 1:
        #     return s

        # n = len(s)
        # sections = ceil(n / (2 * num_rows - 2.0))
        # num_cols = sections * (num_rows - 1)

        # matrix = [[" "] * num_cols for _ in range(num_rows)]

        # curr_row, curr_col = 0, 0
        # curr_string_index = 0

        # while curr_string_index < n:
        #     while curr_row < num_rows and curr_string_index < n:
        #         matrix[curr_row][curr_col] = s[curr_string_index]
        #         curr_row += 1
        #         curr_string_index += 1

        #     curr_row -= 2
        #     curr_col += 1

        #     while (
        #         curr_row > 0 and curr_col < num_cols and curr_string_index < n
        #     ):
        #         matrix[curr_row][curr_col] = s[curr_string_index]
        #         curr_row -= 1
        #         curr_col += 1
        #         curr_string_index += 1

        # answer = ""
        # for row in matrix:
        #     answer += "".join(row)

        # return answer.replace(" ", "")

        if numRows == 1 or numRows >= len(s):
            return s
    
        rows = [''] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char
            if current_row == 0:
                going_down = True
            elif current_row == numRows - 1:
                going_down = False

            current_row += 1 if going_down else -1

        return ''.join(rows)


        