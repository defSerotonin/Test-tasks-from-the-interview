class SortMyList:
    def __init__(self, mylist):
        self.sorted_list = mylist

    def convert_value_list(self):
        temporary_lists_append = []
        for i in range(0, len(self.sorted_list)):
            first_position_value = self.sorted_list[i]
            first_position_value = first_position_value[0].split()
            temporary_lists_append.append(first_position_value)
        return temporary_lists_append
        
    def sort_values(self):
        temporary_list_append = self.convert_value_list()
        for i in range(len(temporary_list_append)-1):
            for j in range(len(temporary_list_append)-1-i):
                if temporary_list_append[j][0] > temporary_list_append[j+1][0]:
                    temporary_list_append[j][0], temporary_list_append[j + 1][0] = temporary_list_append[j+1][0], temporary_list_append[j][0]
        return temporary_list_append

    def compare_lists(self):
        temporary_lists_append = self.sort_values()
        list_sorted = []
        for i in range(0, len(temporary_lists_append)-1, 2):
            if int(temporary_lists_append[i][0]) > int(temporary_lists_append[i+1][0]):
                list_sorted.append(temporary_lists_append[i][1])
            elif int(temporary_lists_append[i][0]) == int(temporary_lists_append[i+1][0]):
                if int(temporary_lists_append[i][2]) > int(temporary_lists_append[i+1][2]):
                    list_sorted.append(temporary_lists_append[i][1])
                else:
                    list_sorted.append(temporary_lists_append[i + 1][1])
            else:
                list_sorted.append(temporary_lists_append[i+1][1])
        return list_sorted


# Тестирование:
entered_list = [['141413 anyInfoAboutValue.z1 11131'], ['1414487692 anyInfoAboutValue.z0 1031'],
                ['1411234 anyInfoAboutValue.z3 1831'], ['1418944 anyInfoAboutValue.z4 1531'],
                ['1414453 anyInfoAboutValue.z1 1231'], ['412838281 anyInfoAboutValue.z11 1241532']]
entered_list2 = [['14141 anyInfoAboutValue.z1 11131'], ['14142 anyInfoAboutValue.z0 1031'],
                 ['14141 anyInfoAboutValue.z3 1831'], ['14141 anyInfoAboutValue.x0 1531'],
                 ['14143 anyInfoAboutValue.z1 1231'], ['412838281 anyInfoAboutValue.z9 1241532']]
sl = SortMyList(entered_list)
print(sl.compare_lists())
