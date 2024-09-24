class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # simplest solution by leveraging python built-ins
        # return bin(int(a, 2) + int(b, 2))[2:]

        # iterate from the last digit
        indexA = len(a) - 1
        indexB = len(b) - 1
        carry = 0 # 進位
        result = ""
        
        while indexA >= 0 or indexB >= 0 or carry != 0:
            valueA = int(a[indexA]) if indexA >= 0 else 0
            valueB = int(b[indexB]) if indexB >= 0 else 0
            
            sum_ = valueA + valueB + carry
            carry = sum_ // 2
            result = str(sum_ % 2) + result
            
            indexA -= 1
            indexB -= 1
        
        return result
