def save_csv(data_frame, file):
    if data_frame is None:
        print("Nothing to save!")
        return
    
    data_frame.to_csv(file, index=False)