import instagpy

insta = instagpy.InstaGPy()

post = insta.get_post_details('https://www.instagram.com/p/C7fHloFMVEA')
media = insta.get_media_url(post)
print(media)