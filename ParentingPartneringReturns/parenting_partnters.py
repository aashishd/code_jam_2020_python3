from typing import List, Dict, Tuple, Union

class Activities:
    def __init__(self):
        self.count = int(input())
        self.activities = self.initialize_activities()
        self.cameron_calendar = []
        self.jamie_calendar = []

    def initialize_activities(self):
        activities = [[*[int(val) for val in input().split(" ")], i, None] for i in range(self.count)]
        sorted_by_time = sorted(activities, key=lambda x: (x[0], x[1]))
        return sorted_by_time

    @staticmethod
    def check_calendar(activity: Tuple[int, int, int, str], calendar: List[Tuple[int, ...]]) -> bool:
        can_do = True
        if len(calendar) == 0:
            return True
        else:
            start, end, _, _ = activity
            l_start, l_end = calendar[-1]
            if start < l_end:
                can_do = False
        return can_do

    def get_calendar(self) -> str:
        for activity in self.activities:
            can_cameron_do = self.check_calendar(activity, self.cameron_calendar)
            if can_cameron_do is True:
                self.cameron_calendar.append(activity[:2])
                activity[3] = 'C'
            else:
                can_jamie_do = self.check_calendar(activity, self.jamie_calendar)
                if can_jamie_do is True:
                    self.jamie_calendar.append(activity[:2])
                    activity[3] = 'J'
                else:
                    return "IMPOSSIBLE"

        return "".join([act[3] for act in sorted(self.activities, key=lambda a: a[2])])


def main():
    test_count = int(input())
    for t in range(1, test_count + 1):
        calendar = Activities()
        print("Case #{}: {}".format(t, calendar.get_calendar()))


if __name__ == "__main__":
    main()
