eval "$(ssh-agent -s)"
printf "malta\n" | ssh-add key
ssh -vT git@github.com
python maltiscam.py
