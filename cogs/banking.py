import discord
from discord.ext import commands
import os
import json
import time

'''
Banking

Users all start with $0

Command:
    $daily -> every 24 hours get $500
    $shop ? 
    $pay {user} {amount}
    $cf, $coinflip -> spin a coin -> heads / tails {betting ammount} -> random 0,1 if 0 - head , 1 tails
'''