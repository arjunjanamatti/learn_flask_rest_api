from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import werkzeug

app = Flask(__name__)
api = Api(app=app)

# will make first resource
# name_dict = {'arjun': {'edu': 'grad', 'country': 'India'},
#              'aj': {'edu': 'under-grad', 'country': 'UK'}}

video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help='Name of the video')
video_put_args.add_argument('views', type=int, help='Views of the video')
video_put_args.add_argument('likes', type=int, help='Likes on the video')

videos = {}


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        return {video_id: args}


api.add_resource(Video, '/info/<int:video_id>')

if __name__ == '__main__':
    app.run(debug=True)