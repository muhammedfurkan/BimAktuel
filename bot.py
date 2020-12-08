# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# (c) Muhammed Furkan http://t.me/B_Azade
import asyncio
import logging
import os
import time

import requests
import telethon
import wget
from telethon import TelegramClient, errors, events, utils
from telethon.sync import TelegramClient
from telethon.tl import functions, types
from telethon.tl.custom import Button

from config import Config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


bot = TelegramClient('bimbot', Config.APP_ID, Config.APP_HASH).start(
    bot_token=Config.BOT_TOKEN)


def bim(num):
    kelime = "https://kolektifapi.herokuapp.com/bim"
    headers = {"USER-AGENT": "UniBorg"}
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(
        pool_connections=100,
        pool_maxsize=100
    )
    session.mount('http://', adapter)
    resp = session.get(kelime, headers=headers).json()
    tarih = resp['veri']['tarih']
    urunler = resp['veri']['urunler']
    if num == "1":
        urun_1 = urunler[0]
        return _extracted_from_bim_15(urunler, 0, tarih)
    elif num == "2":
        urun_2 = urunler[1]
        return _extracted_from_bim_15(urunler, 1, tarih)
    elif num == "3":
        urun_3 = urunler[2]
        return _extracted_from_bim_15(urunler, 2, tarih)
    elif num == "4":
        urun_4 = urunler[3]
        return _extracted_from_bim_15(urunler, 3, tarih)
    elif num == "5":
        urun_5 = urunler[4]
        return _extracted_from_bim_15(urunler, 4, tarih)
    elif num == "6":
        urun_6 = urunler[5]
        return _extracted_from_bim_15(urunler, 5, tarih)
    elif num == "7":
        urun_7 = urunler[6]
        return _extracted_from_bim_15(urunler, 6, tarih)
    elif num == "8":
        urun_8 = urunler[7]
        return _extracted_from_bim_15(urunler, 7, tarih)


def _extracted_from_bim_15(urunler, arg1, tarih):
    urun_1_baslik = urunler[arg1]['urun_baslik']
    urun_1_gorsel = urunler[arg1]['urun_gorsel']
    urun_1_fiyat = urunler[arg1]['urun_fiyat']
    resim_1 = wget.download(urun_1_gorsel)
    return urun_1_baslik, urun_1_fiyat, resim_1, tarih


markup = bot.build_reply_markup(
    [
        [
            Button.inline(text='1️⃣', data="1"),
            Button.inline(text='2️⃣', data="2"),
            Button.inline(text='3️⃣', data="3"),
            Button.inline(text='4️⃣', data="4")
        ],
        [
            Button.inline(text='5️⃣', data="5"),
            Button.inline(text='6️⃣', data="6"),
            Button.inline(text='7️⃣', data="7"),
            Button.inline(text='8️⃣', data="8")
        ],
        [
            Button.url(text='👤 Yapımcı', url="t.me/By_Azade"),
            Button.url(text='📍 Kanallar Gruplar', url="t.me/KanalLinkleri")
        ]
    ]
)


@bot.on(events.NewMessage(pattern="/start ?(.*)", func=lambda e: e.is_private))
async def start(event):
    x = await bot.send_message(
        event.chat_id,
        "BİM Aktuel'i Telegram Üzerinden Keşfetmek İçin Aşağıdaki Butonlara Tıklayarak Ürün Bilgisi Alabilirsiniz.",
        buttons=markup,
        file="./img/bim.jpg"
    )


@bot.on(events.CallbackQuery())
async def callback(event):
    if event.data.decode("utf-8") == "1":
        await event.answer('Güncelleniyor, çok uzun sürmez :)', alert=True)
        sonuc = bim(event.data.decode("utf-8"))
        sonuc_baslik = sonuc[0]
        sonuc_fiyat = sonuc[1]
        sonuc_img = sonuc[2]
        sonuc_tarih = sonuc[3]
        msg = f"**{sonuc_tarih} Tarihli Ürün**\n\n**Ürün:** {sonuc_baslik}\n**Fiyat:** {sonuc_fiyat}"
        mssg = await bot.send_message(
            event.sender_id,
            msg,
            file=sonuc_img,
            buttons=markup
        )
        os.remove(sonuc_img)

    if event.data.decode("utf-8") == "2":
        await event.answer('Güncelleniyor, çok uzun sürmez :)', alert=True)
        sonuc = bim(event.data.decode("utf-8"))
        sonuc_baslik = sonuc[0]
        sonuc_fiyat = sonuc[1]
        sonuc_img = sonuc[2]
        sonuc_tarih = sonuc[3]
        msg = f"**{sonuc_tarih} Tarihli Ürün**\n\n**Ürün:** {sonuc_baslik}\n**Fiyat:** {sonuc_fiyat}"
        mssg = await bot.edit_message(
            event.sender_id,
            event.query.msg_id,
            msg,
            file=sonuc_img,
            buttons=markup
        )
        os.remove(sonuc_img)

    if event.data.decode("utf-8") == "3":
        await event.answer('Güncelleniyor, çok uzun sürmez :)', alert=True)
        sonuc = bim(event.data.decode("utf-8"))
        sonuc_baslik = sonuc[0]
        sonuc_fiyat = sonuc[1]
        sonuc_img = sonuc[2]
        sonuc_tarih = sonuc[3]
        msg = f"**{sonuc_tarih} Tarihli Ürün**\n\n**Ürün:** {sonuc_baslik}\n**Fiyat:** {sonuc_fiyat}"
        mssg = await bot.edit_message(
            event.sender_id,
            event.query.msg_id,
            msg,
            file=sonuc_img,
            buttons=markup
        )
        os.remove(sonuc_img)

    if event.data.decode("utf-8") == "4":
        await event.answer('Güncelleniyor, çok uzun sürmez :)', alert=True)
        sonuc = bim(event.data.decode("utf-8"))
        sonuc_baslik = sonuc[0]
        sonuc_fiyat = sonuc[1]
        sonuc_img = sonuc[2]
        sonuc_tarih = sonuc[3]
        msg = f"**{sonuc_tarih} Tarihli Ürün**\n\n**Ürün:** {sonuc_baslik}\n**Fiyat:** {sonuc_fiyat}"
        mssg = await bot.edit_message(
            event.sender_id,
            event.query.msg_id,
            msg,
            file=sonuc_img,
            buttons=markup
        )
        os.remove(sonuc_img)

    if event.data.decode("utf-8") == "5":
        await event.answer('Güncelleniyor, çok uzun sürmez :)', alert=True)
        sonuc = bim(event.data.decode("utf-8"))
        sonuc_baslik = sonuc[0]
        sonuc_fiyat = sonuc[1]
        sonuc_img = sonuc[2]
        sonuc_tarih = sonuc[3]
        msg = f"**{sonuc_tarih} Tarihli Ürün**\n\n**Ürün:** {sonuc_baslik}\n**Fiyat:** {sonuc_fiyat}"
        mssg = await bot.edit_message(
            event.sender_id,
            event.query.msg_id,
            msg,
            file=sonuc_img,
            buttons=markup
        )
        os.remove(sonuc_img)

    if event.data.decode("utf-8") == "6":
        await event.answer('Güncelleniyor, çok uzun sürmez :)', alert=True)
        sonuc = bim(event.data.decode("utf-8"))
        sonuc_baslik = sonuc[0]
        sonuc_fiyat = sonuc[1]
        sonuc_img = sonuc[2]
        sonuc_tarih = sonuc[3]
        msg = f"**{sonuc_tarih} Tarihli Ürün**\n\n**Ürün:** {sonuc_baslik}\n**Fiyat:** {sonuc_fiyat}"
        mssg = await bot.edit_message(
            event.sender_id,
            event.query.msg_id,
            msg,
            file=sonuc_img,
            buttons=markup
        )
        os.remove(sonuc_img)

    if event.data.decode("utf-8") == "7":
        await event.answer('Güncelleniyor, çok uzun sürmez :)', alert=True)
        sonuc = bim(event.data.decode("utf-8"))
        sonuc_baslik = sonuc[0]
        sonuc_fiyat = sonuc[1]
        sonuc_img = sonuc[2]
        sonuc_tarih = sonuc[3]
        msg = f"**{sonuc_tarih} Tarihli Ürün**\n\n**Ürün:** {sonuc_baslik}\n**Fiyat:** {sonuc_fiyat}"
        mssg = await bot.edit_message(
            event.sender_id,
            event.query.msg_id,
            msg,
            file=sonuc_img,
            buttons=markup
        )
        os.remove(sonuc_img)

    if event.data.decode("utf-8") == "8":
        await event.answer('Güncelleniyor, çok uzun sürmez :)', alert=True)
        sonuc = bim(event.data.decode("utf-8"))
        sonuc_baslik = sonuc[0]
        sonuc_fiyat = sonuc[1]
        sonuc_img = sonuc[2]
        sonuc_tarih = sonuc[3]
        msg = f"**{sonuc_tarih} Tarihli Ürün**\n\n**Ürün:** {sonuc_baslik}\n**Fiyat:** {sonuc_fiyat}"
        mssg = await bot.edit_message(
            event.sender_id,
            event.query.msg_id,
            msg,
            file=sonuc_img,
            buttons=markup
        )
        os.remove(sonuc_img)


bot.start()
bot.run_until_disconnected()
