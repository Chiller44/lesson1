import user

user.new('Mark', '1234')
user.auth('Mark', '1234')
user.block('Mark')

import user as user_account
from user import new

user_account.new('Mark', '1234')
user_account.auth('Mark', '1234')
user_account.block('Mark')

new('Mark', '1234')
user_account.auth('Mark', '1234')
user_account.block('Mark')

from user import *

new('Mark', '1234')

import user.admin as admim

admin.new("")