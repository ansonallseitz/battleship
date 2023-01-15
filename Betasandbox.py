

squares=[]
for i in range(1, 101):
    squares.append(i**2)

print(squares)


squares2 = [i**2 for i in range(1, 101)]

remainders5 = [x**2 for x in range(1,101)]

movies = ["The Shawshank Redemption", "The Godfather", "Pulp Fiction", "Inception", "The Lord of the Rings", "Ghostbusters"]


gmovies = [title for title in movies if title.startswith("G")]

print(gmovies)