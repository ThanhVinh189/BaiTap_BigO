lst_demo = [
    {
        "id": 1,
        "value": [
            {
                "id": 2,
                "value": [
                    {
                        "id": 3,
                        "value": [
                            {
                                "id": 4,
                                "value": []
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": 5,
        "value": []
    }
]

def flatten_ids(data):
    result = []  
    for item in data:
        result.append({"id": item["id"]})  
        if "value" in item and item["value"]:  
            result.extend(flatten_ids(item["value"]))  
    return result

# Gọi hàm và in kết quả
flattened_list = flatten_ids(lst_demo)
print(flattened_list)
