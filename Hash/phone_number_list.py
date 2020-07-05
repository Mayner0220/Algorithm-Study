def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

phone_book1 = ["119", "97674223", "1195524421"]
phone_book2 = ["123", "456", "789"]
phone_book3 = ["12" , "123" , "1235", "567", "88"]

print(solution(phone_book1))
print(solution(phone_book2))
print(solution(phone_book3))