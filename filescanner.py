
#!/usr/bin/env/python3
from sys import path
import os
import time
import datetime
import platform
import _sqlite3
import hashlib
import codecs
import os.path
import io


def dbcreation():
    global now, dbname
    now = datetime.date.today()
    now = datetime.datetime.now().strftime("%Y-%m-%d.%H-%M")
    dbname = str(now)


def finish():
    return 1


def dbname():
    nowtime = datetime.datetime.now().strftime("%Y-%m-%d.%H-%M")
    dbnamenow = str(nowtime)
    name = dbnamenow + '-datastore' + '.db'
    return name


def enum(**enums):
    return type('Enum', (), enums)


oslist = enum(LINUX='LINUX', WINDOWS='WINDOWS', MAC='DARWIN', UNKNOWN='UNKNOWN')

global os_name, w, g


def osname():
    global oslist, os_name
    oslist = (platform.system())
    os_name = oslist
    return os_name


def getpath():
    thepath = None
    thepath = '/'
    return thepath


def getcount(name):
    global number
    file_count = 0
    dir_count = 0
    total = 0
    nowis = datetime.datetime.now()
    dbnameis = str(nowis)
    sqlis = dbnameis + '-datastore' + '.db'

    for dirName, subdirList, fileList in os.walk(name):
        dir_count += 1
        for fname in fileList:
            file_count += 1
    total += 1
    print("Total number of files == {0}".format(file_count))
    number = file_count
    print("Total number of directories == {0}".format(dir_count))


def allpaths(name):
    file_list = []
    global globallists

    for root, _, filenames in os.walk(name):
        for filename in filenames:
            file_list.append(os.path.join(root, filename))

    globallists = file_list


def getfiles(name):
    rows = 100
    count = 1
    global names
    fname = []
    global w, g
    now = datetime.datetime.now().strftime("%Y-%m-%d.%H-%M")
    dbname = str(now)
    sql = dbname + '-datastore' + '.db'

    # for x in name:
    head, tail = os.path.split(name)
    return tail


def getsize(name):
    sizing = []
    global globalsizing
    count = 1

    try:
        sizing = [os.stat(name).st_size]
        return sizing

    except IOError:
        count += 1
        print("doing ", end=',')
        print(count)
        pass

    globalsizing = sizing


def creationdate(name):
    global creations

    y = os.path.getctime(name)
    b = datetime.datetime.fromtimestamp(y)
    j = datetime.datetime.isoformat(b)
    return j


def modificationdate(name):
    global modifications

    y = os.path.getmtime(name)
    b = datetime.datetime.fromtimestamp(y)
    j = datetime.datetime.isoformat(b)

    return j


def accessdate(name):
    global acceses
    y = os.path.getctime(name)
    b = datetime.datetime.fromtimestamp(y)
    j = datetime.datetime.isoformat(b)

    return j


def hash(name):
    global md5global

    with codecs.open(name, "r", encoding='utf-8', errors='ignore') as fdata:
        for line in fdata:
            data_encode = line.encode('utf-8', errors='ignore')
            md5 = hashlib.md5(data_encode).hexdigest()
            return md5


def extension(name):
    global ext
    head, tail = os.path.split(name)
    ext = os.path.splitext(tail)[1][1:].strip()
    # ext = tail.split(".")[-1]
    return ext


def low(exte):
    audio = ['AIF', 'CDA', 'MID', 'MIDI', 'MP3', 'MPA', 'OGG', 'WAV', 'WMA', 'WPL', 'M3U', 'PLS' ]
    disk_image= ['BIN', 'DMG', 'ISO', 'TOAST', 'VCD', 'VMDK']
    data_source = ['DAT', 'DB', 'DBF', 'MDF', 'SAV', 'SQL', 'XML']
    nothing = ['APK', 'BAT', 'BIN', 'CGI', 'PL', 'COM', 'EXE', 'GADGET', 'JAR', 'PY', 'WSF', 'VBS', 'TASK', 'CMD', 'FNT'
            , 'FON', 'OTF', 'TTF', 'WOFF', 'WOFF2', 'ASP', 'ASPX', 'CER', 'CFM', 'CGI', 'PL', 'CSS', 'HTML', 'HTML', 'JS',
               'JSP', 'PART', 'PHP', 'PHTML', 'PHP3', 'PHP4', 'PHP5', 'PY', 'RSS', 'XHTML', 'C', 'CLASS', 'CPP', 'CS',
               'H', 'JAVA', 'SH', 'SWIFT', 'VB', 'BAK', 'CAB', 'CFG', 'CPL', 'CUR', 'DLL', 'DMP', 'DRV', 'ICNS', 'ICO',
               'INI', 'LNK', 'MSI', 'SYS', 'TMP', '7Z', '7ZIP', 'ARJ', 'PKG', 'RAR', 'RPM', 'TAR.GZ', 'GZ', 'ZIP', 'TAR', 'BZIP']
    image = ['AI', 'BMP', 'GIF', 'ICO', 'JPEG', 'JPG', 'JPE', 'PNG', 'PS', 'PSD', 'SVG', 'TIF', 'TIFF']
    presentation = ['KEY', 'ODP', 'PPS', 'PPT', 'PPTX']
    spreadsheet = ['ODS', 'XLR', 'XLS', 'XLSX' ]
    video = ['3G2', '3GP', 'AVI', 'FLV', 'H264', 'M4V', 'MKV', 'MOV', 'MP4', 'MPG', 'MPE', 'MPEG', 'RM', 'SWF', 'VOB', 'WMV']
    document = ['DOC', 'DOT', 'DOCX', 'ODT', 'PDF', 'RTF', 'TEX', 'TXT', 'WKS', 'WPS', 'WPD']
    exte = exte.upper()
    if exte in audio:
        return "Audio"
    elif exte in image:
        return "Image"
    elif exte in disk_image:
        return "Disk Image"
    elif exte in data_source:
        return "Data Source"
    elif exte in presentation:
        return "Presentation"
    elif exte in spreadsheet:
        return "Spreadsheet"
    elif exte in video:
        return "Video"
    elif exte in document:
        return "Document"
    elif exte in nothing:
        return ""
    else:
        return "Unknown"


def high(exte):
    archive = ['7Z', '7ZIP', 'ARJ', 'PKG', 'RAR', 'RPM', 'TAR.GZ', 'GZ', 'ZIP', 'TAR', 'BZIP']
    media = ['AIF', 'CDA', 'MID', 'MIDI', 'MP3', 'MPA', 'OGG', 'WAV', 'WMA', 'WPL', 'M3U', 'PLS', 'BIN', 'DMG', 'ISO',
             'TOAST', 'VCD', 'VMDK', 'AI', 'BMP', 'GIF', 'ICO', 'JPEG', 'JPG', 'JPE', 'PNG', 'PS', 'PSD', 'SVG', 'TIF',
             'TIFF', '3G2', '3GP', 'AVI', 'FLV', 'H264', 'M4V', 'MKV', 'MOV', 'MP4', 'MPG', 'MPE', 'MPEG', 'RM', 'SWF',
             'VOB', 'WMV' ]
    data = ['DAT', 'DB', 'DBF', 'MDF', 'SAV', 'SQL', 'XML']
    executable = ['APK', 'BAT', 'BIN', 'CGI', 'PL', 'COM', 'EXE', 'GADGET', 'JAR', 'PY', 'WSF', 'VBS', 'TASK', 'CMD']
    font = ['FNT', 'FON', 'OTF', 'TTF', 'WOFF', 'WOFF2']
    internet = ['ASP', 'ASPX', 'CER', 'CFM', 'CGI', 'PL', 'CSS', 'HTML', 'HTML', 'JS', 'JSP', 'PART', 'PHP', 'PHTML',
                'PHP3', 'PHP4', 'PHP5', 'PY', 'RSS', 'XHTML']
    document = ['KEY', 'ODP', 'PPS', 'PPT', 'PPTX', 'ODS', 'XLR', 'XLS', 'XLSX', 'DOC', 'DOT', 'DOCX', 'ODT', 'PDF', 'RTF', 'TEX', 'TXT', 'WKS', 'WPS', 'WPD']
    sourcecode = ['C', 'CLASS', 'CPP', 'CS', 'H', 'JAVA', 'SH', 'SWIFT', 'VB']
    systemfile = ['BAK', 'CAB', 'CFG', 'CPL', 'CUR', 'DLL', 'DMP', 'DRV', 'ICNS', 'ICO', 'INI', 'LNK', 'MSI', 'SYS', 'TMP']

    exte = exte.upper()
    if exte in archive:
        return "Archive"
    elif exte in media:
        return "Media Files"
    elif exte in data:
        return "Data Source"
    elif exte in executable:
        return "Executable File"
    elif exte in font:
        return "Font File"
    elif exte in internet:
        return "Internet File"
    elif exte in sourcecode:
        return "Source Code"
    elif exte in document:
        return "Document"
    elif exte in systemfile:
        return "System File"
    else:
        return "Unknown"


def deleted(default=0):
    return default


class File:
    file_name = None
    file_path = None
    file_size = 0
    file_created = None
    file_modified = None
    file_accessed = None
    file_hash = None
    file_extension = None
    file_deleted = None
    file_typehigh = None
    file_typelow = None


def collectdata():
    global dbis
    sql = dbname + '-datastore' + '.db'
    dbis = sql
    blank_db = _sqlite3.connect(sql)
    c = blank_db.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS metatable (file_name text, path blob, size real, last_modified blob, date_created blob, last_accessed blob, hash blob, file_extension blob, file_typehigh blob, file_typelow blob, file_deleted blob)')

    print(number)

    for i in range(0, number):
        try:
            j = File()
            print(i)
            j.file_path = globallists[i]
            j.file_name = getfiles(globallists[i])
            j.file_size = getsize(globallists[i])
            j.file_created = creationdate(globallists[i])
            j.file_modified = modificationdate(globallists[i])
            j.file_accessed = accessdate(globallists[i])
            j.file_hash = hash(globallists[i])
            j.file_extension = extension(globallists[i])
            j.file_typehigh = high(j.file_extension)
            j.file_typelow = low(j.file_extension)
            j.file_deleted = deleted()
            c.execute("INSERT INTO main.metatable (file_name, path, size, last_modified,date_created, last_accessed, hash, file_extension, file_typehigh, file_typelow, file_deleted) VALUES (?,?, ?, ?, ?,?, ?, ?,?, ?,?)", (str(j.file_name), j.file_path, str(j.file_size), j.file_modified, j.file_created, j.file_accessed, j.file_hash, j.file_extension, j.file_typehigh, j.file_typelow, j.file_deleted))
            blank_db.commit()
            c.execute("DELETE FROM main.metatable WHERE ROWID NOT IN (SELECT min(ROWID) FROM main.metatable GROUP BY main.metatable.file_name)")
            blank_db.commit()

        except(IOError, OSError):
            pass


if __name__ == '__main__':
    dbcreation()
    osname()
    print(os_name)
    a = getpath()
    print("The path to current directory is :"),
    print(a)
    print(getcount(a))
    getfiles(a)
    allpaths(a)
    collectdata()



