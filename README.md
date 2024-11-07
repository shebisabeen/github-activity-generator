# github-activity-generator
Python script that can generate GitHub activity to make your profile contributions graph more colorful.



# To use this script:
1. Install Python and Git in your system.
2. Create an Empty GitHub Repository.
3. Give your repository a name, choose whether it should be public or private, but do not select any options to initialize it (like “Add a README file,” “Add .gitignore,” or “Choose a license”).
4. Download the script `github_activity_generator.py`
5. Update the git configuration in the script with your name and email
6. Run the script: `python github_activity_generator.py`
7. Create a new repository on GitHub
8. Follow the printed instructions to push the changes

# The script does the following:

- Creates a git repository if one doesn't exist
- Generates commits for random days over the past year
- Each day has a 70% chance of getting 2-12 commits (you can adjust this by changing the `frequency` parameter)
- Creates commits with random times during working hours (9 AM - 6 PM)
- Creates a dummy file with random content for each commit

# **Important Notes:**
1. This is meant for educational purposes
2. Make sure to use this responsibly
3. Some might consider this gaming the system, so use it wisely
4. GitHub's terms of service should be considered

You can customize the script by:
- Adjusting the date range
- Changing the frequency of commits
- Modifying the number of commits per day
- Changing the time range for commits

---
**Remember to replace the git configuration with your actual GitHub email and name before running the script.**
---