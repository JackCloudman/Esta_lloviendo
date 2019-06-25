import os
from dotenv import load_dotenv,find_dotenv
import telebot
from parser import Parser
load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")
URL = os.getenv("URL")
bot = telebot.TeleBot("TOKEN")
parser = Parser(URL)
print(parser.parse())
