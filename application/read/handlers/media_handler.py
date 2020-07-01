from flask import send_from_directory
from flask_restful import Resource
import os
import config

class MediaHandler(Resource):
    def get(self,nameFile):
        return send_from_directory(config.MEDIA_DIR, nameFile)

class MediaAlbumsHandler(Resource):
    def get(self,nameFile):
        return send_from_directory(config.ALBUMS_DIR, nameFile)

class MediaPlaylistsHandler(Resource):
    def get(self,nameFile):
        return send_from_directory(config.PLAYLISTS_DIR, nameFile)

class MediaArtistsHandler(Resource):
    def get(self,fileName):
        return send_from_directory(config.ARTISTS_DIR, fileName)