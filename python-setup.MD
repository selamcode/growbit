## See All Installed Python Versions

```bash
ls /usr/local/bin/python*
```

## How to swith between python version?
`pyenv` — Manages Python versions
-Lets you install and switch between multiple Python versions on your system.

- Useful when:

    - Your system Python is outdated.

    - You want to test your code in Python 3.8, 3.11, 3.12, etc.

- Doesn't manage dependencies or packages directly.

- Think of it as a Python version manager.
### Python Version Management with pyenv

For updated information on installing pyenv go to 
[Visit pyenv repo](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)

##### install pyenv

```bash
brew update
brew install pyenv
```
Then we need to `Set up our shell environment for Pyenv`

for `Zsh`

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init - zsh)"' >> ~/.zshrc
```
##### Finally `Restart` your shell for the `PATH` changes to take effect.

```bash
exec "$SHELL"
```

### Usage

##### See all available Python versions you can install

```bash
pyenv install --list
```

##### Narrow down the list to specific versions, e.g., Python 3.11.x
```bash
pyenv install --list | grep 3.11
```

##### See which Python versions are already installed on your machine

```bash
pyenv versions
```
##### Check if a specific version (e.g., 3.11.7) is installed

```bash
pyenv versions | grep 3.11.7
```
> No output means version is not installed

##### Install a specific Python version using pyenv

```bash
pyenv install 3.11.7
```
### Set the installed Python version as default

##### Set globally (system-wide default for all projects)

```bash
pyenv global 3.11.7
```

##### Set locally (only for the current project directory)
```bash 
pyenv local 3.11.7
```
- It sets the Python version only for the current directory and its subdirectories.

- It does this by creating a file named .python-version in that directory, which tells pyenv:
"Use Python 3.11.7 here, no matter what the global default is."

##### Check which Python version is currently active

```bash
python --version
# or
pyenv version
```
