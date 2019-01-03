class Game(object):
    #定义历史最高分
    top_score = 0

    def __init__(self,player_name):
        self.player_name = player_name

    #显示游戏提示
    @staticmethod
    def show_help():
        print("显示游戏提示：xxxxx")

    #显示历史最高分
    @classmethod
    def show_top_score(cls):
        print("历史最高分是 %d" % cls.top_score)

    #开始游戏
    def start_game(self):
        print("%s 开始游戏啦" % self.player_name)

def main():
    print("测试")
    print("-"*50)

    Game.show_help()
    Game.show_top_score()

    xiaoming = Game("xiaoming")

    xiaoming.start_game()

if __name__ == "__main__":
    main()