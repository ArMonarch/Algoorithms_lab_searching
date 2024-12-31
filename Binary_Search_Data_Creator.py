import random

with open ("Binary_Search_Data.py", 'w+t') as Linear_Data:
    # write do not modify comments at the top of the file
    lines_list: list = []
    lines_list.append("# Do Not Modify This File\n")
    lines_list.append("# This file is generated by Binary_Search_Data_Creator.py for automatic data creation for testing binary_Search time_complexity\n")
    lines_list.append("\n")
    Linear_Data.writelines(lines_list)

    # create a dict of data for testing.
    # start
    # Linear_Data: dict = {
    # end
    # }
    data_dict_inti: str = "Binary_Search_Data: dict = {\n"
    data_dict_end: str = "}"

    # write data_dict_inti
    Linear_Data.write(data_dict_inti)

    # create unsorted list of 100, 1,000, 10,000, 100,000, 1,000,000, 2,000,000 ... 10,000,000 data
    # for 100, 100,000
    for index in range(2,6):
        data_list_inti = str(f'    "data_{pow(base=10, exp=index)}" : ')
        range_data = str ( list ( range (0,pow(base=10, exp=index)) ) )
        data_list:str = data_list_inti + range_data + ",\n"
        Linear_Data.write(data_list)
    
    # for 1M to 50M
    for index in range(0,6):
        data_list_inti = str(f'    "data_{0.5 * (index+1)}M" : ')
        range_data = str (  list ( range (0, (index+1) * 500000 ) ) )
        data_list: str = data_list_inti + range_data + ",\n"
        Linear_Data.write(data_list)

    # write data_dict_end
    Linear_Data.write(data_dict_end)