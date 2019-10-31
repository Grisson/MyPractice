class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        dirc = [p for p in path.split("/") if p != "." and p != ""]
        stack = []
        for name in dirc:
            if name == "..":
                if stack:
                    stack.pop()
            else:
                stack.append("/" + name)
        
        return "".join(stack) if stack else "/"
                