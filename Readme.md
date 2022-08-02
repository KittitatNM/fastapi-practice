# FastAPI Practice

## UPDATE THIS PROJECT USE POETRY FOR PACKAGE MANAGER SERVICE

### INITAIL WITH POETRY

init poetry package manager with commad

``` bash
$ poetry init
```

After run this command in your project will create pyproject.toml for keep your dependencies and create virtualenv for use to develop

### ACTIVATE VIRTUALENV 

You **must** to access to virtualenv in your project because after the end of development process you need to push project to production virtaulenv as same as env in production. This project can't be crash.

Find the virtualenv (manual)

``` bash
$ poetry env info
```

This command will show path to keep virtualenv.

Command to activate virtualenv
``` bash
$ source {path-to-virtualenv}/Scripts/activate
```
---
*OLD Project VirtualENV*
## VIRTUAL ENV
### Create Virtual ENV at first
Create virtual ENV for export to use in another machine
``` powershell
PS> python -m virtualenv venv
```
### Active Virtualenv
Acitve virtualenv for install python package
- Powershell
``` powershell
PS> .\venv\Scripts\Activate
```
if you have problem with policy in powershell [Execution Policy](https:/go.microsoft.com/fwlink/?LinkID=135170)

- Command Prompt
``` cmd
C:\> .\venv\Scripts\activate
```
### Deactivate Virtualenv
Deactivate from virtualenv
``` cmd
(venv) C:\> deactivte
```
** Can use this command from command prompt and powershell