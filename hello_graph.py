import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import csv
import os
import shutil
import os.path

def do_graph(file_name):
    print("here")
    with open(file_name) as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        all_time_dict  = {'food':0, 'clothes':0, 'transportation':0, 'phone':0, 'fun':0, 'sport':0, 'gifts':0, 'rent':0,
        'utilities':0, 'travel':0, 'personalcare':0, 'health':0, 'housing':0, 'supplies':0, 'education':0, 'other':0}
        if read_csv != None:
            for row in read_csv:
                to_add = row[2].split()
                more_add = to_add[0].split('-')
                row[2] = more_add[0]
                row.append(more_add[1])
                row.append(more_add[2])
                all_time_dict[row[0]] = all_time_dict[row[0]] + int(float(row[1]))
            frac1 = []
            labels1 = []
            for key in all_time_dict:
                labels1.append(key)
                frac1.append(all_time_dict[key])


            def make_autopct(values):
                def my_autopct(pct):
                    return ' '
                return my_autopct
            explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
            the_grid = GridSpec(1, 1)
            plt.subplot(the_grid[0, 0], aspect = 1)
            patches, texts, autotexts = plt.pie(frac1, explode=explode,
                                                labels=labels1, autopct=make_autopct(frac1),
                                                shadow = True, labeldistance = 1.15 )


            #зберігаю файл в static

            #delete a file final_stat from MyMoney
            checking = os.path.isfile("statis.png")
            if checking == True:
                os.remove("statis.png")
            ##############
            anither_path = os.getcwd() + '\static' + "\statis.png"

            if os.path.isfile(anither_path) == True:
                os.remove(anither_path)

            plt.savefig("statis.png")
            dir_path = os.path.abspath("statis.png")
            destination = os.getcwd() + '\static'
            shutil.move(dir_path,destination)
            print("Done")

