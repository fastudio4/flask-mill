from math import pi
from statistics import mean
from mill.calculations import db_milling


class Milling(object):
    def __init__(self, material, d_cut, t_cut, max_speed_spindle, max_frequency):
        self.material = material
        self.d_cut = d_cut
        self.t_cut = t_cut
        self.max_speed_spindle = max_speed_spindle
        self.max_frequency = max_frequency
        self.setting = self.min_max_speed()

    def spindle_speed(self, cutting_speed):
        return int(round((1000 * cutting_speed)/(pi * self.d_cut), 0))

    def fz_materials(self):
        val = int(self.d_cut)
        if 0 < val <= 1:
            return 0
        elif 1 <= val <= 2:
            return 1
        elif 3 <= val <= 4:
            return 2
        elif 5 <= val <= 6:
            return 3
        elif 8 <= val <= 10:
            return 4
        elif 12 <= val <= 16:
            return 5
        else:
            return None

    def feed(self, spindle_speed):
        return spindle_speed * db_milling[self.material]['fz'][self.fz_materials()] * self.t_cut

    def min_max_speed(self):
        min_speed = self.spindle_speed(db_milling[self.material]['min_cut'])
        max_speed = self.spindle_speed(db_milling[self.material]['max_cut'])
        if max_speed > self.max_speed_spindle:
            max_speed_cut = int(round((self.max_frequency * self.max_speed_spindle)/max_speed, 0))
            min_speed_cut = db_milling[self.material]['min_cut'] - (db_milling[self.material]['max_cut'] - max_speed_cut)
            min_speed_spindle = self.spindle_speed(min_speed_cut)
            max_speed_spindle = self.spindle_speed(max_speed_cut)
            return {
                'min_cut': min_speed_cut,
                'mean_cut': mean([min_speed_cut, max_speed_cut]),
                'max_cut': max_speed_cut,
                'min_speed': min_speed_spindle,
                'mean_speed': mean([min_speed_spindle, max_speed_spindle]),
                'max_speed': max_speed_spindle,
                'min_feed': self.feed(min_speed_spindle),
                'mean_feed': mean([self.feed(min_speed_spindle), self.feed(max_speed_spindle)]),
                'max_feed': self.feed(max_speed_spindle),
                'fz': db_milling[self.material]['fz'][self.fz_materials()] * self.t_cut,
                'embed': round(self.d_cut, 1)
            }

        return {
            'min_cut': db_milling[self.material]['min_cut'],
            'mean_cut': mean([db_milling[self.material]['min_cut'], db_milling[self.material]['max_cut']]),
            'max_cut': db_milling[self.material]['max_cut'],
            'min_speed': min_speed,
            'mean_speed': mean([min_speed, max_speed]),
            'max_speed': max_speed,
            'min_feed': self.feed(min_speed),
            'mean_feed': mean([self.feed(min_speed), self.feed(max_speed)]),
            'max_feed': self.feed(max_speed),
            'fz': db_milling[self.material]['fz'][self.fz_materials()] * self.t_cut,
            'embed': self.d_cut
        }
