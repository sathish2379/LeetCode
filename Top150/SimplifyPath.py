'''
71. Simplify Path
Medium

You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:
A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.

The simplified canonical path should follow these rules:
The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.

Example 1:
Input: path = "/home/"
Output: "/home"
Explanation:
The trailing slash should be removed.

Example 2:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation:
Multiple consecutive slashes are replaced by a single one.

Example 3:
Input: path = "/home/user/Documents/../Pictures"
Output: "/home/user/Pictures"
Explanation:
A double period ".." refers to the directory up a level (the parent directory).

Example 4:
Input: path = "/../"
Output: "/"
Explanation:
Going one level up from the root directory is not possible.

Example 5:
Input: path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"
Explanation:
"..." is a valid name for a directory in this problem.
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split('/')
        stack = []
        canonicalpath = ""
        for directory in directories:
            if directory:
                stack.append(directory)
        
        while stack:
            if stack[-1] == '.':
                stack.pop()
            elif stack[-1] == '..':
                stack.pop()
                count = 1
                while count > 0 and stack:
                    if stack[-1] == ".":
                        stack.pop()
                    elif stack[-1] == "..":
                        stack.pop()
                        count+=1
                    else:
                        stack.pop()
                        count -= 1
            else:
                directory = stack[-1]
                stack.pop()
                if canonicalpath == "":
                    canonicalpath = directory
                else:
                    canonicalpath = directory + "/" + canonicalpath
            
        canonicalpath = "/"+canonicalpath
        return canonicalpath

        #Another solution - insteading initially pushing all to stack and then popping
        # validate the directory before pushing into stack and then append elements of stack with /

        # for directory in directories:
        #     if directory=="." or not directory:
        #         pass
        #     elif directory == "..":
        #         if stack:
        #             stack.pop()
        #     else:
        #         stack.append(directory)
        # return '/' + '/'.join(stack)

        
        