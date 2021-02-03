from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app=app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_temp/database.db'
sql_db = SQLAlchemy(app=app)


class VideoModel(sql_db.Model):
    id = sql_db.Column(sql_db.Integer, primary_key=True)
    name = sql_db.Column(sql_db.String(100), nullable=False)
    views = sql_db.Column(sql_db.Integer, nullable=False)
    likes = sql_db.Column(sql_db.Integer, nullable=False)

    def __repr__(self):
        return f'Video(name = {name}, views = {views}, likes = {likes} '
    
# sql_db.create_all()


video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help='Name of the video', required=True)
video_put_args.add_argument('views', type=int, help='Views of the video', required=True)
video_put_args.add_argument('likes', type=int, help='Likes on the video', required=True)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer,
}


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id = video_id).first()
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        video = VideoModel(id=video_id, name = args['name'], views = args['views'], likes = args['likes'])
        sql_db.session.add(video)
        sql_db.session.commit()
        return video

    def delete(self, video_id):
        abort_id_not_exist(video_id)
        del videos[video_id]
        pass


api.add_resource(Video, '/info/<int:video_id>')

if __name__ == '__main__':
    app.run(debug=True)