import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.data = [[0] * length]
        self.count_snap = 0
        self.length = length

    def set(self, index: int, val: int) -> None:
        if len(self.data[self.count_snap]) == 0:
            self.data[self.count_snap].append(val)
        self.data[self.count_snap][index] = val

    def snap(self) -> int:
        self.data.append([0] * self.length)
        self.count_snap += 1
        for i in range(len(self.data[self.count_snap - 1])):
            self.data[self.count_snap][i] = self.data[self.count_snap - 1][i]
        return self.count_snap - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.data[snap_id][index]


if __name__ == '__main__':
    snap_array = SnapshotArray(3)
    snap_array.set(0, 5)
    snap_array.snap()
    snap_array.set(0, 6)
    print(snap_array.get(0, 0))
    bisect.bisect_left()