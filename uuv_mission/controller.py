class PDController:
    def __init__(self, KP, KD):
        self.KP = KP
        self.KD = KD
        self.e_prev = 0

    def compute_control_action(self, r, y):
        e = r - y
        u = self.KP * e + self.KD * (e - self.e_prev)
        self.e_prev = e
        return u