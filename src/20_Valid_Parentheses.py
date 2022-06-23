class Solution:
    def isValid(self, s: str) -> bool:
        """方針
        ①個数があってること
        後述するようにstackを利用するが、ループを最後まで回し終わったあと、stackに文字が残っていれば
        ②stackを利用する
        ( [ { が渡されたらstackに文字列を積んでいく。
        ) ] } が渡されたらstackからpopしていく。
        この際、stackの一番上の文字に対応するカッコであるかを検査し、ダメだったらその時点でearly returnでfalseを返す
        """
        stack: list = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            elif s[i] == ")":
                # 整合性の検査
                if len(stack) == 0:
                    return False
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif s[i] == "}":
                # 整合性の検査
                if len(stack) == 0:
                    return False
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif s[i] == "]":
                # 整合性の検査
                if len(stack) == 0:
                    return False
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                # illegal character
                return False
        if len(stack) == 0:
            return True
        return False
