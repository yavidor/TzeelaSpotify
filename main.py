import requests
import pandas as pd
URL = 'https://api.spotify.com'
token = 'BQDXLRoZ2aJSEIvUdGabTfwbs48Rvi_EKOhRrp_i-qQtryvTA8xU00JXR6oDgZLE-nA_5Q5EpQcra4RxCohim77loqTdcwEbdQxVTRSPOAxvdlglJpGljPUxWP3awRKj8ZVxj1EKsF0cHFcLoviT5zx-HctLXxp0rFjCmU8HZSDmenJ7kj-1KLXTBmqXETs-N_G_WOr1AmVe-MScX1Bm_VQhwRcOvXUrmL9AE8B42oxPprAAOROdELEG5g2Ix9zDvXGdLRKnei3dPepB4c9c9iU9Xeo5GehV7RU8HOLs3wxVktkFPQ0YfJ_b_uW5NPgubZQnVyLIk9Fe'
auth = {'Authorization': f'Bearer {token}'}


def get_listened(items, nexturl):
    if len(items) == 0:
        url = f'{URL}/v1/me/player/recently-played?limit=50'
    else:
        url = nexturl
    response = requests.get(url, headers=auth).json()
    items.extend(response['items'])
    if len(response['items']) == 0:
        return items
    return get_listened(items, response['next'])


def extract_songs(items):
    songs_dict = {}
    for item in items:
        track_name = item['track']['name']
        if track_name not in songs_dict:
            songs_dict[track_name] = 0
        songs_dict[track_name] += int(item['track']['duration_ms']) * 60000
    return pd.DataFrame(list(songs_dict.items()),columns=['Name','Minutes'])


def main():
    track_list = get_listened([], 0)
    track_list = extract_songs(track_list)
    track_list.sort_values(by=['Minutes'])
    print(track_list)
    print(len(track_list))
    track_list.to_csv('file.csv')


if __name__ == '__main__':
    main()
