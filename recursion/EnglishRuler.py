class EnglishRuler:

    def draw_line(self, tick_length, tick_label=''):
        line = '-' * tick_length;
        if tick_label:
            line += ' ' + tick_label

        print(line)


    def draw_interval(self, center_length):
        if center_length > 0:
            self.draw_interval(center_length-1)
            self.draw_line(center_length)
            self.draw_interval(center_length-1)


    def draw_ruler(self, num_inches, major_length):
        self.draw_line(major_length, '0')

        for j in range(1, 1 + num_inches):
            self.draw_interval(major_length-1)
            self.draw_line(major_length, str(j))
