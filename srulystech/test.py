from app import Post,db
#p = Post(title='duck say quack',picture='quack.jpg',description='quack quack quaaaack quack quack quaccckkk quack quack')
# # cards = {
# #     'DownTube':{'title':'DownTube','pic':'tube.jpg','description':'a full fledged youtube downloader with support for searching youtube and realtime progressbars','updated':'7/13/9098'},
# #     'inspiration':{'title':'inspiraitional thing','pic':None,'description':'haha just kidding nothing inspirational here ','updated':'02/06/9038'},'commingSoon':{'title':'Comming soon..','pic':'soon.png','description':'somthings comming soon somthing big','updated':'7/12/4598'},
# #     'duck':{'title':'duck say quack','pic':'quack.jpg','description':'quack quack quaaaack quack quack quaccckkk quack quack ','updated':'02/06/9038'})
# db.session.add(p)
# db.session.commit()
for post in Post.query.all():
    print(post.title)