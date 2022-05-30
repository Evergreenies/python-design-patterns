# Filename      :       002_mediator_events.py
# Created By    :       Suyog Shimpi
# Created Date  :       26/05/22

class Event(list):  # noqa
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:  # noqa
    def __init__(self):
        self.events = Event()

    def fire(self, args):  # noqa
        self.events(args)


class GoalScoredInfo:  # noqa
    def __init__(self, who_scored, goals_scored):
        self.who_scored = who_scored
        self.goals_scored = goals_scored


class Player:  # noqa
    def __init__(self, name: str, game: Game):
        self.name = name
        self.game = game
        self.goals_scored = 0

    def score(self):  # noqa
        self.goals_scored += 1
        args = GoalScoredInfo(self.name, self.goals_scored)
        self.game.fire(args)


class Coach:  # noqa
    def __init__(self, game: Game):
        game.events.append(self.celebrate_goal)

    def celebrate_goal(self, args):  # noqa
        if isinstance(args, GoalScoredInfo) and args.goals_scored < 3:
            print(f'Coach says: well done. {args.who_scored}!')


if __name__ == '__main__':
    _game = Game()
    _player = Player('Sam', _game)
    _coach = Coach(_game)
    _player.score()
    _player.score()
    _player.score()
