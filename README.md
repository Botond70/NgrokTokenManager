# NgrokTokenManager
A semi useful Ngrok authentication token manager.

## Before use: put 2 tokens inside the tokens.bac txt file!

Static cli-mode syntax: python ngrokmanager.py (lbi(n|d)) [int for n|d]

l - loads the tokens from the tokens.txt file.

b - loads the tokens from the tokens.bac file, doesn't work unless there are at least 2 tokens inside the tokens.bac file!

i - injects the corresponding authtoken in the list into the .yml file.

n [int] - cycles onto next token, uses the default n=0.

d [int] - drops the nth token from the list, useful for debugging, but can destroy the internal counter of the program if you provide wrong input. use carefully

the last 2 parameters are NOT compatible with eachother.
