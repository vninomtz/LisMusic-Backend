import sys
sys.path.append("../../")
from artists.artists.application.use_cases import create_artist, update_artist, delete_artist
from infraestructure.sqlserver_repository_artist import SqlServerArtistRepository
import datetime
from artists.artists.domain.artist import Artist
from artists.artists.domain.exceptions import DataBaseException, ArtistNotExistsException, ArtistInvalidException
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

class ArtistHandler(Resource):
    def post(self):
        print("Creating artist...")
        usecase = create_artist.CreateArtist(SqlServerArtistRepository())
        dtoclass = create_artist.CreateArtistInputDto(
            request.json["name"],
            request.json["cover"],
            request.json["description"],
        )     
        try:
            result = usecase.execute(dtoclass)
            if result:
                response = jsonify(result.to_json())
                response.status_code = 200
                return response
        except DataBaseException as ex: 
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 500
            return response

    def put(self):
        print("Updating artist")
        usecase = update_artist.UpdateArtist(SqlServerArtistRepository())
        dtoclass = update_artist.UpdateArtistInputDto(
            request.json["idArtist"],
            request.json["name"],
            request.json["cover"],
            request.json["description"],
        )


        try:
            result = usecase.execute(dtoclass)
            if result:
                response = jsonify({'message': 'Artist successfully updated'})
                response.status_code = 204
                return response

        except ArtistNotExistsException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 404
            return response
        except DataBaseException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 500
            return response

    def delete(self):
        print("Deleting artist...")
        usecase = delete_artist.DeleteArtist(SqlServerArtistRepository())
        dtoclass = delete_artist.DeleteArtistInputDto(request.json["idArtist"])
        try:
            result = usecase.execute(dtoclass)
            if result:
                response = jsonify({'message': 'Artist successfully deleted'})
                response.status_code = 204
                return response
        except ArtistInvalidException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 400
            return response
        except ArtistNotExistsException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 404
            return response
        except DataBaseException as ex:
            error = str(ex)
            response = jsonify({'error': error})
            response.status_code = 500
            return response

