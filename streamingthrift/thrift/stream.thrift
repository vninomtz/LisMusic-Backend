/*
*   Copyright 2020 Alan González Heredia and Victor Manuel Niño Martínez
*
*   Licensed under the Apache License, Version 2.0 (the "License");
*   you may not use this file except in compliance with the License.
*   You may obtain a copy of the License at
*
*   http://www.apache.org/licenses/LICENSE-2.0
*
*   Unless required by applicable law or agreed to in writing, software
*   distributed under the License is distributed on an "AS IS" BASIS,
*   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
*   See the License for the specific language governing permissions and
*   limitations under the License.
*/

/** Apache Thrift IDL definition for the LisMusic Streaming service
 */

enum Quality{
    HIGH = 0,
    MIDDLE = 1,
    LOW = 2,
}

struct TrackRequest{
    1: string fileName
    2: Quality quality
}

struct TrackUploaded{
    1: string fileName
}

struct TrackAudio{
    1: string idTrack
    2: string trackName
    3: binary audio

}

service StreamingService {
    TrackAudio GetTrackAudio(1: TrackRequest trackRequest)
    TrackUploaded UploadTrack(1: TrackAudio trackAudio)
    TrackUploaded UploadPersonalTrack(1: TrackAudio trackAudio)
}

