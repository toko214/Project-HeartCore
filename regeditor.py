import _winreg
abc = "abcdefghijklmnopqrstuvwxyz"


def print_values(key, info):
    for ch in xrange(0,len(info[0])):
        print info[0][ch]
        print _winreg.QueryValueEx(key,info[0][ch])[0]


def create_value(key,data, info):
    if len(info[0]) == 26:
        value = info[0][-1]
        info = info[0].replace(value,"")
        info = value + info
        _winreg.SetValueEx(key, value, 0, _winreg.REG_SZ, data)
        _winreg.SetValueEx(key, "MRUList", 0, _winreg.REG_SZ, info)
    else:
        temp = abc
        for ch in info[0]:
            temp = temp.replace(ch,"")
        print "chars = " + temp
        _winreg.SetValueEx(key, temp[0], 0, _winreg.REG_SZ, data)
        info = info[0] + temp[0]
        _winreg.SetValueEx(key, "MRUList", 0, _winreg.REG_SZ, info)


def delete_value(key, value, info):
    _winreg.DeleteValue(key, value)
    print info[0]
    info = info[0].replace(value, "")
    _winreg.SetValueEx(key, "MRUList", 0, _winreg.REG_SZ, info)


def main():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU", 0, _winreg.KEY_ALL_ACCESS)
    info = _winreg.QueryValueEx(key, "MRUList")
    create_value(key,  "asasddfsfsdd", info)
    info = _winreg.QueryValueEx(key, "MRUList")
    create_value(key,"kesy", info)
    info = _winreg.QueryValueEx(key, "MRUList")
    print_values(key, info)
    delete_value(key, "a", info)
if __name__ == "__main__":
    main()
