---
title: '6.4 Virtual Environments (optional)'
---

::::::::::::::::::::::::::::::::::::: callout

## Optional section

This section is optional. It belongs with Week 6, but nothing in the course depends on it.

::::::::::::::::::::::::::::::::::::::::::::::::

## Setting up Virtual Environments

To start with project, it would be better to have a virtual environment. Virtual environment can help us to create an isolated or separate environment. This will help us to avoid conflicts in dependencies across projects. If you write `python -m pip freeze` on your terminal you will see all the installed packages on your computer. If we use a virtual environment, we will access only packages which are specific for that project.

Python comes with the _venv_ module for this, so there is nothing extra to install. PyCharm also creates a virtual environment for you when you make a new project; the steps below show what it does behind the scenes.

Inside the IntroToProgramming folder create a my_project folder, then open a terminal in that folder and create a virtual environment:

For Windows:

```bash
C:\Users\User\Documents\IntroToProgramming\my_project> python -m venv venv
```

For Mac/Linux:

```bash
~/Desktop/IntroToProgramming/my_project$ python3 -m venv venv
```

I prefer to call the new virtual environment venv, but feel free to name it differently. Let us check if the venv was created by using `dir` (Windows) or `ls` (Mac/Linux). You should see a folder called venv.

Let us activate the virtual environment by writing the following command in our project folder.

For Windows PowerShell or Command Prompt:

```bash
C:\Users\User\Documents\IntroToProgramming\my_project> venv\Scripts\activate
```

For Windows Git Bash:

```bash
~/Documents/IntroToProgramming/my_project$ source venv/Scripts/activate
```

For Mac/Linux:

```bash
~/Desktop/IntroToProgramming/my_project$ source venv/bin/activate
```

After you write the activation command, your prompt will start with (venv). See the example below.

```bash
(venv) C:\Users\User\Documents\IntroToProgramming\my_project>
```

Now, let's check the available packages in this project by writing `python -m pip freeze`. You will not see any packages. Let us install the _requests_ package to this project.

```bash
(venv) C:\Users\User\Documents\IntroToProgramming\my_project> python -m pip install requests
```

Now, let us write pip freeze to see a list of installed packages in the project:

```bash
(venv) C:\Users\User\Documents\IntroToProgramming\my_project> python -m pip freeze
```

```output
certifi==2026.10.23
charset-normalizer==3.5.2
idna==3.20
requests==2.34.2
urllib3==2.8.0
```

Your version numbers may differ. requests needs four other packages, so pip installed them too. When you finish, you should deactivate the virtual environment using _deactivate_.

```bash
(venv) C:\Users\User\Documents\IntroToProgramming\my_project> deactivate
```

Your project folder now has its own virtual environment. You should add venv to your .gitignore file so you do not push it to GitHub.

::::::::::::::::::::::::::::::::::::: challenge

## Exercises

1. Create a project directory with a virtual environment based on the example given above.

::::::::::::::::::::::::::::::::::::::::::::::::

