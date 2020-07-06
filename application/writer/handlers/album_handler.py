import sys
sys.path.append("../../")
from albums.albums.application.use_cases import create_album, update_album, delete_album, get_albums_of_artist
from infraestructure.sqlserver_repository_album import SqlServerAlbumRepository
import datetime
from albums.albums.domain.album import Album
from albums.albums.domain.exceptions import AlbumGenderInvalidException, AlbumInvalidException, AlbumNotExistsException, AlbumTracksInvalidException, AlbumTypeInvalidException, DataBaseException
from flask import Flask, request
from flask_restful import Resource
from artists.artists.domain.exceptions import ArtistInvalidException, ArtistNotExistsException
from infraestructure.sqlserver_repository_artist import SqlServerArtistRepository
from artists.artists.application.use_cases import exists_artist

class AlbumHandler(Resource):
    def post(self):
        print("Creating album...")
        usecase = create_album.CreateAlbum(SqlServerAlbumRepository())
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
            usecase_exists_artist = exists_artist.ExistsArtist(SqlServerArtistRepository())
            idartist = exists_artist.ExistsArtistInputDto(dtoclass.idArtist)
            usecase_exists_artist.execute(idartist)

            album = usecase.execute(dtoclass)
            return album.to_json(), 201

        except DataBaseException as ex: 
            return {"error": str(ex)}, 500
        except AlbumInvalidException as ex:
            return {"error": str(ex)}, 400 
        except AlbumGenderInvalidException as ex:
            return {"error": str(ex)}, 404
        except AlbumTypeInvalidException as ex:
            return {"error": str(ex)}, 404
        except ArtistNotExistsException as ex:
            return {"error": str(ex)}, 404
        except AlbumTracksInvalidException as ex:
            return {"error": str(ex)}, 400 
                 



