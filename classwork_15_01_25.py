import zipfile

class Archive:
    def __init__(self, path, description):
        self.path = path
        self.description = description
        self.password = None

    def getinfo(self):
        print(f'Path: {self.path}\nDescription{self.description}\nPassword: {self.password}')


class Bruteforce:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def hack(self, archive):
        zip_file = zipfile.ZipFile(archive)
        password = None
        f = open(self.dictionary, 'r')
        for line in f.readlines():
            password = line.strip('\n')
            try:
                zip_file.extractall(pwd=password.encode())
                print('--------------------')
                print(f'RESULT: {password}')
                f.close()
                return (True, password)
            except:
                print(password)
        f.close()
        return (False, None)

class Library:
    def __init__(self, bruteforce):
        self.bruteforce = bruteforce
        self.archives = []

    def showarchives(self):
        for archive in self.archives:
            archive.getinfo()
            print('')

    def hackall(self):
        for archive in self.archives:
            if archive.password == None:
                res = self.bruteforce.hack(archive.path)
                if res[0] == True:
                    archive.password = res[1]


def main():
    library = Library(Bruteforce('dictionary.txt'))
    library.archives.append(Archive('test.zip', 'Test'))
    library.showarchives()
    library.hackall()
    library.showarchives()

if __name__ == '__main__':
    main()








