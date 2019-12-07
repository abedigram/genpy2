def read_from_file(param):
    """
    read data points from csv
    :return: array of data
    """
    f = open('Dataset/Dataset'+param+'.csv', 'r')
    f.readline()
    two_dim_points = []

    line = ''
    while True:
        line = f.readline()
        if line:
            two_dim_points.append([float(i) for i in line[:len(line)-1].split(',')])
        else:
            break

    return two_dim_points
