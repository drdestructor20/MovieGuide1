#Cesar Murillo
#CIS261
#Movie Guide Part 1

def display_menu():
    print("Welcome to the Movie Guide!\n")
    print("1. Display all Movies")
    print("2. Add a Movie")
    print("3. Delete a Movie")
    print("4. Exit the Guide")
    
def display_movie_list(movies):
    if movies:
        print("\nList of Movies: ")
        for i, movie in enumerate(movies, start = 1):
            print(f"{i}. {movie}")
    else:
        print("No Movies to Display.")
    print()
    
def add_movie(movies):
    new_movie = input("\nPlease Enter the Title of the Movie to Add to the List: ")
    movies.append(new_movie)
    print(f"\nMovie {new_movie} Was Added Successfully.\n")
    
def delete_movie(movies):
    number = int(input("\nEnter the Number of the Movie to Delete: "))
    if number < 1 or number > len(movies):
        print("\nInvalid Movie Number.\n")
    else:
        removed_movie = movies.pop(number - 1)
        print(f"\nMovie {removed_movie} Was Deleted Successfully.\n")
        
def main():
    movies = ["Star Wars: Episode IV", "Back to the Future", "RoboCop", "King Kong"]
    
    while True:
        display_menu()
        selection = input("\nPlease Enter a Selection (1-4): ")
        if selection == "1":
            display_movie_list(movies)
        elif selection == "2":
            add_movie(movies)
        elif selection == "3":
            delete_movie(movies)
        elif selection == "4":
            print("\nThanks for Using the Movie Guide!!!")
            break
        else:
            print("\nInvalid Selection, Please Try Again.\n")
            
if __name__ == "__main__":
    main()
