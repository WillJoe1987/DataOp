
class file_calc():
    name = 'd:/bill_int_calc__eff1a02d_54af_41e8_acad_83a3cd24f648'
    opened = False
    calc_file = None

    def get_file(self):
        if self.calc_file is None:
            self.calc_file = open(self.name, 'a+')
        return self.calc_file

    def write_line(self, line_content):
        try:
            if self.calc_file is None:
                self.get_file(self)
            self.calc_file.write(line_content)
            return True
        except:
            return False

    def file_close(self):
        try:
            self.calc_file.close()
        finally:
            self.calc_file = None
            self.opened = False

def helow():
    print('h')