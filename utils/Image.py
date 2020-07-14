import sys
sys.path.append("")
import base64
import config

class Image:
    @classmethod
    def save_image(cls, imageEncode:str, nameFile:str, typeImage:str):
        path = cls.get_path(cls,typeImage)
        if path:
            imageDecode = base64.decodestring(imageEncode.encode())
            newPath = "{0}/{1}".format(path,nameFile)
            image_save = open(newPath, "wb")
            image_save.write(imageDecode)
            return True
        else: 
            return False
        


    def get_path(self, typeImage:str):
        if typeImage == 'Playlist':
            return config.PLAYLISTS_DIR
        if typeImage == 'Album':
            return config.ALBUMS_DIR
        if typeImage == 'Artist':
            return config.ARTISTS_DIR
        
