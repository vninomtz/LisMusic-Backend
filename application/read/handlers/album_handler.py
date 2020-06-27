from albums.albums.application.use_cases import get_albums_by_id_artist
from infraestructure.sqlserver_repository_album import SqlServerAlbumRepository
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from artists.artists.domain.exceptions import ArtistNotExistsException, DataBaseException
from infraestructure.sqlserver_repository_artist import SqlServerArtistRepository

class AlbumsOfArtistHandler(Resource):
    def get(self,idArtist):
        usecase = get_albums_by_id_artist.GetAlbumsByIdArtist(SqlServerAlbumRepository(),SqlServerArtistRepository())
        dtoclass = get_albums_by_id_artist.GetAlbumsByIdArtistInputDto(idArtist)
        try:
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