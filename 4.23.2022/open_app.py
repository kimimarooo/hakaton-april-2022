import math
data_all_user = [[55.0234, 46.3745, [0, 1, 1, 0, 1, 0, 0, 0, 0, 0]], [47.5319, 53.2488, [0, 1, 1, 0, 0, 1, 0, 1, 1, 0]], [47.5319, 53.2488, [1, 0, 0, 1, 1, 1, 0, 0, 0, 1]]]
data_some_user = [54.0022, 47.0004, [0, 1, 1, 0, 0, 0, 1, 1, 1, 0]]


def Checking_interests(data_all_user, data_some_user):
    Interests_rezult = []
    raw_data = []
    for i in range(len(data_all_user)):
        raw_data.clear()
        for j in range(len(data_all_user[i][2])):
            if data_all_user[i][2][j] == data_some_user[2][j] and data_all_user[i][2][j] != 0:
                raw_data.append([True, j])
        Interests_rezult.append(list(raw_data))
    return Interests_rezult


def Checking_location(data_all_user, data_some_user):
    radius_size = 1000



dist = 1000
mylon = 51.5289156201 # долгота центра
mylat = 46.0209384922 # широта
lon1 = mylon - dist / abs(math.cos(math.radians(mylat)) * 111.0)  # 1 градус широты = 111 км
lon2 = mylon + dist / abs(math.cos(math.radians(mylat)) * 111.0)
lat1 = mylat - (dist / 111.0)
lat2 = mylat + (dist / 111.0)
print(lat1 , lon1, lat2, lon2)
print(Checking_interests(data_all_user, data_some_user))
