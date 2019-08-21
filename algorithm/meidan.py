def median(data):
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half]) / 2
