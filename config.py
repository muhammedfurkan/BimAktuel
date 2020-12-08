# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# (c) Muhammed Furkan http://t.me/B_Azade
import os


class Config():
    APP_ID = os.environ.get('APP_ID', None)
    APP_HASH = os.environ.get("APP_HASH", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
