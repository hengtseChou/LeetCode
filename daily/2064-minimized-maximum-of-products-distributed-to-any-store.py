class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def canDistribute(max_products):
            stores_needed = 0
            # Iterate through each quantity of products
            for quantity in quantities:
                # Calculate the number of stores required for this product type
                # if each store can have at most 'max_products'.
                # (quantity + max_products - 1) // max_products is equivalent to
                # math.ceil(quantity / max_products), ensuring we round up to
                # account for any remainder (if quantity is not perfectly divisible).
                stores_needed += (quantity + max_products - 1) // max_products
            # Return True if the total number of stores needed is less than or
            # equal to 'n', meaning the distribution is feasible.
            return stores_needed <= n

        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid
            else:
                left = mid + 1

        return left
