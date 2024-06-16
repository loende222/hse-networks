import argparse
import socket
import subprocess


class MTUFinder:
    min_mtu_ = 0
    max_mtu_ = 100000
    HEADERS_SIZE_ = 28

    def __init__(self, host):
        self.host_ = host
    
    def check_correctness(self):
        try:
            socket.inet_aton(socket.gethostbyname(self.host_))
        except Exception:
            print("Assress is not correct")
            exit(1)

    def build_ping(self, packet_size):
        return ["ping", self.host_, "-M", "do", "-c", "1", "-s", str(packet_size)]

    def try_packet(self, packet_size):
        print(f"Considering packet size {packet_size}")
        try:
            out = subprocess.Popen(self.build_ping(packet_size), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            print("Error occured while processing ping. Can't proceed")
            exit(1)
        return out.wait() == 0

    def find_mtu(self):
        while self.max_mtu_ - self.min_mtu_ > 1:
            mtu = (self.min_mtu_ + self.max_mtu_) // 2
            if self.try_packet(mtu):
                self.min_mtu_ = mtu
            else:
                self.max_mtu_ = mtu
        return self.min_mtu_ + self.HEADERS_SIZE_


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', help='Host to be checked', required=True)
    args = parser.parse_args()
    
    mtu_finder = MTUFinder(args.host)
    mtu_finder.check_correctness()
    mtu = mtu_finder.find_mtu()

    print(f"MTU is {mtu}")
