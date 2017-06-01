allchar = [
    'geometry',
    'trigonometry',
    'statistics-probability',
    'calculus-home',
    'differential-equations',
    'linear-algebra',
    'math-for-fun-and-glory']

import csv


from api_models import *
khan = Khan(lang="en")

with open('kaca.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['l0','l1','l2','n1','n2','u1','u2','youtube_id','mp4_id', 'png_id'])
    for e0 in allchar:
        print '~~~~~~~~~~~~~~'
        print 'e0 ', e0
        a = khan.get_topic(e0)
        for e1 in a['children']:
            print 'e1 ', e1['id']
            b = khan.get_topic(e1['id'])
            for e2 in b['children']:
                print 'e2 ', e2['id']
                c = khan.get_topic_videos(e2['id'])
                for each in c:
                    youtube_id = "https://www.youtube.com/watch?v="+each["translated_youtube_id"]
                    mp4_id = each["download_urls"]["mp4"]
                    png_id = each["download_urls"]["png"]
                    spamwriter.writerow([e0,e1['id'],e2['id'],e1['title'],e2['title'],e1['url'],e2['url'],youtube_id,mp4_id,png_id])
