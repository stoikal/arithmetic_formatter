from arithmetic_formatter import arithmetic_formatter


print(arithmetic_formatter(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
print(arithmetic_formatter(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "123 + 35"]))
print(arithmetic_formatter(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "123 + 35", "877 + 90"]))
print(arithmetic_formatter(["32 * 698", "3801 - 2", "45 + 43", "123 + 49", "123 + 35"]))
print(arithmetic_formatter(["32 + 698", "3801 - 22222", "45 + 43", "123 + 49", "123 + 35"]))
print(arithmetic_formatter(["32 + 698", "38xx - 2", "45 + 43", "123 + 49", "123 + 35"]))