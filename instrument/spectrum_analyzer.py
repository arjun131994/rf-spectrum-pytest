import socket

class SpectrumAnalyzer:

    def __init__(self, ip, port=5025):

        self.sock = socket.socket()
        self.sock.connect((ip, port))

    def send_cmd(self, cmd):

        self.sock.send((cmd + "\n").encode())

    def query(self, cmd):

        self.send_cmd(cmd)
        return self.sock.recv(1024).decode()

    def set_center_frequency(self, freq):

        self.send_cmd(f"FREQ:CENT {freq}")

    def get_center_frequency(self):

        return self.query("FREQ:CENT?")

    def set_span(self, span):

        self.send_cmd(f"FREQ:SPAN {span}")

    def read_peak_power(self):

        return self.query("CALC:MARK:Y?")

    def close(self):

        self.sock.close()
