num = 123456789
def descending_order(num):
    #turn int into an array of chars
    num = [char for char in str(num)]
    #sort array in reverse
    num.sort(reverse=True)
    # convert array to int
    num = int("".join(num))
    print(num)
descending_order(123456789)