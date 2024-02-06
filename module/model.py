from devantech_eth import eth002


class Eth002(eth002.ETH002):
    def __init__(self, ip="192.168.0.2", port=17494, password=None):
        super().__init__(ip=ip, port=port, password=password)


if __name__ == "__main__":
    eth = Eth002(ip="192.168.2.141", password="password")
