# Sallam is a young student who has been learning how to read numbers for a while. now Sllam can read numbers forward but he can't read numbers backward. Sallam is now playing a game, in order to move to the next level, the game gives him a number and wants him to enter the backward version of the given number. Unfortunately, Sallam has not learned to read the numbers backward, so he wants you to write the reversed version of the number (without leading zeros) so that he can read it and pass the level.
# A leading zero is any 0 digit that comes before the first nonzero digit in a number.
#REVERSE the STRING
n = input()
reverse = n[::-1]
start=0
while reverse[start] =='0':
    start+=1
reverse = reverse[start:]
#https://reactgo.com/python-get-first-character-of-string/
print(reverse)