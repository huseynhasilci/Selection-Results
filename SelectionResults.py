from Tkinter import *
from ttk import Combobox
from PIL import ImageTk,Image
import tkFileDialog
from clusters import *
# from ttk import *
class Results():
    def __init__(self,election_results = {}):           #result part
        self.election_results = election_results
        # self.blabla = GUIPart(self)
    def districts_clusters(self):
        self.lines = [line for line in self.filename2]

        district_list = []
        self.party_list = []
        party_helper = False
        count = 0
        district_name = ""
        district_value = 0
        for line in self.lines[0:]:
            count += 1
            p = line.split('\t')                #addind everything to the dictionry in district rate
            if (p[0].find("Kaynak") > -1):
                party_helper = False
                district_value = count + 1
            if (district_value == count):
                district_name = p[0].replace("\n", "")
                if district_name not in district_list:
                    district_list.append(district_name)
            if (p[0] == "Toplam"):
                party_helper = False


            if (p[0].find("Kis.") > -1):
                vote_rate_in_districts ={}
                party_helper = True
            if (party_helper == True and p[0].find("Kis.") < 0 and p[0] != "BGMSZ"):

                vote_rate_in_districts[p[0].replace("\n", "")] = p[4].replace("%", "").replace("\n", "")
                if p[0] not in self.party_list:
                    self.party_list.append(p[0].replace("\n", ""))              #addind everything to the dictionry in district rate
            if (p[0] == "Toplam"):
                self.election_results[district_name] = vote_rate_in_districts

class PoliticalParties():
    def __init__(self):
        self.blabula =  Results()
        self.election_results1 = {}
    def political_parties_clusters(self):
        for partyItem in self.blabula.party_list:
            districts_rates = {}
            for distrctItem in self.blabula.election_results.items():
                distrct_vote_rates = distrctItem[1]
                if partyItem in distrct_vote_rates.keys():                              #addind everything to the dictionry in political district rate
                    districts_rates[distrctItem[0]] = distrct_vote_rates[partyItem]
                else:
                    districts_rates[distrctItem[0]] = "0"
            self.election_results1[partyItem] = districts_rates


class DataCenter():
    def __init__(self,districts,parties):
        self. districts = districts
        self.parties = parties                      #Data center


class GUIPart(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent                #GUI part

        # self.filename2 = open(tkFileDialog.askopenfilename(initialdir="/", title="Select file",
        # self.a = Results()
        # self.a.districts_clusters()
        self.unitIU()
    def unitIU(self):
        self.var = StringVar()
        self.var.set("%0")
        first_frame = Frame(self)       # Frames for the GUI
        second_frame = Frame(self)
        third_frame = Frame(self)
        fourth_frame = Frame(third_frame)
        self.fiveth_frame = Frame(self)
        self.sixth_frame = Frame(self.fiveth_frame)
        self.seventh_frame = Frame(self)
        self.eigth_frame = Frame(self.seventh_frame)
        self.pack()
        first_frame.pack(fill = X,expand = True)
        second_frame.pack()
        third_frame.pack()
        fourth_frame.grid()
        self.fiveth_frame.pack()
        self.sixth_frame.grid(row=0,column=0)
        self.seventh_frame.pack()
        self.eigth_frame.grid(row=1,column=0)
        e_d_a_t = Label(first_frame,text = "Election Data Analysis Tool v.1.0",bg = "red",fg= "white")          #Labels buttons
        e_d_a_t.pack(side = TOP,fill = X,expand = True)
        first_button = Button(first_frame,text = "Load Election Data",height=3, width=40,command= self.load_election_data)
        first_button.pack(side = TOP)
        second_button = Button(fourth_frame,text = "Cluster Districts",height=3, width=40,command = self.cluster_districts)
        second_button.grid(row = 0, column= 0,padx= 10)
        third_button = Button(fourth_frame,text = "Cluster Political Parties",height=3, width=40,command = self.cluster_political_parties)
        third_button.grid(row =0 ,column = 1)


    def load_election_data(self):
        self.filename2 = open(tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                           filetypes=(("txt files", "*.txt"), ("all files", "*.*"))))
        self.lines = [line for line in self.filename2]
        self.election_results = {}
        self.election_results1 = {}
        district_list = []
        self.party_list = []                    #getting data from the load election button
        party_helper = False
        count = 0
        district_name = ""
        district_value = 0
        for line in self.lines[0:]:                 # addind everything to the data
            count += 1
            p = line.split('\t')
            if (p[0].find("Kaynak") > -1):
                party_helper = False
                district_value = count + 1
            if (district_value == count):
                district_name = p[0].replace("\n", "")
                if district_name not in district_list:
                    district_list.append(district_name)
            if (p[0] == "Toplam"):
                party_helper = False

            if (p[0].find("Kis.") > -1):
                vote_rate_in_districts = {}
                party_helper = True
            if (party_helper == True and p[0].find("Kis.") < 0 and p[0] != "BGMSZ"):
                vote_rate_in_districts[p[0].replace("\n", "")] = p[4].replace("%", "").replace("\n", "")
                if p[0] not in self.party_list:
                    self.party_list.append(p[0].replace("\n", ""))
            if (p[0] == "Toplam"):
                self.election_results[district_name] = vote_rate_in_districts
        for partyItem in self.party_list:
            districts_rates = {}
            for distrctItem in self.election_results.items():
                distrct_vote_rates = distrctItem[1]
                if partyItem in distrct_vote_rates.keys():
                    districts_rates[distrctItem[0]] = distrct_vote_rates[partyItem]
                else:
                    districts_rates[distrctItem[0]] = "0"
            self.election_results1[partyItem] = districts_rates

    def cluster_districts(self):
        self.canvas = Canvas(self.sixth_frame, bg='#FFFFFF', width=1100, height=300)        #adding canvas and image part
        # self.canvas.config(width=1100, height=300)
        # self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.canvas.grid(row = 0,column = 0)

        self.hbar = Scrollbar(self.sixth_frame, orient=HORIZONTAL, command=self.canvas.xview)   #adding scrollbar, canvas, label,button,combobox
        self.hbar.grid(row = 0,column = 0,sticky="nsew")
        # self.hbar.config(command=self.canvas.xview)

        self.vbar = Scrollbar(self.sixth_frame, orient=VERTICAL, command=self.canvas.yview)
        self.vbar.grid(row = 0,column = 0,sticky="nsew")
        # self.vbar.config(command=self.canvas.yview)

        self.label = Label(self.eigth_frame,text = "Districts:")
        self.label.grid(row = 0,column = 0)
        self.label_threshold = Label(self.eigth_frame,text= "Threshold:")
        self.label_threshold.grid(row = 0,column = 2)

        self.comboExample = Combobox(self.eigth_frame, state="readonly",
                                values=[
                                    "%0",
                                    "%1",
                                    "%10",
                                    "%20","%30","%40","%50"],textvariable = self.var)

        self.comboExample.grid(column=3, row=0)

        self.scrollbar1 = Scrollbar(self.eigth_frame)
        self.scrollbar1.grid(row=0, column=1, sticky="nswe")
        self.mylist = Listbox(self.eigth_frame, yscrollcommand=self.scrollbar1.set,selectmode = "multiple")
        self.mylist.grid(row=0, column=1)
        self.scrollbar1.config(command=self.mylist.yview)
        self.button = Button(self.eigth_frame,text = "Refine Analysis",width = 30,height = 3,command = self.combobox_function)
        self.button.grid(row = 0,column = 4)
        # img = ImageTk.PhotoImage(Image.open("clusters.jpg"))
        # canvas.create_image(20, 20, anchor=NW, image=img)
        # blognames, words, data = readfile(self.filename2.name)
        # clust = hcluster(data)
        # drawdendrogram(clust, blognames, jpeg="a.jpg")
        # img = ImageTk.PhotoImage(Image.open("a.jpg"))
        # self.canvas.create_image(20, 20, anchor=NW, image=img)
        for i in self.election_results.keys():
            self.mylist.insert(END, i)                  # adding districts to the list box

        line = ""
        with open("Districts.txt", "w+") as filetest:               #matrix part
            line = "Blog\t"
            for item in self.election_results1.keys():
                line = line + item
                line = line + "\t"

            line = line.strip('\t')

            filetest.writelines(line)
            filetest.writelines("\n")
            district_name = ""
            temp_dict = {}
            line = ""
            for item in self.election_results.items():
                district_name = item[0]
                line = line + district_name
                line = line + "\t"
                for itemNew in self.election_results1.keys():
                    temp_dict = item[1]
                    if(itemNew in temp_dict.keys()):
                        if(item[1][itemNew] == ""):
                            line = line + "0"
                        else:
                            line = line + item[1][itemNew]
                    else:
                        line = line + "0"

                    line = line + "\t"
                line = line.strip('\t')
                line = line + "\n"
                filetest.writelines(line)
                line = ""
        filetest.close()


        self.blognames, words, self.data = readfile("Districts.txt")            #parsing districts file and creating a new jpg file
        clust = hcluster(self.data)
        drawdendrogram(clust, self.blognames, jpeg="DistrictsRate.jpg")
        self.img = ImageTk.PhotoImage(Image.open("DistrictsRate.jpg"))
        self.canvas.create_image(0, 0, anchor=NW, image=self.img)           #and adding image


    def cluster_political_parties(self):
        self.canvas = Canvas(self.sixth_frame, bg='#FFFFFF', width=1100, height=300)
        # self.canvas.config(width=1100, height=300)
        # self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.canvas.grid(row=0, column=0)

        self.hbar = Scrollbar(self.sixth_frame, orient=HORIZONTAL, command=self.canvas.xview)
        self.hbar.grid(row=0, column=0, sticky="nsew")
        # self.hbar.config(command=self.canvas.xview)

        self.vbar = Scrollbar(self.sixth_frame, orient=VERTICAL, command=self.canvas.yview)
        self.vbar.grid(row=0, column=0, sticky="nsew")
        # self.vbar.config(command=self.canvas.yview)

        self.label = Label(self.eigth_frame, text="Districts:")
        self.label.grid(row=0, column=0)
        self.label_threshold = Label(self.eigth_frame, text="Threshold:")
        self.label_threshold.grid(row=0, column=2)

        self.comboExample = Combobox(self.eigth_frame, state="readonly",
                                     values=[
                                         "%0",
                                         "%1",
                                         "%10",
                                         "%20", "%30", "%40", "%50"])

        self.comboExample.grid(column=3, row=0)
        self.comboExample.current(1)

        self.scrollbar1 = Scrollbar(self.eigth_frame)
        self.scrollbar1.grid(row=0, column=1, sticky="nswe")
        self.mylist = Listbox(self.eigth_frame, yscrollcommand=self.scrollbar1.set,selectmode = "multiple")
        self.mylist.grid(row=0, column=1)
        self.scrollbar1.config(command=self.mylist.yview)
        self.button = Button(self.eigth_frame, text="Refine Analysis", width=30, height=3,
                             command=self.combobox_function)
        self.button.grid(row=0, column=4)
        #**********************************************
        for i in self.election_results.keys():
            self.mylist.insert(END, i)

        line = ""
        with open("Districts.txt", "w+") as filetest:           #also matrix part for parties
            line = "Blog\t"
            for item in self.election_results1.keys():
                line = line + item
                line = line + "\t"

            line = line.strip('\t')

            filetest.writelines(line)
            filetest.writelines("\n")
            district_name = ""
            temp_dict = {}
            line= ""
            for item in self.election_results.items():
                district_name = item[0]
                line = line + district_name
                line = line + "\t"
                for itemNew in self.election_results1.keys():
                    temp_dict = item[1]
                    if (itemNew in temp_dict.keys()):
                        if (item[1][itemNew] == ""):
                            line = line + "0"
                        else:
                            line = line + item[1][itemNew]
                    else:
                        line = line + "0"

                    line = line + "\t"
                line = line.strip('\t')
                line = line + "\n"
                filetest.writelines(line)
                line = ""
        filetest.close()



        blognames, words, data = readfile("PartyDistricts.txt")
        clust = hcluster(data)                                      #also creating image for parties
        drawdendrogram(clust, blognames, jpeg="DistrictsRate1.jpg")
        self.img = ImageTk.PhotoImage(Image.open("DistrictsRate1.jpg"))
        self.canvas.create_image(0, 0, anchor=NW, image=self.img)

    def combobox_function(self):
        percantege = self.var.get()                             #Refine analiysis button codes
        self.comboExample.bind("<<ComboboxSelected>>")



        # if percantege == self.data:
        #     self.label.configure(text = "You Selected" + i)
        # elif percantege == "%1":
        #     self.label.configure(text="You Selected" + i)
        # elif percantege == "%10":
        #     self.label.configure(text="You Selected" + i)
        # elif percantege == "%20":
        #     self.label.configure(text="You Selected" + i)
        # elif percantege == "%30":
        #     self.label.configure(text="You Selected" + i)
        # elif percantege == "%40":
        #     self.label.configure(text="You Selected" + i)
        # elif percantege == "%50":
        #     self.label.configure(text="You Selected" + i)










def main():
    root = Tk()
    root.title("Clustering")
    root.geometry("1300x800+10+10")
    app = GUIPart(root)

    root.mainloop()

main()










