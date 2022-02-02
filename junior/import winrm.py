import win32wnet

username = 'eapteka\d.artamonov2'
password = 'Df4kq-poECW1'

# sess = winrm.Session('http:////10.100.24.28', auth=(username,
#  password))
# result = sess.run_cmd('ipconfig', ['/all'])

# win32wnet.WNetAddConnection2(0, None, '\\\\'+host, None, username, password)
# shutil.copy(source_file, '\\\\'+host+dest_share_path+'\\')
# print()
# win32wnet.WNetCancelConnection2('\\\\'+host, 0, 0)


def testAddConnection(self):
    localName = self.findUnusedDriveLetter() + ':'
    print(localName)
    for share in self.iterConnectableShares():
        print(localName)

        share.lpLocalName = localName
        print(share)
        win32wnet.WNetAddConnection2(share)
        win32wnet.WNetCancelConnection2(localName, 0, 0)
        break


testAddConnection()
