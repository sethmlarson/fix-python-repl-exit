# Fix Python REPL `exit`

A simple script that makes typing `exit` in a Python interpreter do what you expect.

## How to Use

The whole script to make things work is in the file `fix-python-repl-exit.py`.

If you have a `PYTHONSTARTUP` script already, simply paste the contents of the file
into your existing script. If you don't have a script already then you can setup one
up like so:

```bash
# Create the initial script
$ touch ~/.pythonstartup.py

# Add the PYTHONSTARTUP environment variable to your bash / console profile:
# The name of the file '~/.bashrc' may be different if you're on a different OS.
$ echo 'export PYTHONSTARTUP="$HOME/.pythonstartup.py"' > ~/.bashrc

# Add things to the '.pythonstartup.py' file:
$ cat fix-python-repl-exit.py >> ~/.pythonstartup.py

# Try it out!
$ python
>>> exit
🎉
```

## License

MIT
