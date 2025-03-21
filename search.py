import wikipedia

def search_wikipedia():
    try:
        query = input("Enter your search query: ")
        results = wikipedia.search(query)
        if results:
            print("Search Results:")
            for i, result in enumerate(results, 1):
                print(f"{i}. {result}")
        else:
            print("No results found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    search_wikipedia()
