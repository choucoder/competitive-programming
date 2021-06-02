class Activity:

    def __init__(self, times) -> None:
        self.start = times[0]
        self.end = times[1]

    def __lt__(self, a):
        return self.end < a.end

    def __repr__(self) -> str:
        return repr(f'{self.start} -> {self.end}')


def solve(activities):
    activities = sorted(activities)

    activity = activities.pop(0)
    print(activity)

    for ai in activities:
        if ai.start >= activity.end:
            print(ai)
            activity = ai

if __name__ == '__main__':
    activities = [
        [0, 6], [3, 4], [1, 2],
        [5, 9], [5, 7], [8, 9]
    ]
    _activities = []
    for a in activities:
        _activities.append(Activity(a))
    
    print(solve(_activities))