eval "$(ssh-agent -s)"
ssh-add key
ssh -vT git@github.com
python maltiscam.py
