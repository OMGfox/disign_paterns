import base64


class Encryptor:

    def __init__(self, filename):
        self.filename = filename

    def run(self):
        # каркас алгоритма обработки - эта последовательность не меняется
        # It's a frame of processing - this sequence is not changing
        data = self.get_data()
        encrypted = self.encrypt(data)
        self.save(encrypted)

    def get_data(self):
        # этап алгоритма, который можно переопределить в наследнике
        # This state of the algorithm, which can be overrided
        with open(self.filename, 'r') as ff:
            return ff.read()

    def encrypt(self, data):
        result = ''
        for ch in data:
            result += str(ord(ch))
        return result.encode()

    def save(self, encrypted):
        with open(self.filename + '.enc', 'wb') as ff:
            ff.write(encrypted)


class Base64Encryptor(Encryptor):

    def encrypt(self, data):
        return base64.b64encode(data.encode())

if __name__ == '__main__':
    need_base_64 = input('Вам нужна base64 зашифровка? (да/нет) >>>') == 'да'
    filename = 'my_private_data.txt'
    if need_base_64:
        enc = Base64Encryptor(filename=filename)
    else:
       enc = Encryptor(filename=filename)
    enc.run()
    
