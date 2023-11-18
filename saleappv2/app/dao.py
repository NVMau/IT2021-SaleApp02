from itertools import product


def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    },
        {
            'id': 2,
            'name': 'Tablet'
        }
    ]
def load_products(kw = None):
    products = [{
        "id": 1,
        "name": "Iphone 15 Pro Max",
        "price": 20000000,
        "image":"https://cdn.tgdd.vn/Products/Images/42/305658/iphone-15-pro-max-blue-thumbnew-200x200.jpg"
    },
        {
            "id": 2,
            "name": "Iphone 15 Pro Max",
            "price": 20000000,
            "image": "https://cdn.tgdd.vn/Products/Images/42/305658/iphone-15-pro-max-blue-thumbnew-200x200.jpg"
        },
        {
            "id": 3,
            "name": "Iphone 15 Pro Max",
            "price": 20000000,
            "image": "https://cdn.tgdd.vn/Products/Images/42/305658/iphone-15-pro-max-blue-thumbnew-200x200.jpg"
        },{
            "id": 4,
            "name": "Ipad mini 2",
            "price": 20000000,
            "image": "https://cdn.tgdd.vn/Products/Images/42/305658/iphone-15-pro-max-blue-thumbnew-200x200.jpg"
        },{
            "id": 5,
            "name": "Ipad 10",
            "price": 20000000,
            "image": "https://cdn.tgdd.vn/Products/Images/42/305658/iphone-15-pro-max-blue-thumbnew-200x200.jpg"
        },]
    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]
    return products




