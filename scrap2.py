allchar = [
    'early-math',
    'arithmetic',
    'algebra',
    'geometry',
    'trigonometry',
    'statistics-probability',
    'calculus-home',
    'differential-equations',
    'linear-algebra',
    'math-for-fun-and-glory']

### -- all the big header you want

import csv


from api_models import *
khan = Khan(lang="en")

with open('kaca_exer.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['l0','l1','l2','n1','n2','u1','u2','video_title','png_id','exercise_id'])
    # creating the CSV file and wiring first line
    for e0 in allchar:
        print '~~~~~~~~~~~~~~'
        print 'e0 ', e0
        # - going first latyer in
        a = khan.get_topic(e0)
        for e1 in a['children']:
            print 'e1 ', e1['id']
            b = khan.get_topic(e1['id'])
            # - going second layer in
            for e2 in b['children']:
                print 'e2 ', e2['id']
                c = khan.get_topic_videos(e2['id'])
                c_exercise = khan.get_topic_exercises(e2['id'])
                # - going third layer in

                #print 'exercises....'
                for each in c_exercise:
                    image_url = each["image_url"]
                    ka_url = each["ka_url"]
                    vid_title = each["translated_title"]
                    # writing into CSV file
                    spamwriter.writerow([
                        e0.replace(',','').encode('utf-8'),
                        e1['id'].replace(',','').encode('utf-8'),
                        e2['id'].replace(',','').encode('utf-8'),
                        e1['title'].replace(',','').encode('utf-8'),
                        e2['title'].replace(',','').encode('utf-8'),
                        e1['url'].replace(',','').encode('utf-8'),
                        e2['url'].replace(',','').encode('utf-8'),
                        vid_title.replace(',','').encode('utf-8'),
                        image_url,
                        ka_url
                        ])
