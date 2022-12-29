bytes = int(input('How many bytes?'))
kilobytes = bytes / 1024
megabytes = bytes / 1048576
gigabytes = bytes / 1073741824
terabytes = bytes / 1099511627776

print( str(bytes) + ' bytes =')
print( str(kilobytes) + ' kbs')
print( str(megabytes) + ' mbs')
print( str(gigabytes) + ' gbs')
print( str(terabytes) + ' tbs')
print(' ')

tbytes = float(input('How many terabytes?'))
gbytes = tbytes * 1024
mbytes = tbytes * 1048576
kbytes = tbytes * 1073741824
bbytes = tbytes * 1099511627776

print( str(tbytes) + ' terabytes =')
print( str(gbytes) + ' gbs')
print( str(mbytes) + ' mbs')
print( str(kbytes) + ' kbs')
print( str(bbytes) + ' bytes')
