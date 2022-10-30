class PlainTextDatabase:
    def __init__(self, database_path):
        # The Class has to be assigned with the path of the CSV File
        self.database_path = database_path

    def dataread(self):
        # Reading the Data of the CSSV file in following Format
        # Stat1;Stat2;Stat3 ... can be expended
        with open(f'{self.database_path}','r') as pt_database:
            index = 0
            for row in pt_database:
                line = pt_database.readlines()
                for stats in line:
                    line_stat = line[index].strip()
                    pt_data = line_stat.split(';')
                    stat1 = pt_data[0]
                    stat2 = pt_data[1]
                    stat3 = pt_data[2]
                    yield stat1, stat2, stat3
                    # Extract the data with a for loop
                    index += 1
                    
    def dataedit(self, stat_number, data_replace, pt_stat):
        # data_replace = 0-2 for number;name;status
        # pt_stat = new state for data_replace
        # stat_number = Number of the User wich needs to be edited
        with open(f'{self.database_path}', 'r') as pt_database:
            index = 0
            for row in pt_database:
                add_line = pt_database.readlines()
                for stats in add_line:
                    line_stat = add_line[index].strip()
                    pt_data = line_stat.split(';')
                    index += 1
                    if pt_data[0] == stat_number:
                    # Searching for the Number to edit 
                        replaceable_stat = pt_data[data_replace]
                        pt_data_file = ";".join([stats for stats in pt_data]).replace(replaceable_stat, pt_stat)
        with open(f'{self.database_path}', 'a+') as file_replace:
            file_replace.write(pt_data_file + '\n')     

    def datadelete(self,advanced_stat):
        # advanced_stat = full lien of number;name;status
        with open(f'{self.database_path}', 'r') as user_del:
            del_lines = user_del.readlines()

            with open(f'{self.pt_path}', 'w') as file_del:
                for del_line in del_lines:
                
                    if del_line.find(advanced_stat):
                        file_del.write(del_line)

    def dataadd(self, stat_num,stat_name):
        # stat_num = Number of the User
        # stat_name = name of the User
        # The User is always open with the off stat
        with open(f'{self.database_path}', 'a+') as user_add:
            user_add.write(f'{stat_num};{stat_name}:off')

    def databackup(self):
        pass


    