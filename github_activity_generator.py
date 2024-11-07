import os
import datetime
from random import randint
import subprocess

def create_commit(date):
    # Create a dummy file with random content
    with open('dummy.txt', 'w') as file:
        file.write(str(randint(1, 1000)))
    
    # Set environment variables for the commit date
    os.environ['GIT_AUTHOR_DATE'] = date.strftime('%Y-%m-%d %H:%M:%S')
    os.environ['GIT_COMMITTER_DATE'] = date.strftime('%Y-%m-%d %H:%M:%S')
    
    # Stage and commit the file
    subprocess.call(['git', 'add', 'dummy.txt'])
    subprocess.call(['git', 'commit', '-m', f'Activity for {date.strftime("%Y-%m-%d")}'])

def generate_activity(start_date, end_date, frequency=0.7):
    current_date = start_date
    while current_date <= end_date:
        # Randomly decide whether to create a commit for this day
        if randint(1, 100) <= frequency * 100:
            # Create 2-12 commits for this day
            num_commits = randint(2, 12)
            for _ in range(num_commits):
                # Set random time for each commit
                hour = randint(9, 18)
                minute = randint(0, 59)
                commit_date = datetime.datetime(
                    current_date.year,
                    current_date.month,
                    current_date.day,
                    hour,
                    minute
                )
                create_commit(commit_date)
        
        current_date += datetime.timedelta(days=1)

def main():
    # Initialize git repository if not already initialized
    if not os.path.exists('.git'):
        subprocess.call(['git', 'init'])
    
    # Set git configuration
    subprocess.call(['git', 'config', 'user.name', 'Your Name'])
    subprocess.call(['git', 'config', 'user.email', 'your.email@example.com'])
    
    # Set date range for activity generation
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=365)  # Last 365 days
    
    # Generate activity
    generate_activity(start_date, end_date)
    
    print("Activity generation completed!")
    print("Don't forget to:")
    print("1. Create a new repository on GitHub")
    print("2. Add remote: git remote add origin <your-repo-url>")
    print("3. Push changes: git push -u origin master")

if __name__ == "__main__":
    main()