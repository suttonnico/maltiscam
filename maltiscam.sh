eval "$(ssh-agent -s)"
printf "malta\n" | ssh-add /home/pi/Documents/maltis/maltiscam/key
ssh -vT git@github.com
python /home/pi/Documents/maltis/maltiscam/maltiscam.py
cd /home/pi/Documents/maltis/maltiscam/
git push
