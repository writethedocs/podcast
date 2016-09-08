from feedgen.feed import FeedGenerator

fg = FeedGenerator()
fg.load_extension('podcast')

# Meta
fg.id('http://podcast.writethedocs.org/')
fg.title('Write the Docs Podcast')
fg.author({'name': 'Eric Holscher', 'email': 'eric@writethedocs.org'})
#fg.link(href='', rel='alternate')
fg.logo('http://conf.writethedocs.org/img/stickers/sticker-wtd-colors.png')
fg.subtitle('All things documentation')
fg.link(href='http://podcast.writethedocs.org/rss.xml', rel='self')
fg.language('en')

# Podcast Meta
fg.podcast.itunes_category('Technology')
fg.podcast.itunes_image('http://conf.writethedocs.org/img/stickers/sticker-wtd-colors.png')
fg.podcast.itunes_owner(name='Eric Holscher', email='eric@writethedocs.org')
fg.podcast.itunes_summary('A podcast about all things documentation')

# Entries
fe = fg.add_entry()
fe.id('http://podcast.writethedocs.org/episodes/heidi-waterhouse.html')
fe.title('Episode One: Heidi Waterhouse')
fe.enclosure(url='')

# Write
fg.rss_str(pretty=True)
fg.rss_file('rss.xml')
