from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app=app)

# will make first resource
# name_dict = {'arjun': {'edu': 'grad', 'country': 'India'},
#              'aj': {'edu': 'under-grad', 'country': 'UK'}}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help='Name of the video')
video_put_args.add_argument('views', type=int, help='Views of the video', required=True)
video_put_args.add_argument('likes', type=int, help='Likes on the video')

videos = {}


def abort_id_not_exist(video_id):
    if video_id not in videos:
        abort(404, message='Video ID is not found')


class Video(Resource):
    def get(self, video_id):
        abort_id_not_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id]


api.add_resource(Video, '/info/<int:video_id>')

if __name__ == '__main__':
    app.run(debug=True)