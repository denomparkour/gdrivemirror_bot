#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Atul-Kadian

class Text(object):
	GREET_USER = "Hello {}!\nI am GDrive Mirror Bot kanged by @thedenomparkour. Just send me any direct download link and I'll send you the GDrive Mirror of that file.\nNot only this, I can send you the GDrive link of YouTube videos and even can extract high quality audio from them.\n\nUse /help command to get started."
	PROCESSING = "Processing your request..."
	VERIFYING_URL = "Verifying the link..."
	UPLOADING_GD = "Downloaded.\nNow uploading to Google Drive and invoking permissions..."
	UPLOADING_TG = "Downloaded and processed\nNow uploading the file to Telegram..."
	DONE = "Request completed successfully!!\n\n<b>Filename :</b> {}\n<b>Size :</b> {}mb\n<b>GDrive Mirror :</b> {}"
	FAILED = "Some error occured. Couldn't proceed further :(\n\n<b>Possible reasons and/or workarounds :</b> \n• The link doesn't contain a file and/or redirects to a webpage.\n• You didn't use correct parameter with the link.(Use /help)\n• Link not supported, you can try transloading your file. (Use /help) \n\n<b>Please consider reporting it here</b> @aicp_whyred <b>with your link.</b>"
	MAXLIMITEXCEEDED = "Maximium file limit exceeded.\nTry sending file with filesize less than 10GB."
	RETARD = "Stop being a retard 😑\nGo find someone else. I'm not built for chatting."
	TELL_ADMIN = "Sir,\nA new user just joined :)"
	HELP = "<b>Some features :</b>\n• Create GDrive mirror of direct download links.\n• Download highest quality video from YouTube.<i>(Sometimes highest quality doesn't contain audio, blame youtube for that :D.)</i>\n• Extract high quality music from YouTube videos.\n• Download videos from <a href = 'http://rg3.github.io/youtube-dl/supportedsites.html'>1000+ websites</a> .\n• Set custom filename to a file.\n\n<b>To create GDrive Mirror, send :</b>\n<code>download_link</code>\n<b>To create GDrive Mirror with custom filename, send :</b>\n<code>your_filename | download_link</code>\n<b>To download video from a link, send :</b> \n<code>video | video_link</code>\n<b>To extract audio from a youtube link, send :</b>\n<code>audio | youtube_link</code>\n\n<b>If your requested link failed</b>, send your link to <a href = 'https://atul-engine2.herokuapp.com'>atul-engine2</a> <i>(just click on save configuration if it asks for any)</i> and after transloading send your link again to the bot."
	DONATE = "Thank You for supporting 🥰"
	UNAUTHORIZED_CMD = "You're not authorized to use this command."
	UNAUTHORIZED_USR = "You aren't authorized to use this bot. The service is not free anymore. \n\nUse /help command to check more details and pricing.."
	NOT_SUPPORTED = "Your request couldn't be processed from this source."
	BUSY = "Currently all the threads are busy. Please try after sometime."
	NOT_USER = "User not found in the database."
	OLD_USER = "User already exists."
	ADDED_USER = "New user added successfully to the database."
	REVOKED_USER = "User successfully revoked from database."
	ISNOT_DOWNLOADABLE = "Please check your link again. The link does not contain any file or redirects to a webpage."
