import sys
sys.path.append("../../")
from albums.albums.application.use_cases import create_album, update_album, delete_album, get_albums_by_id_artist
from infraestructure.sqlserver_repository_album import SqlServerAlbumRepository
import datetime
from albums.albums.domain.album import Album
from albums.albums.domain.exceptions import AlbumGenderInvalidException, AlbumInvalidException, AlbumNotExistsException, AlbumTracksInvalidException, AlbumTypeInvalidException, DataBaseException
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from artists.artists.domain.exceptions import ArtistInvalidException, ArtistNotExistsException
from infraestructure.sqlserver_repository_artist import SqlServerArtistRepository

class AlbumHandler(Resource):
    def post(self):
        print("Creating album...")
        usecase = create_album.CreateAlbum(SqlServerAlbumRepository(),SqlServerArtistRepository())
        dtoclass = create_album.CreateAlbumInputDto(
            request.json["title"],
            request.json["cover"],
            request.json["publication"],
            request.json["recordCompany"],
            request.json["idMusicGender"],
            request.json["idAlbumType"],
            request.json["idArtist"],
            request.json["tracks"]
        )
       
        try:
            result = usecase.execute(dtoclass)
            if result:
                response = jsonify(result.to_json())
                response.status_code = 201
                return response
        except DataBaseException as ex: 
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 500
            return response
        except AlbumInvalidException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 400
            return response
        except AlbumGenderInvalidException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 404
            return response
        except AlbumTypeInvalidException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 404
            return response
        except ArtistNotExistsException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 404
            return response
        except AlbumTracksInvalidException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 400
            return response

class AlbumsOfArtistHandler(Resource):
    def get(self,idArtist):
        usecase = get_albums_by_id_artist.GetAlbumsByIdArtist(SqlServerAlbumRepository(),SqlServerArtistRepository())
        dtoclass = get_albums_by_id_artist.GetAlbumsByIdArtistInputDto(idArtist)
        try:
            result = usecase.execute(dtoclass)
            print(result)
            return jsonify(result.replace("\'", ' '))
        except ArtistNotExistsException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 400
            return response                       



