class QuanLyCheckIn:
    def __init__(self):
        self.ds_CheckIn = []

    def them_CheckIn(self, checkIn):
        self.ds_CheckIn.append(checkIn)

    def getCheckInByMHGV(mh, gv): 
        checkin = None
        for ck in self.ds_CheckIn: 
            if ck.giang_day.giangVien.hoTen == gv and ck.giang_day.monHoc.tenMH:
                checkin = ck
        return checkin