Classes
=======

.. automodule:: qmusic

.. autoclass:: qmusic.Qmusic
	:members: get_channel
.. autoclass:: qmusic.Channel
	:members: current_song, next_song, color, slug, background_image, name, station_id, logo, streams, search_terms
.. autoclass:: qmusic.Streams
	:members: aac, mp3, video, hls, radioplayer_id, mobile, android, iphone
.. autoclass:: qmusic.Mobile
	:members: audio, video, live
.. autoclass:: qmusic.Android
	:members: high, low, video
.. autoclass:: qmusic.Iphone
	:members: live, video
.. autoclass:: qmusic.Stream
	:members: source, extra
.. autoclass:: qmusic.Logo
	:members: active_android_url, active_iphone_url, inactive_android_url, inactive_iphone_url, app_card, app_player_bg_phone, app_player_bg_tablet, app_player_icon, app_player_thumbnail, app_player_small, app_player_header, app_square, appletv_background, app_messages_avatar, radioplayer_cover, radioplayer_banner, site_logo, site_background, homepage_banner
.. autoclass:: qmusic.Color
	:members: background, foreground, extra
.. autoclass:: qmusic.Song
	:members: played_at, slug, title, selector_code, release_year, affiliate_url, thumbnail_url, spotify_url, youtube_url, preview_url, artist, featuring_artists
.. autoclass:: qmusic.Artist
	:members: id_code, name_all_artist, name_main_artist, slug, bio, social_medias, photo, country_code, country_name
.. autoclass:: qmusic.Edition
	:members: song_position, release_year, name