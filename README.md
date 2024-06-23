                                                      

# CONTACTS MANAGEMENT SYSTEM

- This program was built to help organize contacts.

- This program was a weekend assignment from the Coding Temple Backend-Core Coursework

- The intent of this program is to enhance our skills using regex, dictionaries and with file handling

## HOW TO USE

-Once You have cloned the repository onto your local machine as well as the backup file,
Open the app in the repository it was cloned into.
 
 - It will pull up the menu options for the driver code in your CLI.
 - Optionally You may start by pressing '9' to restore the contacts from the preloaded contacts backup
that has several contacts of fictional characters.
 - or you may manually add any contacts you wish using the '1' input, Make sure the formatting matches
  The directions given in the CLI as to how input should be formatted
  (Note: if you do not add any contacts to the program, much of the functionality will not be accesible)
 - Once you have contacts loaded into your dictionary you are now capable of running the program
 
 - You may:
 
 - 1. Add contacts
 - 2. Edit existing contacts
 - 3. Delete a contact
 - 4. Search for a contact by any property of said contact
 - 5. Display All contacts by 3 Filters
        - 1. By groups
        - 2. Alphabetically By Name
        - 3. Alphabetically by Email
 - 6. Export All contacts to a file
 - 7. Import Contacts from a file (Note: To properly import contacts from a file they have to match the format given)
 - 8. Backup contacts to the backup file, or if you feel so inclined you may change the file in the source code
 - 9. Restore Contacts from the backup file
 - 10. Quit the program


### INSTALLATION

To install and run the CONTACTS MANAGEMENT SYSTEM, please follow these steps:

1. **Prerequisites**
   - Ensure you have Git installed on your machine. You can download it from [git-scm.com](https://git-scm.com/).
   - Make sure you have Python installed. This project requires Python 3.6 or later. You can download Python from [python.org](https://www.python.org/).

2. **Clone the Repository**
   - Open your terminal.
   - Navigate to the directory where you want to clone the project.
   - Run the following command to clone the repository:
     ```
     git clone https://github.com/your-username/CONTACTS-MANAGEMENT-SYSTEM.git
     ```
   - Replace `your-username` with the username of the repository owner if you're cloning directly from the original repository.

3. **Navigate to the Project Directory**
   - After cloning, move into the project directory:
     ```
     cd CONTACTS-MANAGEMENT-SYSTEM
     ```

4. **Install Dependencies**
   - This project may require additional libraries or dependencies. Install them using pip:
     ```
     pip install -r requirements.txt
     ```
   - This command reads the `requirements.txt` file in the project directory and installs all the libraries listed there.

5. **Run the Application**
   - Once the dependencies are installed, you can run the application using Python:
     ```
     python app.py
     ```
   - Replace `app.py` with the main script of your project if it's named differently.

6. **Accessing the Application**
   
   - This is a command-line application, follow the on-screen instructions to interact with the system.





## Contributing

We welcome contributions to the CONTACTS MANAGEMENT SYSTEM! If you'd like to contribute, please follow these steps to create a pull request:

1. **Fork the Repository**
   - Navigate to the repository on GitHub.
   - In the top-right corner of the page, click the "Fork" button.

2. **Clone the Forked Repository**
   - On your GitHub account, navigate to the forked repository.
   - Above the list of files, click the "Code" button.
   - Copy the URL for the repository.
   - Open your terminal.
   - Change the current working directory to the location where you want the cloned directory.
   - Type `git clone`, and then paste the URL you copied earlier. It will look something like this:
     ```
     git clone https://github.com/your-username/CONTACTS-MANAGEMENT-SYSTEM.git
     ```
   - Press Enter to create your local clone.

3. **Create a New Branch**
   - Navigate into the cloned repository directory:
     ```
     cd CONTACTS-MANAGEMENT-SYSTEM
     ```
   - Now, create a new branch using the `git checkout` command:
     ```
     git checkout -b your-new-branch-name
     ```

4. **Make Your Changes**
   - Open the project in your preferred editor.
   - Make your changes to the code or documentation. Please ensure you follow the project's coding conventions and documentation style.

5. **Commit Your Changes**
   - After making changes, stage them using:
     ```
     git add .
     ```
   - Commit the changes with a meaningful commit message:
     ```
     git commit -m "A brief description of your changes"
     ```

6. **Push Changes to GitHub**
   - Push your changes using the command:
     ```
     git push origin your-new-branch-name
     ```

7. **Create a Pull Request**
   - Go to your forked repository on GitHub.
   - Click the "Pull request" button.
   - Click the "New pull request" button.
   - Choose your branch and then click "Create pull request".
   - Add any additional comments about your changes.
   - Click "Create pull request" again.

After you submit your pull request, one of our project maintainers will review your changes. We may request further changes or merge your contribution if everything looks good. Thank you for contributing!