class MusicPlayer(object):

    instance = None

    init_flag = False

    #重写new方法
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance


    def __init__(self):
        if MusicPlayer.init_flag:
            return

        print("初始化音乐播放器")

        MusicPlayer.init_flag = True


kugou = MusicPlayer()

abc = MusicPlayer()

