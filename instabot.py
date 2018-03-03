from os.path import join, dirname
from dotenv import load_dotenv
from src import InstaBot
import os

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

bot = InstaBot(os.getenv("IG_USER"),\
               os.getenv("IG_PASSWORD"),\
               like_per_day=int(os.getenv("LIKE_PER_DAY")),\
               media_max_like=int(os.getenv("MEDIA_MAX_LIKE")),\
               media_min_like=int(os.getenv("MEDIA_MIN_LIKE")),\
               tag_list=os.getenv("TAG_LIST").split(","),\
               max_like_for_one_tag=int(os.getenv("MAX_LIKE_FOR_ONE_TAG")),\
               follow_per_day=int(os.getenv("FOLLOW_PER_DAY")),\
               unfollow_per_day=int(os.getenv("UNFOLLOW_PER_DAY")),\
               comments_per_day=int(os.getenv("COMMENTS_PER_DAY")),\
               comment_list=[['coool', 'great shot', 'superb', 'cool', 'fantastic'], ['❤❤❤❤', '!!!!!', '...']],\
               log_mod=int(os.getenv("LOG_MODE")))
bot.auto_mod()
