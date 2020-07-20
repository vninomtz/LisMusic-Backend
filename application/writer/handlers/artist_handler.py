import sys
sys.path.append("../../")
from artists.artists.application.use_cases import create_artist, update_artist, delete_artist
from infraestructure.sqlserver_repository_artist import SqlServerArtistRepository
import datetime
from artists.artists.domain.artist import Artist
from artists.artists.domain.exceptions import DataBaseException, ArtistNotExistsException, ArtistInvalidException
from flask import Flask, request, jsonify
from flask_restful import Resource


class ArtistHandler(Resource):
    def post(self):
        print("Creating artist...")
        usecase = create_artist.CreateArtist(SqlServerArtistRepository())
        dtoclass = create_artist.CreateArtistInputDto(
            request.json["name"],
            request.json["cover"],
            request.json["description"],
            request.json["idAccount"],
        )     
        try:
            artist = usecase.execute(dtoclass)
            if artist:
                return artist.to_json(), 200
        except ArtistInvalidException as ex: 
            return {"error": str(ex)}, 400
        except DataBaseException as ex: 
            return {"error": str(ex)}, 500 
       
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
                return {"message": "Artist successfully updated."}, 200

        except ArtistNotExistsException as ex:
            return {"error": str(ex)}, 404
        except DataBaseException as ex:
            return {"error": str(ex)}, 500

    def delete(self):
        print("Deleting artist...")
        usecase = delete_artist.DeleteArtist(SqlServerArtistRepository())
        dtoclass = delete_artist.DeleteArtistInputDto(request.json["idArtist"])
        try:
            result = usecase.execute(dtoclass)
            if result:
                return {"message": "Artist successfully deleted."}, 200
        except ArtistInvalidException as ex:
            return {"error": str(ex)}, 400
        except ArtistNotExistsException as ex:
            return {"error": str(ex)}, 404
        except DataBaseException as ex:
            return {"error": str(ex)}, 500

