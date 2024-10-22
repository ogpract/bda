import time


class Bucket:
    def __init__(self, size, bits, timestamp):
        self.size = size
        self.bits = bits
        self.timestamp = timestamp


class DGIM:
    def __init__(self, N):
        self.N = N
        self.buckets = []

    def add_bit(self, bit):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if bit == '1':
            new_bucket = Bucket(1, '1', current_time)
            self.buckets.append(new_bucket)
            self._merge_buckets()
        self._remove_old_buckets()

    def _merge_buckets(self):
        i = len(self.buckets) - 1
        while i > 0:
            if self.buckets[i].size == self.buckets[i - 1].size == self.buckets[i - 2].size:
                self.buckets[i - 1].size *= 2
                self.buckets[i - 1].bits = self.buckets[i -
                                                        2].bits + self.buckets[i - 1].bits
                del self.buckets[i - 2]
            i -= 1

    def _remove_old_buckets(self):
        total_bits = sum([bucket.size for bucket in self.buckets])
        while total_bits > self.N:
            total_bits -= self.buckets[0].size
            self.buckets.pop(0)

    def estimate_ones(self):
        total_ones = 0
        for i in range(len(self.buckets) - 1):
            total_ones += self.buckets[i].size
        if self.buckets:
            total_ones += self.buckets[-1].size // 2
        return total_ones

    def print_buckets(self):
        print(f"\nTotal number of buckets: {len(self.buckets)}")
        total_ones = sum([bucket.size for bucket in self.buckets])
        print(f"Total count of 1's in all buckets: {total_ones}")
        print("Buckets (size, bits, timestamp):")
        for bucket in self.buckets:
            print(
                f"Size: {bucket.size}, Bits: {bucket.bits}, Timestamp: {bucket.timestamp}")


def main():
    N = int(input("Enter the window size (N): "))
    binary_string = input("Enter the binary string: ")
    dgim = DGIM(N)
    for bit in binary_string:
        dgim.add_bit(bit)
    estimated_ones = dgim.estimate_ones()
    print(f"Estimated number of 1's in the last {N} bits: {estimated_ones}")
    dgim.print_buckets()


if __name__ == "__main__":
    main()
