def process(data_frame):
    if data_frame is None:
        print("No data to process!")
        return None

    if "price" in data_frame.columns and "qty" in data_frame.columns:    
        data_frame["total"] = data_frame["price"] * data_frame["qty"]
    else:
        print("Columns 'price' or 'qty' not found!")
    
    return data_frame

