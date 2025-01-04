import requests # we have to install module that is not pre defined in python for this we have to run pip install module name it will installed automatically

# Function to get user details from GitHub API
def get_user_details(username):
    url = f'https://api.github.com/users/{username}'
    
    # Send a GET request to GitHub API
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        user_data = response.json()
        print(f"User: {user_data['login']}")
        print(f"Name: {user_data['name']}")
        print(f"Bio: {user_data['bio']}")
        print(f"Location: {user_data['location']}")
        print(f"Public Repositories: {user_data['public_repos']}")
    else:
        print("User not found or there was an error.")

# Function to get repository details from GitHub API
def get_user_repositories(username):
    url = f'https://api.github.com/users/{username}/repos'
    
    # Send a GET request to GitHub API
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        repos_data = response.json()
        if len(repos_data) > 0:
            print(f"\nRepositories of {username}:")
            for repo in repos_data:
                print(f"Name: {repo['name']}")
                print(f"Description: {repo['description']}")
                print(f"Stars: {repo['stargazers_count']}")
                print("-" * 40)
        else:
            print(f"No repositories found for {username}.")
    else:
        print("Error fetching repositories.")

# Main function to ask user input and call the functions
def main():
    username = input("Enter the GitHub username: ")
    get_user_details(username)
    get_user_repositories(username)

# Run the program
if __name__ == "__main__":
    main()
