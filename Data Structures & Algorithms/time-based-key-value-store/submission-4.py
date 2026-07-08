class TimeMap:

    def __init__(self):
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = [(timestamp, value)]
        else:
            self.mapping[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping:
            return ""
        else:
            values = self.mapping[key]
            print(values)
            l, h = 0, len(values) - 1
            tp = values[-1][0] + 1
            while l <= h:
                mid = l + (h-l)//2
                mid_time = values[mid][0]
                if mid_time == timestamp:
                    return values[mid][1]
                elif mid_time > timestamp:
                    h = mid - 1
                else:
                    tp = mid
                    l = mid + 1
            if tp > values[-1][0]:
                return ""
            else:
                return values[tp][1]


        
