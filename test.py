# dataencode = {
#     "_method": "POST",
#     "data[FileSearch][is_compress]": "false",
#     "data[FileSearch][fixedToken]": '',
#     "data[FileSearch][hashUrl]": "bDw2maKV",
#     "action": "dir_download_dl",
#     "filelist[0]": "/osn-disk/webuser/wsdb/share_directory/bDw2maKV/png/Pifd/" + "2022/04-24/20/"+"hima820220424200000fd.png",
#     "dl_path": "/osn-disk/webuser/wsdb/share_directory/bDw2maKV/png/Pifd/"+"2022/04-24/20/"+"hima820220424200000fd.png"
# }

# from urllib.parse import urlencode
# data = '_method=POST&data%5BFileSearch%5D%5Bis_compress%5D=false&data%5BFileSearch%5D%5BfixedToken%5D=020e1db382162119f2f6e6cf6e7e5e4af311d63c&data%5BFileSearch%5D%5BhashUrl%5D=bDw2maKV&action=dir_download_dl&filelist%5B0%5D=%2Fosn-disk%2Fwebuser%2Fwsdb%2Fshare_directory%2FbDw2maKV%2Fpng%2FPifd%2F2022%2F04-24%2F23%2Fhima820220424233000fd.png&dl_path=%2Fosn-disk%2Fwebuser%2Fwsdb%2Fshare_directory%2FbDw2maKV%2Fpng%2FPifd%2F2022%2F04-24%2F23%2Fhima820220424233000fd.png'

# print(data)

# print(urlencode(dataencode))

# data = {'searchList': [['file', 'hima820220428120000fd.png', 155875637, '2022/04/28 12:19:44', '/osn-disk/webuser/wsdb/share_directory/bDw2maKV/png/Pifd/2022/04-28/12'], ['file', 'hima820220428121000fd.png', 155901296, '2022/04/28 12:29:44', '/osn-disk/webuser/wsdb/share_directory/bDw2maKV/png/Pifd/2022/04-28/12'],
#                        ['file', 'hima820220428122000fd.png', 155823510, '2022/04/28 12:39:44', '/osn-disk/webuser/wsdb/share_directory/bDw2maKV/png/Pifd/2022/04-28/12'], ['file', 'hima820220428123000fd.png', 155693196, '2022/04/28 12:49:45', '/osn-disk/webuser/wsdb/share_directory/bDw2maKV/png/Pifd/2022/04-28/12']], 'dirList': None}

# print(data['searchList'][0][4]+data['searchList'][0][1])
# print(data['searchList'][len(data['searchList'])-2])

a = 'hima820220428122000fd.png'
print(a[13:15]+":"+a[15:17])