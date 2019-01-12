#incomplete
with open('license_file.txt', 'r') as input_file:
    input_data = input_file.read()

data_list = [int(s) for s in input_data.split(' ')]
data_label = [0]*len(data_list)

nodes_remaining_per_level = [[data_list[0], data_list[1]]]  # layers down, metadata that remains to be entered on that layer


position_across = 0
position_down = 0
while 0 in data_label:

    data_label[position_across] = 'N'
    if position_down > len(nodes_remaining_per_level) - 1:
        nodes_remaining_per_level.append([data_list[position_across], data_list[position_across + 1]])
    position_across += 1
    data_label[position_across] = 'M'

    if nodes_remaining_per_level[max(position_down,0)][0] == 0:
        for x in range(nodes_remaining_per_level[max(position_down, 0)][1]):
            data_label[min(position_across + x + 1, len(data_label))] = 'E'
        position_across += data_list[position_across] + 1
        position_down -= 1
    elif nodes_remaining_per_level[position_down][0] > 0:
        nodes_remaining_per_level[position_down][0] -= 1
        position_across += 1
        position_down += 1

    print(data_label[:40])
    print(position_down)

        


        





