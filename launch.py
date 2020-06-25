


import zipfile
import urllib.request
import hashlib
import os
import shutil

#https://www.programiz.com/python-programming/examples/hash-file
def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

print("Downloading file")
urllib.request.urlretrieve("https://dl.nwjs.io/v0.46.3/nwjs-v0.46.3-win-ia32.zip", "nwjs-v0.46.3-win-ia32.zip")

print("File downloaded")
print("Checking hash")



if hash_file("nwjs-v0.46.3-win-ia32.zip") != "2f1466850d63821f31390c034f23b37f4d6a60ff":
    print("Incorrect hash")
    print("Stopping")
else:
    print("Hash correct")
    
    print("Unzip nwjs")    
    with zipfile.ZipFile("nwjs-v0.46.3-win-ia32.zip", 'r') as archive:
        archive.extractall()
        
    print("Unzip finished")  
    
    print("Removing old files")  
    os.remove("d3dcompiler_47.dll")
    os.remove("ffmpegsumo.dll")
    os.remove("icudtl.dat")
    os.remove("Learn Japanese To Survive - Hiragana Battle.exe")
    os.remove("libEGL.dll")
    os.remove("libGLESv2.dll")
    os.remove("nw.pak")
    os.remove("package (1).json")
    os.remove("pdf.dll")
    shutil.rmtree("locales")  
    print("Files Removed")
    
    
    print("Add new files")
    dirs = os.listdir( "nwjs-v0.46.3-win-ia32" )
    for file in dirs:
        if(os.path.isfile("nwjs-v0.46.3-win-ia32/"+file)):
            shutil.copyfile("nwjs-v0.46.3-win-ia32/"+file, "./" + file)
        else:
            shutil.copytree("nwjs-v0.46.3-win-ia32/"+file, "./" + file)    
        
    print("File added")

    print("Edit Files")
    os.rename('nw.exe', 'Learn Japanese To Survive - Hiragana Battle.exe')
    
    file = open("www/js/rpg_managers.js", 'r')
    content = file.read();
    content = content.replace("""StorageManager.localFileDirectoryPath = function() {
    var path = window.location.pathname.replace(/(\/www|)\/[^\/]*$/, '/save/');
    if (path.match(/^\/([A-Z]\:)/)) {
        path = path.slice(1);
    }
    return decodeURIComponent(path);
};""", """StorageManager.localFileDirectoryPath = function() {
    var path = require('path');
    return path.dirname(process.execPath) + "/save/";
};""")
    file.close()
    
    file = open("www/js/rpg_managers.js", 'w')
    file.write(content)
    file.close()
    
    print("Files Edited")

    print("Clear temp files and dirs")   
    shutil.rmtree("nwjs-v0.46.3-win-ia32")  
    os.remove("nwjs-v0.46.3-win-ia32.zip")
    print("Clear temp files and dirs")   
    
    
    
    print("\n\n\nGame updated")   
    
    