class MyQueue:
    """方針
    FIFOの構造にするには、stackを二つ用意すればいい。

    あるstack①について、先頭行を取り出したい場合
    1. 一度stack①が空になるまでpopを行い、
    2. popされた値をstack②にpushしていく。するとstackに積まれたデータの順序が逆になる
        e.g.) [0, 1, 2, 3] -> [3, 2, 1, 0]
    3. stack②をpopし、返り値に設定する。
    4. stack②を空になるまでpopし、popされる値をstack①にpushしていく
    """

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        while(self.stack_1):
            self.stack_2.append(self.stack_1.pop())
        val = self.stack_2.pop()
        while(self.stack_2):
            self.stack_1.append(self.stack_2.pop())
        return val

    def peek(self) -> int:
        # 基本はpopと同じ構造だが、popされた値が消えないように帳尻を合わせる
        while(self.stack_1):
            self.stack_2.append(self.stack_1.pop())
        val = self.stack_2.pop()
        self.stack_1.append(val)
        while(self.stack_2):
            self.stack_1.append(self.stack_2.pop())
        return val

    def empty(self) -> bool:
        if(self.stack_1):
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
