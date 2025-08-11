'''Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird'''

def test(n):
    if n % 2 != 0:
        print("Weird")
    elif (n % 2 == 0) and (2 <= n <= 5):
        print("Not Weird")
    elif (n % 2 == 0) and (6 <= n <= 20):
        print("Weird")
    elif (n % 2 == 0) and (n > 20):
        print("Not Weird")

if __name__ == '__main__':
    n = int(input(). strip())
    test(n)



'''# সংখ্যার ধরন চেক করার ফাংশন
def test(n):
    # যদি সংখ্যা বিজোড় হয়
    if n % 2 != 0:
        print("Weird")
    # যদি সংখ্যা জোড় হয় এবং 2 থেকে 5 এর মধ্যে হয়
    elif (n % 2 == 0) and (2 <= n <= 5):
        print("Not Weird")
    # যদি সংখ্যা জোড় হয় এবং 6 থেকে 20 এর মধ্যে হয়
    elif (n % 2 == 0) and (6 <= n <= 20):
        print("Weird")
    # যদি সংখ্যা জোড় হয় এবং 20 এর বেশি হয়
    elif (n % 2 == 0) and (n > 20):
        print("Not Weird")


# প্রোগ্রামের মূল অংশ
if __name__ == '__main__':
    # ব্যবহারকারীর কাছ থেকে সংখ্যা ইনপুট নেওয়া
    n = int(input("একটা সংখ্যা লিখুন: ").strip())

    # test() ফাংশনে ইনপুট পাঠিয়ে ফলাফল দেখানো
    test(n)
'''