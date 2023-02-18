import vk
import time

api = vk.UserAPI(
    user_login='',
    user_password='',
    scope='',
    v='5.131'
)

for i in range(0, 6001, 1000):
    l = api.groups.getMembers(group_id='159981119', # group id
                              sort="id_desc",
                              count="1000",
                              offset=str(i)) # number per 1 step, max 1000
    with open('ids.txt', 'a') as fp:
        for item in l['items']:
            fp.write("%s\n" % item)
        print('Done ' + str(i / 1000))
    time.sleep(2)

IDS = open('ids.txt', 'r')
Lines = IDS.readlines()

for line in Lines:
    try:
        sta = api.status.get(user_id=line.strip())
        if sta['text']:
            file_object = open('status.txt', 'a', encoding="utf-16")
            file_object.write(sta['text'] + "\n")
            file_object.close()
    except Exception:
        pass
