from randomUtils import *
import copy


class CuckooHashTable:

    def __init__(self, length: int):
        self.arrays = [[None for i in range(length)] for j in range(2)]
        self.length = length
        self.h = None
        self.reset_hash()

    def get_load_factor(self):
        return len([i for i in self.arrays[0] if i is not None] + [i for i in self.arrays[1] if i is not None]) / (2 * self.length)

    def __str__(self):
        return f"[0]: {self.arrays[0]}\n[1]: {self.arrays[1]}"

    def reset_hash(self):
        a1, b1, c1, d1 = get_random_numbers(4)
        a2, b2, c2, d2 = get_random_numbers(4)
        p1 = get_random_prime()
        p2 = get_random_prime()
        self.h = [lambda x: ((a1*x**3 + b1*x**2 + c1*x + d1) % p1) % self.length, lambda x:  ((a2*x**3 + b2*x**2 + c2*x + d2) % p2) % self.length]

    def search(self, key):
        for i in range(2):
            if self.arrays[i][self.h[i](key)] is not None:
                return self.arrays[i][self.h[i](key)]
        return None

    def set(self, key, val):
        ret = self._set(key, key, val, 0)
        if ret == 1:
            rehash_failed = self.rehash()
            if rehash_failed == 1:
                # print(f"rehashing failed")
                return 1
            ret = self._set(key, key, val, 0)
            if ret == 1:
                # print(f"after rehashing, insertion failed")
                return 1
        return 0

    def _set(self, key, first_key, val, time, array_id=0):
        if key == first_key:
            time += 1
            if time == 3:
                return 1
        if self.arrays[array_id][self.h[array_id](key)] is not None:
            dis = self.arrays[array_id][self.h[array_id](key)]
            self.arrays[array_id][self.h[array_id](key)] = (key, val)
            return self._set(dis[0], first_key, dis[1], time, 0 if array_id == 1 else 1)
        else:
            self.arrays[array_id][self.h[array_id](key)] = (key, val)
            return 0

    def rehash(self):

        old_arrays = copy.deepcopy(self.arrays)
        old_hash = copy.deepcopy(self.h)
        elems = []
        for i in range(2):
            for j in range(self.length):
                if self.arrays[i][j] is not None:
                    elems.append(self.arrays[i][j])
                    self.arrays[i][j] = None

        self.reset_hash()
        ret = 0
        for e in elems:
            ret = self._set(e[0], e[0], e[1], 0)
            if ret == 1:
                break

        if ret == 1:
            self.arrays = old_arrays
            self.h = old_hash
            # print("abort, restore to previous status")
            return 1
        else:
            # print("rehashing done")
            return 0










