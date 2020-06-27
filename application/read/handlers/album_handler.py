from albums.albums.application.use_cases import exists_album, get_albums_of_artist, get_albums_of_artist, get_tracks_of_album
from infraestructure.sqlserver_repository_album import SqlServerAlbumRepository
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from artists.artists.domain.exceptions import ArtistNotExistsException, DataBaseException
from infraestructure.sqlserver_repository_artist import SqlServerArtistRepository
from artists.artists.application.use_cases import exists_artist
from albums.albums.domain.exceptions import AlbumNotExistsException
class AlbumsOfArtistHandler(Resource):
    def get(self,idArtist):    
        try:
            usecase_exists_artist = exists_artist.ExistsArtist(SqlServerArtistRepository())
            dtoclass_artist = exists_artist.ExistsArtistInputDto(idArtist)
            usecase_exists_artist.execute(dtoclass_artist)

            usecase = get_albums_of_artist.GetAlbumsOfArtist(SqlServerAlbumRepository())
            dtoclass = get_albums_of_artist.GetAlbumsOfArtistInputDto(idArtist)
            list_albums = usecase.execute(dtoclass)

            return jsonify([ob.to_json() for ob in list_albums])

        except ArtistNotExistsException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 400
            return response  
        except DataBaseException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 500
            return response

class TracksOfAlbumHandler(Resource):
    def get(self, idAlbum):
        try:
            usecase_exist_album = exists_album.ExistsAlbum(SqlServerAlbumRepository())
            dtoclass_album = exists_album.ExistsAlbumInputDto(idAlbum)
            list_tracks = usecase_exist_album.execute(dtoclass_album)

            usecase = get_tracks_of_album.GetTracksOfAlbum(SqlServerAlbumRepository())
            dtoclass = get_tracks_of_album.GetTracksOfAlbumInputDto(idAlbum)
            list_albums = usecase.execute(dtoclass)

            return jsonify([ob.to_json() for ob in list_albums])
            
        except AlbumNotExistsException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 400
            return response 
        except DataBaseException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 500
            return response