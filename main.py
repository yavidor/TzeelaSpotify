import requests

URL = 'https://api.spotify.com'
token = 'BQDXLRoZ2aJSEIvUdGabTfwbs48Rvi_EKOhRrp_i-qQtryvTA8xU00JXR6oDgZLE-nA_5Q5EpQcra4RxCohim77loqTdcwEbdQxVTRSPOAxvdlglJpGljPUxWP3awRKj8ZVxj1EKsF0cHFcLoviT5zx-HctLXxp0rFjCmU8HZSDmenJ7kj-1KLXTBmqXETs-N_G_WOr1AmVe-MScX1Bm_VQhwRcOvXUrmL9AE8B42oxPprAAOROdELEG5g2Ix9zDvXGdLRKnei3dPepB4c9c9iU9Xeo5GehV7RU8HOLs3wxVktkFPQ0YfJ_b_uW5NPgubZQnVyLIk9Fe'
auth = {'Authorization': f'Bearer {token}'}


def get_listened(items, nexturl):
    if len(items) == 0:
        url = f'{URL}/v1/me/player/recently-played'
    else:
        url = nexturl
    response = requests.get(url, headers=auth).json()
    # print(response)
    # print(response['cursors']['after'])
    items.extend(response['items'])
    if len(response['items']) == 0:
        return items
    return get_listened(items, response['next'])


def main():
    a = get_listened([], 0)
    print(len(a))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
