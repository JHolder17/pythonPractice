num = 123456789
def descending_order(num):
    # Bust a move right here
    num = [char for char in str(num)]
    num.sort(reverse=True)
    num = int("".join(num))
descending_order(123456789)