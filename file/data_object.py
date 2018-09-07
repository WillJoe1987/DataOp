import time

init_key = 2018011500019011320108611569

class file_calc():
    name = 'd:/bill_int_calc__eff1a02d_54af_41e8_acad_83a3cd24f648'
    opened = False
    calc_file = None

    def get_file(self):
        if self.calc_file is None:
            self.calc_file = open(self.name, mode='a+',encoding='utf-8')
        return self.calc_file

    def write_line(self, line_content):
        try:
            if self.calc_file is None:
                self.get_file()
            self.calc_file.write(line_content)
            return True
        except BaseException as e:
            print(e)
            return False

    def file_close(self):
        try:
            self.calc_file.close()
        finally:
            self.calc_file = None
            self.opened = False


def create_data_line(initkey, order):
    return str(initkey+order)+',20180213,0,0,18000,0,0.0,0.00050,0,36,0,01'

start = lambda:int(round(time.time() * 1000))
start_time = start()
line_number = 20000000
index = 0
data_file = file_calc()

while(index<line_number):

    content = create_data_line(init_key, index)
    result = data_file.write_line(content+'\n')
    index += 1
    print(''+str(index)+':'+str(result)+':'+content)
end_time = start()
print('finished!used:'+str(end_time - start_time)+'ms.')
data_file.file_close()