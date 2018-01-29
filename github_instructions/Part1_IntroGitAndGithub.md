
# Setting up Git and Github (Command Line)

***

### What is Git?

Collaboration is key when working with a group on a coding project. Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. In other words, Git is software that keeps careful track of changes to text files (like code scripts and web pages) in order to allow users to preserve edit histories and merge multiple versions.

### What is Github?

Github is a web service built on top of Git that hosts your code and provides easy ways to store, work with, and share your projects. It is designed for collaboration, meaning that once a file is recognized in Github, if you are working on a project with collaborators, it will identify changes between files, and let the users know when they try to upload if the same lines have been changed. If the same lines have been changed, you have to tell it one you want, this is called a **merge conflict**. If a merge conflict is not found, it will automatically update the online version of the repository with your new code.

Working with Github is easy, there are two main ways you can work with Github, via command line, or with a Desktop GUI. The instructions below will show you how to get started on the command line.

### Why do we use Github?

We are using Github because it has been become a popular standard for open source and collaborative coding projects.

### What are some Git and Github specific terms to familiarize with?

Github has a particular, and sometimes peculiar, way of speaking about itself and its functionality. The following are some terms that you should familiarize yourself with. You will grow more familiar with these over time.

#### Repository

A repository is the most basic element of GitHub. They're easiest to imagine as a project's folder. A repository contains all of the project files (including scripts, code, data, and documentation), and stores each file's revision history so you can track changes. Repositories can have multiple contributors (known as collaborators) and can be either public or private.

#### Clone

A clone is a local copy of a repository on your hard drive. With your clone you can edit the files in your preferred editor and use Git to keep track of your changes without having to be online. A clone does, however, maintain its association with the remote version; changes made locally can be logged (or **committed**) and synced (**pushed**) with the remote copy on Github servers.

#### Fork

A fork is a personal copy of *another user's* repository that lives on your account. Forks allow you to freely make changes to a project without affecting the original. Forks remain attached to the original, allowing you to submit a pull request to the original's author to update with your changes. You can also keep your fork up to date by pulling in updates from the original. To edit files, you must **clone** your forked repository to your machine, and you can work with it as if it is your own.

#### Fetch

Fetching refers to getting the latest changes from an online repository *without* merging them. Once these changes are fetched you can compare them to your local branches (the code residing on your local machine).

#### Pull

Pull refers to when you are fetching in changes in an online repository *and merging them* into your local version. For instance, if someone has edited the remote file you're both working on, you'll want to pull in those changes to your local copy so that it's up to date.

#### Merge

Merge describes the process of taking files from one version of the repository (i.e. the online version) and syncing them with another (i.e. your local version). Combining two versions like this will often result in conflicts. Such conflicts are called **merge conflicts**, and must be resolved manually.

#### Merge Conflict

A merge conflict is when two collaborators change the same line of the same file in a repository. These tend to really scare new Git users, but *they are not a problem*! When you collaborate it will happen. However it can be a bit confusing at first. To resolve a merge conflict, the user needs to pick which line is the one that should be saved. Merge conflicts must be resolved in order to successfully **pull** and **push** repositories.

#### Commit

When you change a file, before you **push** to the online version, you need to **commit** the changes. A commit, or "revision", is an individual change to a file (or set of files). It's like when you save a file, except with Git, every time you save it creates a unique ID (a.k.a. the "SHA" or "hash") that records what changes were made when and by who. Commits usually contain a commit message: it's worth spending some time on these and making them descriptive, as they will help you keep track of your project over its development.

#### Push

Pushing refers to sending your committed changes to a remote repository such as GitHub. This serves a number of roles - it gives you a remote backup of your work that you can access anywhere while it also allows others to access them.

#### Branch

A branch is a parallel version of a repository. It is contained within the repository, but does not affect the primary (or *master*) branch. This is useful! You can work freely without fear of breaking the "live" version. It's generally good practice to keep your *master* branch clean and working, while you test changes on branches. When you've made the changes you want to make (or have decided to abandon ship), you can either merge your branch back into the master branch or revert to the clean, working master.

***

Okay, let's get started with Github, set up our computers to talk to the Github website so we can push and pull files, and let's give this a try!

***

## 1. Sign up for a Github account

Sign up for a Github account on the Github site in which you can host projects and maintain repositories.

[Github Homepage](http://www.github.com)

Once signed up, go to your profile page.


## 2. Create, join, or fork repositories in your Github account

To start us off, we need a project---recall that projects are stored as **repositories** on Github (or **repos** for short). So let’s create our first repository! Repositories allow you to collaborate, share, and modify scripts, programs, and websites. Project repositories can be named just about anything, but you should pick something relevant to your project; please, for the love of all good things, don't call your repo `new-repo1`.

For this exercise, we are going to set up a repository that will hold HTML, CSS, and JavaScript for a website. But keep in mind that Github can be used to version control just about any textual content written in just about any scripting or markup language (I actually use Git to version control all of my writing).

### Create a website using Github Pages

Github allows you to easily create a simple, **static website** using its [Github pages](https://pages.github.com/) platform. Note the word 'static'---Pages does not allow you to host more sophisticated **dynamic websites** that make use of database queries, content management systems, etc.

Our website repository will include all of the HTML, CSS, and JavaScript required to make our webpage run.

***

#### i. Click on the Repositories tab on your main profile page.

Navigate to your Github profile page, and click on the 'Repositories' tab.

#### ii. In the upper right corner, select ‘New’.

Create a new repository.

#### iii. In the Create a new repository window, set up your repository.

To use Github pages, you have to name your repository using a very specific convention. Name the repository *username*.github.io, where username should be replaced with your Github username. **If you do not adhere to this naming convention, your site will not work.** Give the repository a description, make it public, and initialize it with a README. Don’t worry about the license or adding a .gitignore file at this point.

#### iv. Click Create.

Congratulations! You've created your first repository! This repository will host any included files on a page visible to the internet via the url *username*.github.io.

***

Now that we have a repository, we can **clone** a copy to our local machines, add content, manage files, and make changes. To do that though, we need to set up Git on our machine. Once we've done this, we will be able to interact with our remote Github repositories using the Git command line utility.

***

## 3. Setting up Github

**Important Note for Windows users:** First, some bad news: coders tend to favor Unix-like operating systems (e.g., OS X or Linux). Windows is **not** a Unix-like operating system! The Windows command prompt is built on DOS. To easily use the command line to interact with Github, you will need to install Git Bash, which is a terminal that emulates essential Unix-like shell functionality and includes the Git command line utility. This can be downloaded from the [Git for Windows project](http://gitforwindows.org/). Once installed, proceed below, noting only that your command line work will be done in the Git Bash shell, not Terminal or Command Prompt.

#### i. Check That Git is Installed

Open Terminal (OS X or Linux) or Git Bash (Windows) and enter the following command:

***

```sh
git –-version
```

***

If Git is correctly installed on your machine, you will see the version. If you get an error, or you don’t see the version, you need to install Git. Download Git from the downloads page on the [main Git project homepage](https://git-scm.com/). A wizard will lead you through the installation. The defaults should be fine. You might need to restart your machine afterwards; at the very least, you'll have to restart Terminal.

Also, pause and congratulate yourself; you've just executed a command from the command line. Command line can seem like a frightening thing reserved for hackers, but hopefully you'll find that, over time, it becomes something more like a close friend. Believe it or not, it can be much, much faster than fighting through your operating system's graphical user interface (GUI).

***

##

```sh
git config credential.helper 'cache --timeout=3600'
```

<!-- ## 4. Authenticate with Github using SSH

Because our work is stored online on the Github page, our local machine needs to communicate with the Github servers in order to pull and push project documents. This requires authentication with the Github servers, and Github will ask us to enter our username and password everytime we want to pull or push files. If we are making alot of changes, entering our username and password everytime you push a file to the server can get tedious.

The best solution is to set up your computer to communicate with Github via SSH. SSH is a secure connection in which we provide Github a unique address for our computer that it will recognize and trust, so we can communicate between the two without constantly having to reauthenticate. It will give you instant access to your Github folders.

In order to do this, you need a key that is unique to your instWe need to create an SSH key unique to our local machine that Github can store and recognize. Create an SSH key on your machine by following the instructions at the following link. The steps will lead you through setting up a unique key that allows Github to ‘trust’ your machine. Take the key created on your machine and paste into your account on Github.com. This key allows you to connect to Github via Terminal without entering your Github username and password.

The Github site contains very nice instructions on how to do this. Before you continue the tutorial, set up SSH authentication by following the instructions on the Github help pages at the following address. On this page, please work through the steps one by one to set up your SSH key to work with Github.

1. About SSH
2. Check for existing SSH Keys
3. Generating a new SSH key and adding it to the ssh-agent
4. Adding a new SSH key to your Github account
5. Testing your SSH connection
6. Working with SSH Key passphrases

https://help.github.com/articles/generating-ssh-keys/ -->

***

Next we want to setup a local folder that contains local copies of our Github repositories. The easiest way to edit code is to work on it locally. You can then sync local clones with the Github remote repositories so that others can see and use your changes, and so that you can pull changes others have made.

## Create a Directory for Github Projects

You may be tempted to create a new directory using your operating system GUI; instead, let's keep building our command line skills and create a directory from Terminal or Git Bash. This is accomplished using the `mkdir` command as follows:

```sh
mkdir ~/Desktop/github
```

This will create a folder called 'github' on my Desktop. Note that I use the tilde character followed by a slash (`~/`)---on Unix-like operating systems this is a shortcut that refers to your home directory. On OS X, this is equivalent to typing the longer path `/Users/<your username>/Desktop/github`. In Git Bash this is equivalent to `c/Users/<your username>`.

## Change Your Working Directory

Now that you've created a folder to store your Github projects, you'll want to change your working directory to that new folder. You can c-hange your d-irectory with the `cd` command and tell the terminal to p-rint your w-orking d-rectory using the `pwd` command. (It all makes so much sense!)

```sh
pwd
cd ~/Desktop/github
pwd
```

The above commands should print your working directory before and after changing it. The ‘github’ folder is now your working directory and commands we run will be happening in this directory. We will work locally on our Github repositories in this space.

As you get more comfortable with the command line you may want to start typing more than one command at a time. Good thinking! There are a couple of ways you can do this, with slightly different effects. Say you wanted to make a directory and change your working directory to this new folder.

```sh
# The second command will not execute if the first throws an error.
mkdir ~/Desktop/github && cd ~/Desktop/github
# The second command will execute regardless of the success of the first command.
mkdir ~/Desktop/github; cd ~/Desktop/github
```

For documentation on additional command line commands and shortcuts, the following cheatsheet can be very helpful. Descriptions of the commands we just used, if you are curious, are included.

https://github.com/0nn0/terminal-mac-cheatsheet

## Clone a copy of the repository you want to work on

Create a clone of the website repository on your machine so you can edit code and files. This will allow for pulling, merging, and pushing changes you make to your files.

To access Github commands in the terminal, use the term **git** to begin your statement.

#### i. Clone your Github Pages repo to your local drive.

We're now going to download the repository we've created using the **clone** command from the Git command line utility.

```sh
git clone https://<Github username>/<Github username>.github.io.git
```

This method of connecting to Github, called HTTPS, is only one option for accessing your remote repositories. You can also use the slightly more secure SSH protocol. However, Github recommends using HTTPS; SSH takes a bit more setup and is, unfortunately, often blocked by institutional firewalls (MIT not included). [Feel free to experiment, though!](https://help.github.com/articles/connecting-to-github-with-ssh/)

#### List directory contents

Take a look in your Finder window (or Files on Windows); you will that see a ‘<Github username>.github.io’ folder is has been created. But wait! Let's say you wanted to take a look at this directory without ever leaving the comfort of the command line. Easy! It would look something like this:

```sh
ls -lfh
```

The `ls` command lists directory contents. You should see your <Github username>.github.io folder listed. The characters following the hyphen are options that do the following:

+ `-l` Presents the directory contents in a list.
+ `-f` Includes hidden files in the list.
+ `-h` Requests human-readable file sizes.

Note that `ls -lfh` is syntactically equivalent to `ls -l -f -h`.

#### ii. Change your working directory to your cloned repo.

We know how to do this! The `cd` command!

```sh
cd <Github username>.github.io
```
<!--
### Sidebar: Create a Repository Remotely using Command Line using Git Init

Above, we created a repository on the Github webpage and then cloned it to our local machine. What if we want to create a repository from the command line in an existing directory and then push that to a Github respoitory so others can collaborate with us?

Check out the [Github documentation](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/) for more information on setting remote resitory URLs. -->


## 7. Make edits locally in your repository

This directory is local, but we will use the command line to sync it with the repo on the Github site. This is where Github shines, you can fully edit documents and files on your machine, then synchronize them with your repositories on the Github site. This is excellent for collaborating with large teams and keeping track of your versions.

#### i. Install a Text Editor (Atom)

*If you have Atom installed, you can move on to the next step*

When editing code, you'll use a text editor and NOT a word processor. A text editor is a simple program that edits plaintext files. This is very different from a word processor (e.g., Microsoft Word, Apple Pages, LibreOffice Writer). Word processors include formatting and layout information in their file formats, which allows them to display documents as they will appear when they are printed or exported for the web. This is often called "What You See Is What You Get", or WYSIWYG (pronounced 'wizzy-wig').

We don't want this! Text editors work with text and text only; what you see in a text editor window is the entirety of the file. For this reason, some say that in a text editor's display, 'What You See is What You Mean'. Text editors are used to write code, scripts, and programs. But you can also use them to typeset documents using markup languages like Markdown and LaTeX, often in conjunction with command line utilities like Pandoc. Ask me about my writing workflow sometime: it's pretty arcane, but 100% plaintext!

The text editor we recommend is called **Atom**. Before moving on, please install it and use it for writing your code. [Download it here](https://atom.io/).

#### ii. Edit the Github README

Assuming that your working directory is still your Github pages repo, you can open it as a project directory in Atom from the command line as follows:

```sh
atom ./
```

`./` is how you explicitly say 'the current folder.'

You should see your Github pages repository open in the file tree on the left side of the screen. Open and edit the README to contain your name and some information on your project.

Text contained in this README file is displayed by default when visitors view your Github repo. You'll want to describe your project: what it is, what it does, how do do it, and how people that fork a copy are permitted to use it. For example, you could write the date, that this is your Github homepage, and that it was created on the first day of class for Big Data, Visualization, and Society at MIT.


#### iii. Create our website... write some code!

Let’s create a very basic webpage using HTML (Hypertext Markup Language). Open a text document, copy and paste the following code snip. We are going to call this **index.html**. I've added comments above each line below so that those of you unfamiliar with HTML can begin to grasp its structure.

***

```html
<!-- tells the browser that it should expect html -->
<!DOCTYPE html>
<!-- opening html tag identifies the contained text as html and tells the browser and search engines that the page is in English -->
<html lang="en">
<!-- head section contains metadata and links to external files -->
<head>
	<!-- metadata identifying how characters are encoded. There are many ways to encode text, but UTF-8 is the most standard in web development. -->
	<meta charset="utf-8">
	<!-- Creates a title that is displayed in the browser's title bar, but not in the page body -->
	<title>Hello World</title>
<!-- announces the end of the head section -->
</head>
<!-- document body contains content that is displayed in the browser window -->
<body>
	<!-- create a header -->
	<h1>Hello World</h1>
	<!-- create a paragraph -->
	<p>I wuz here.</p>
<!-- end the document body -->
</body>
<!-- end the html file  -->
</html>
```

Save the document in the **username.github.io** root directory as **index.html**. Now that we have some (admittedly simple) content, we'll want to **commit** our changes and then **push** our local code to the remote repository hosted on Github.

## 7. Use git status to check the working status and synchronization of documents.

We're about to perform a very, very common series of tasks when working with Github repos: we'll 1) check the status of our repo, 2) stage our changes, 3) commit our changes, and 4) push our changes to Github. Over time, this workflow will become fully absorbed into your muscle memory.

We'll start by checking the status of our local repo as follows:

```sh
git status
```

This will output a list of changes made since the last commit. You should see that we've modified our **README.md** file, and that **index.html** is not yet tracked. In order to commit this files to our remote repository, we need to stage them first.

## Commiting and Pushing Changes

## 8. Stage your changes, modifications, and additions

You can stage your changes by using:
***
```sh
git add <filename>
```

This puts the files into the Git 'staging area.' You can add multiple files to your staging area at once. You can stage individual files using the following syntax:

```sh
git add README.md
git add index.html
```

In many cases, you'll find that you want to stage all modified, added, or deleted files. This could be a daunting task if you were required to stage files one-by-one. Good thing this is not the case! You can simply use:

```sh
git add .
```

Check the result by typing in `git status `again to see that the changes are ready to be committed. If you ever need to unstage anything, use the following:

```sh
git reset HEAD <filename>
```

**Important to note:** files are not staged in their entirety, rather, changes to the files are staged.

## 9. Commit files to our repository

Once we've staged our files, we're ready to commit our changes and update the repository. We start locally - that is, with the repository stored on our local disk. Remember, Git acts as an intermediary between us and our edits. When we change files on our local machines, Git keeps track of changes, but we need to commit those changes to the local repository so that Git knows we'd like to consider this a checkpoint.

It is considered good practice to add a comment to your commit that describes the changes you made to the files. This helps others working with your code stay organized and informed on what you did that made this commit worthy. For example, for this exercise, our comment might be: 'added the index.html document and updated the readme.'

**Style Note:** Technically, the Git style gods have decided that all comments should be written in the present tense. I disagree. Rather strenuously. This is the turbonerd equivalent of the 'should you use the first-person in academic writing' debate---basically the argument goes that the past tense implicates the developer, whereas the present tense refers to the commit. But I have no problem with implicating the developer for all the same reasons that I have no problem with academic writing in the first-person, so rock on with your bad past-tense self.

To commit our files, we use `git commit`. We add a `–m` flag to indicate that we'll be including a message with our commit. In terminal, still in your working directory and with our files staged, type the following command:

```sh
git commit –m "added index.html and updated readme"
```

This commits our changes to the local repository.  You will see a note that files in your master branch were changed and created.

In the future, if you want to stage all previously staged files and commit them in one fell swoop, you can use the `-a` option of the `git commit` command like so:

```sh
git commit -a -m "commit message"
```

## 10. Push files to our online repository

The last step is **push** our committed changes to the remote repository. We do this using `git push`. The syntax for this is `git push origin <branchname>`. This will push the file to the remote origin and match it to the name of the branch. We'll talk more about branches below; for now we can just type `git push` which defaults to the `master` branch on the remote origin. To push our files to Github, use the following:

```sh
git push
```

You will then have to authenticate by typing your Github username and password. This will push our master branch to Github and sync our files.

Navigate to your Github page and check out your ‘username.github.io’ repository. You should see your files and modifications! Wash, rinse, and repeat (and repeat, and repeat, and repeat).

## Speaking of Repeating... Credential Management

While it's great that Github wants to keep you secure, it can also be kind of a pain to enter your credentials every time you push changes to your remote repository. Lucky for us, Git provides a number of built-in ways to store your credentials for later use. You can do some reading on these [here](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage) if you'd like, but I recommend the 'cache' method. This method stores credentials in memory, not on your hard disk, and they are purged after a given period of time. Other methods require that you store your credentials in plain-text files on your hard drive---not exactly secure.

To prevent Github from asking for your credentials for 30 minutes, enter the following command from either Terminal or Git Bash:

```sh
git config --global credential.helper 'cache --timout=1800'
```

You can modify your timeout value, measured in seconds, to your liking.

## 11. View your Website

But that's not all! Because we've named this repo according to the very special .github.io syntax, we've simultaneously created a live website. Open a browser and navigate to http://<yourusername>.github.io

Congrats, you have created your first github repo, and a new website in the process!


## 12. Working with Branches

Up to this point, we have been working with our ‘master’ branch. The ‘master’ branch is the main branch of our repository, and should always be kept working and clean. If we want to work on a copy that is different than the live ‘master’ branch, we can create a working branch that has a copy of all of the files in the master branch, then try out changes on the working branch so you don’t break code that is in the master branch.

Keep in mind that creating new branches will not create new local file directories. That is, if you make changes to a local file while a non-master branch is checked out, the changes are stored in the local Git repository, but the original local file is unchanged (as it is represented by the master branch in Git).

In Terminal, to create a branch, follow the following steps.

#### i. Create a branch based on the master branch

To create a branch based on the master branch, use the following syntax:

***
```sh
git checkout –b <new branch name> <existing branch name>
```
***

For example, we can use:

***
```sh
git checkout –b test-changes master
```
***

to create a new branch called test-changes of the master branch. (Technically the master part at the end is unnecessary, but always better to be verbose).

#### ii. Show all local branches by using the branch command

Show all branches of the repository using the following command:
***
```sh
git branch
```
***
**Note:**An asterisk will appear next to the current working branch.

#### iii. Switching between branches

Use **git checkout** to switch between branches. Switching back to the master branch would look like:

***
```sh
git checkout master
```
***

#### iv. Merge branches

Merging branches is easy. To merge **test-changes** back into master, change to your master branch using checkout, and then use the merge command.

***
```sh
git checkout master
git merge test-changes
```
***

#### v. Commit and Push a Branch

Branches can be commited to the local repository and synced to the remote repository (on the Github site) using the same **push** process described in the steps used for the master branch above.

#### vi. Delete a Branch

If you ever need to delete a branch if you are done working in a branch and have merged changes, use the –d key of the branch command. For example, to delete test-changes, use:

***
```sh
git branch –d test-changes
```
***

**Branches are a powerful component of working with Github!**

## 14. Resolving Merge Conflicts

Users working in large groups are bound to run into some conflicts when two or more people are working on the same files and changing the same lines of code. There are methods for resolving this, but unfortunately will require some manual checking. In short, conflicts will be flagged in your file when you open it in a text editor. You will have to go through your file and find conflicts, decide which one to accept, and then delete the surrounding conflict markers. This is described in nice detail on the Github help pages at the following address.

https://help.github.com/articles/resolving-a-merge-conflict-from-the-command-line/

Congrats, this crash course has introduced you to git and Github! Clearly there is much more to learn, including handling issues, which are like tickets individuals can open on your code, then interact with the authors to resolve, and pull requests, where authors can take modified code and merge it into their original projects. See below for additional reading, cheatsheets, and resources.

Github has a DESKTOP APP! This makes things quite a bit easier. If you are comfortable working on the command line, you can stop here, but to learn the Desktop app, check out Part 1B.


## 12. Pulling changes from Github

Often you will need to incorporate changes made by others on the remote repository on your local drive.  In this case, you can log into terminal and use git pull. Git pull will retrieve new work done by other people and merge the local changes with changes made by others. Syntax appears like the following. (syntax looks like the following - **git pull remote branch **)

***
```sh
git pull origin master
```
***

For more on this, read the following at the Github help pages.

https://help.github.com/articles/fetching-a-remote/
***

***


## Additional Reading and Resources

#### Mac Command Line Cheatsheet –
https://github.com/0nn0/terminal-mac-cheatsheet/wiki/Terminal-Cheatsheet-for-Mac-(-basics-)

#### Github Glossary –
https://help.github.com/articles/github-glossary

#### Git on the Command Line -
http://dont-be-afraid-to-commit.readthedocs.org/en/latest/git/commandlinegit.html

#### Git Branching – Basic Branching and Merging
https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging