#-*-coding=utf-8-*-

def new_update_dict(dict1,dict2):
    if not isinstance(dict1,dict) or not isinstance(dict2,dict):  
        return dict1
    for key,value in dict1.items():
        if key in dict2.keys():
            if isinstance(dict1[key],dict) and isinstance(dict2[key],dict):
                new_update_dict(dict1[key],dict2[key])
            else:
                dict1[key] = dict2[key]
        else:
            pass
    for key,value in dict2.items():
        if key not in dict1.keys():
            dict1[key] = value
    return dict1

if __name__ == "__main__":
    dict1 = {'component': {'description': u'\u9999\u5e72\u7092\u814a\u8089', 'componentType': 'item', 'picUrl': [{'1': u'jiachangcai/1001.jpg'}], 'ispepery': '0', 'action': None, 'id': '1', 'name': u'\u814a\u8089\u9999\u5e72'}}
    dict2 = {'width': 100, 'component': {'original_price': '28.0', 'description': u'description\u9999\u5e72\u7092\u814a\u8089', 'price': '28.0', 'componentType': 'item', 'ispepery': 1, 'action': None, 'id': '1'}, 'height': 100}
    new_dict = new_update_dict(dict1,dict2)
    print new_dict
