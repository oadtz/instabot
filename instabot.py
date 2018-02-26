from src import InstaBot

bot = InstaBot('behappynerd', 'pip2finn',\
               like_per_day=1000,\
               media_max_like=50,\
               media_min_like=5,\
               tag_list=['กันดั้ม', 'กันพลา', 'โมเดล', 'ของเล่น', 'ของสะสม', 'gundam', 'bandai', 'gunpla', 'gundamthailand', 'starwars', 'japan', 'gundamfront', 'gundambase', 'hbuc', 'hgbf', 'gunplathailand', 'toy', 'hobbby', 'gundammodelkits', 'gunplamodelkits', 'mobilesuit', 'mobilesuitgundam'],\
               max_like_for_one_tag=100,\
               follow_per_day=500,\
               unfollow_per_day=100,\
               comments_per_day=100,\
               comment_list=[['coool', 'great shot', 'superb', 'cool', 'fantastic'], ['❤❤❤❤', '!!!!!', '...']],\
               log_mod=1)
bot.auto_mod()
