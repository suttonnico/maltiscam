import cv2
import time
from git import Repo

PATH_OF_GIT_REPO = r'.'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'maltis'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')

cam = 6
camera_0 = cv2.VideoCapture(cam)

time.sleep(1)
s0, img = camera_0.read()
cv2.imwrite('maltis.png', img)
git_push()

