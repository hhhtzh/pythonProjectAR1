from tkinter import *
import tkinter.filedialog
from algorithm.evolutionary_computing.symbolic_regression.initial import GraphAutoInitial, GpInitial, BgGraphInitial, \
    OperonTreeInitial
from data.data import Data
import tkinter.messagebox


class Window:
    def __init__(self):
        self.csy_file = None
        self.str_ft = None
        self.dt = None

    def myx(self):
        self.x_name = self.str_ft[self.var1]
        s = "您选了" + self.x_name + "作为输入x"
        self.x = self.dt.get_col(self.x_name)
        self.lb2.config(text=s)

    def xz(self):
        filename = tkinter.filedialog.askopenfilename()
        if filename != '':
            self.lb.config(text='您选择的文件是' + filename)
            self.dt = Data(filename)
            self.csy_file=filename

        else:
            self.lb.config(text='您没有选择任何文件')



    def graph_teat(self):
        a = self.inp1.get()
        b = self.inp2.get()
        c = self.inp3.get()
        d = self.inp4.get()
        e = GraphAutoInitial(int(b), int(c), int(d), str(a))
        e.init()

    def bg_graph(self):
        x = self.dt.get_x(int(self.inpu3.get()))
        y = self.dt.get_y(int(self.inpu4.get()))
        p_traindata = float(self.inp14.get())
        population_size = int(self.inp15.get())
        p_mutation = 0.4
        stopping_criteria = float(self.inp17.get())
        generation = int(self.inp18.get())
        p_subtreemutation = float(self.inp19.get())
        p_hoistmutation = float(self.inp20.get())
        p_pointmutation = float(self.inp22.get())
        parisimony = 0.01
        rand = int(self.inp21.get())
        bginit = BgGraphInitial(x=x, y=y, train_p=p_traindata,
                                population_size=population_size,
                                mutation_probability=p_mutation,
                                stopping_criteria=stopping_criteria,
                                generations=generation, p_subtree_mutation=p_subtreemutation,
                                p_hoist_mutation=p_hoistmutation, p_point_mutation=p_pointmutation,
                                parsimony_coefficient=parisimony, random_seed=rand)
        bginit.do()

    def gp_tree(self):

        x = self.dt.get_x(int(self.inpu11.get()))
        y = self.dt.get_y(int(self.inpu12.get()))
        p_traindata = float(self.inp1.get())
        population_size = int(self.inp2.get())
        p_mutation = float(self.inp5.get())
        stopping_criteria = float(self.inp13.get())
        generation = int(self.inp4.get())
        p_subtreemutation = float(self.inp5.get())
        p_hoistmutation = float(self.inp6.get())
        p_pointmutation = float(self.inp8.get())
        parisimony = float(self.inp9.get())
        rand = int(self.inp7.get())
        gpinit = GpInitial(x=x, y=y, train_p=p_traindata,
                           population_size=population_size,
                           mutation_probability=p_mutation,
                           stopping_criteria=stopping_criteria,
                           generations=generation, p_subtree_mutation=p_subtreemutation,
                           p_hoist_mutation=p_hoistmutation, p_point_mutation=p_pointmutation,
                           parsimony_coefficient=parisimony, random_seed=rand)
        gpinit.do()

    def op_tree(self):
        csv_file=self.csy_file
        minL=int(self.inpu411.get())
        maxL=int(self.inpu412.get())
        population_size=int(self.inp42.get())
        p_traindata=float(self.inp41.get())
        p_mutation = float(self.inp43.get())
        stopping_criteria = float(self.inp413.get())
        generation = int(self.inp44.get())
        p_crossover = float(self.inp45.get())
        maxD = int(self.inp46.get())
        threads = int(self.inp48.get())
        limit = int(self.inp49.get())
        rand = int(self.inp47.get())
        evaluator_budget=int(self.inp410.get())
        opinit=OperonTreeInitial(csv_filename=csv_file, minL=minL, maxL=maxL, maxD=maxD,
                                  population_size=population_size, train_p=p_traindata,
                                  mutation_probability=p_mutation,
                                  crossover_probability=p_crossover,
                                  generations=generation, time_limit=limit,
                                  random_seed=rand, error_tolerance=stopping_criteria, threads=threads,evaluator_budget=evaluator_budget)
        opinit.do()



    def newwind4(self):
        self.winNew4 = Toplevel(self.root)
        self.winNew4.geometry('720x720')
        self.winNew4.title('operon树编码符号回归')
        self.lb = Label(self.winNew4, text='选择作为数据来源的csv文件(文件的最后一列将作为y)')
        self.lb.place(relx=0)
        btn1 = Button(self.winNew4, text='选择csv文件', command=self.xz)
        btn1.place(relx=0.8, rely=0)
        self.lb410 = Label(self.winNew4, text='请输入树的最小宽度')
        self.lb410.place(relx=0, rely=0.05)
        self.inpu411 = Entry(self.winNew4)
        self.inpu411.place(relx=0.3, rely=0.05)
        self.lb412 = Label(self.winNew4, text='请选择树的最大宽度')
        self.lb412.place(relx=0.5, rely=0.05)
        self.inpu412 = Entry(self.winNew4)
        self.inpu412.place(relx=0.7, rely=0.05)
        lb1 = Label(self.winNew4, text='请输入数据中作为训练数据的比例(0到1之间，剩下用作测试数据)')
        lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
        self.inp41 = Entry(self.winNew4)
        self.inp41.place(relx=0.76, rely=0.12, relwidth=0.1, relheight=0.05)
        lb2 = Label(self.winNew4, text='请输入种群的大小')
        lb2.place(relx=0.1, rely=0.18, relwidth=0.8, relheight=0.1)
        self.inp42 = Entry(self.winNew4)
        self.inp42.place(relx=0.76, rely=0.2, relwidth=0.1, relheight=0.05)
        lb3 = Label(self.winNew4, text='请输入突变发生的概率(0到1之间)')
        lb3.place(relx=0.1, rely=0.26, relwidth=0.8, relheight=0.1)
        self.inp43 = Entry(self.winNew4)
        self.inp43.place(relx=0.76, rely=0.28, relwidth=0.1, relheight=0.05)
        lb3 = Label(self.winNew4, text='请输入迭代终止的标准 (0到1之间)')
        lb3.place(relx=0.1, rely=0.34, relwidth=0.8, relheight=0.1)
        self.inp413 = Entry(self.winNew4)
        self.inp413.place(relx=0.76, rely=0.36, relwidth=0.1, relheight=0.05)
        lb4 = Label(self.winNew4, text='请输入最大迭代次数')
        lb4.place(relx=0.1, rely=0.42, relwidth=0.8, relheight=0.1)
        self.inp44 = Entry(self.winNew4)
        self.inp44.place(relx=0.76, rely=0.44, relwidth=0.1, relheight=0.05)
        lb5 = Label(self.winNew4, text='请输入发生子树交叉的概率(0到1之间)')
        lb5.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.1)
        self.inp45 = Entry(self.winNew4)
        self.inp45.place(relx=0.76, rely=0.52, relwidth=0.1, relheight=0.05)
        lb6 = Label(self.winNew4, text='请输入树的最大深度')
        lb6.place(relx=0.1, rely=0.58, relwidth=0.8, relheight=0.1)
        self.inp46 = Entry(self.winNew4)
        self.inp46.place(relx=0.76, rely=0.6, relwidth=0.1, relheight=0.05)
        lb7 = Label(self.winNew4, text='请输入随机种子')
        lb7.place(relx=0.3, rely=0.66, relwidth=0.5, relheight=0.1)
        self.inp47 = Entry(self.winNew4)
        self.inp47.place(relx=0.76, rely=0.68, relwidth=0.1, relheight=0.05)
        lb8 = Label(self.winNew4, text='请输入运行线程的数量')
        lb8.place(relx=0.1, rely=0.74, relwidth=0.8, relheight=0.1)
        self.inp48 = Entry(self.winNew4)
        self.inp48.place(relx=0.76, rely=0.76, relwidth=0.1, relheight=0.05)
        lb9 = Label(self.winNew4, text='请输入最大运行时间')
        lb9.place(relx=0.1, rely=0.82, relwidth=0.8, relheight=0.1)
        self.inp49 = Entry(self.winNew4)
        self.inp49.place(relx=0.76, rely=0.84, relwidth=0.1, relheight=0.05)
        lb10 = Label(self.winNew4, text='请输入评估预算')
        lb10.place(relx=0.1, rely=0.9, relwidth=0.65, relheight=0.1)
        self.inp410 = Entry(self.winNew4)
        self.inp410.place(relx=0.76, rely=0.92, relwidth=0.1, relheight=0.05)
        btn2 = Button(self.winNew4, text='operon树编码回归', command=self.op_tree)
        btn2.place(relx=0, rely=0.8, relwidth=0.3, relheight=0.05)
        btn3 = Button(self.winNew4, text='关闭', command=self.winNew4.destroy)
        btn3.place(relx=0, rely=0.9, relwidth=0.3, relheight=0.05)

    def newwind2(self):
        self.winNew2 = Toplevel(self.root)
        self.winNew2.geometry('720x720')
        self.winNew2.title('gp树编码符号回归')
        self.lb = Label(self.winNew2, text='选择作为数据来源的csv文件')
        self.lb.place(relx=0)
        btn1 = Button(self.winNew2, text='选择csv文件', command=self.xz)
        btn1.place(relx=0.8, rely=0)
        self.lb1 = Label(self.winNew2, text='选择作为x的列')
        self.lb1.place(relx=0, rely=0.05)
        self.inpu11 = Entry(self.winNew2)
        self.inpu11.place(relx=0.3, rely=0.05)
        self.lb12 = Label(self.winNew2, text='选择作为y的列')
        self.lb12.place(relx=0.5, rely=0.05)
        self.inpu12 = Entry(self.winNew2)
        self.inpu12.place(relx=0.7, rely=0.05)
        lb1 = Label(self.winNew2, text='请输入数据中作为训练数据的比例(0到1之间，剩下用作测试数据)')
        lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
        self.inp1 = Entry(self.winNew2)
        self.inp1.place(relx=0.76, rely=0.12, relwidth=0.1, relheight=0.05)
        lb2 = Label(self.winNew2, text='请输入种群的大小')
        lb2.place(relx=0.1, rely=0.18, relwidth=0.8, relheight=0.1)
        self.inp2 = Entry(self.winNew2)
        self.inp2.place(relx=0.76, rely=0.2, relwidth=0.1, relheight=0.05)
        lb3 = Label(self.winNew2, text='请输入突变发生的概率(0到1之间)')
        lb3.place(relx=0.1, rely=0.26, relwidth=0.8, relheight=0.1)
        self.inp3 = Entry(self.winNew2)
        self.inp3.place(relx=0.76, rely=0.28, relwidth=0.1, relheight=0.05)
        lb3 = Label(self.winNew2, text='请输入迭代终止的标准 (0到1之间)')
        lb3.place(relx=0.1, rely=0.34, relwidth=0.8, relheight=0.1)
        self.inp13 = Entry(self.winNew2)
        self.inp13.place(relx=0.76, rely=0.36, relwidth=0.1, relheight=0.05)
        lb4 = Label(self.winNew2, text='请输入最大迭代次数')
        lb4.place(relx=0.1, rely=0.42, relwidth=0.8, relheight=0.1)
        self.inp4 = Entry(self.winNew2)
        self.inp4.place(relx=0.76, rely=0.44, relwidth=0.1, relheight=0.05)
        lb5 = Label(self.winNew2, text='请输入发生子树变异的概率(0到1之间)')
        lb5.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.1)
        self.inp5 = Entry(self.winNew2)
        self.inp5.place(relx=0.76, rely=0.52, relwidth=0.1, relheight=0.05)
        lb6 = Label(self.winNew2, text='请输入发生提升变异的概率(0到1之间)')
        lb6.place(relx=0.1, rely=0.58, relwidth=0.8, relheight=0.1)
        self.inp6 = Entry(self.winNew2)
        self.inp6.place(relx=0.76, rely=0.6, relwidth=0.1, relheight=0.05)
        lb7 = Label(self.winNew2, text='请输入随机种子')
        lb7.place(relx=0.3, rely=0.66, relwidth=0.5, relheight=0.1)
        self.inp7 = Entry(self.winNew2)
        self.inp7.place(relx=0.76, rely=0.68, relwidth=0.1, relheight=0.05)
        lb8 = Label(self.winNew2, text='请输入发生点变异的概率(0到1之间)')
        lb8.place(relx=0.1, rely=0.74, relwidth=0.8, relheight=0.1)
        self.inp8 = Entry(self.winNew2)
        self.inp8.place(relx=0.76, rely=0.76, relwidth=0.1, relheight=0.05)
        lb9 = Label(self.winNew2, text='请输入节俭系数')
        lb9.place(relx=0.1, rely=0.82, relwidth=0.8, relheight=0.1)
        self.inp9 = Entry(self.winNew2)
        self.inp9.place(relx=0.76, rely=0.84, relwidth=0.1, relheight=0.05)
        lb10 = Label(self.winNew2, text='请输入随机种子')
        lb10.place(relx=0.1, rely=0.9, relwidth=0.65, relheight=0.1)
        self.inp10 = Entry(self.winNew2)
        self.inp10.place(relx=0.76, rely=0.92, relwidth=0.1, relheight=0.05)
        btn2 = Button(self.winNew2, text='gp树编码回归', command=self.gp_tree)
        btn2.place(relx=0, rely=0.8, relwidth=0.3, relheight=0.05)
        btn3 = Button(self.winNew2, text='关闭', command=self.winNew2.destroy)
        btn3.place(relx=0, rely=0.9, relwidth=0.3, relheight=0.05)

    def newwind3(self):
        self.winNew3 = Toplevel(self.root)
        self.winNew3.geometry('720x720')
        self.winNew3.title('bingo图编码符号回归')
        self.lb = Label(self.winNew3, text='选择作为数据来源的csv文件')
        self.lb.place(relx=0)
        btn2 = Button(self.winNew3, text='选择csv文件', command=self.xz)
        btn2.place(relx=0.8, rely=0)
        self.lb4 = Label(self.winNew3, text='选择作为x的列')
        self.lb4.place(relx=0, rely=0.05)
        self.inpu3 = Entry(self.winNew3)
        self.inpu3.place(relx=0.3, rely=0.05)
        self.lb5 = Label(self.winNew3, text='选择作为y的列')
        self.lb5.place(relx=0.5, rely=0.05)
        self.inpu4 = Entry(self.winNew3)
        self.inpu4.place(relx=0.7, rely=0.05)
        lb1 = Label(self.winNew3, text='请输入数据中作为训练数据的比例(0到1之间，剩下用作测试数据)')
        lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
        self.inp14 = Entry(self.winNew3)
        self.inp14.place(relx=0.76, rely=0.12, relwidth=0.1, relheight=0.05)
        lb2 = Label(self.winNew3, text='请输入种群的大小')
        lb2.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.1)
        self.inp15 = Entry(self.winNew3)
        self.inp15.place(relx=0.76, rely=0.22, relwidth=0.1, relheight=0.05)
        lb3 = Label(self.winNew3, text='请输入突变发生的概率(0到1之间)')
        lb3.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.1)
        self.inp16 = Entry(self.winNew3)
        self.inp16.place(relx=0.76, rely=0.32, relwidth=0.1, relheight=0.05)
        lb3 = Label(self.winNew3, text='请输入迭代终止的标准 (0到1之间)')
        lb3.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.1)
        self.inp17 = Entry(self.winNew3)
        self.inp17.place(relx=0.76, rely=0.32, relwidth=0.1, relheight=0.05)
        lb4 = Label(self.winNew3, text='请输入最大迭代次数')
        lb4.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.1)
        self.inp18 = Entry(self.winNew3)
        self.inp18.place(relx=0.76, rely=0.42, relwidth=0.1, relheight=0.05)
        lb5 = Label(self.winNew3, text='请输入发生子树变异的概率(0到1之间)')
        lb5.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.1)
        self.inp19 = Entry(self.winNew3)
        self.inp19.place(relx=0.76, rely=0.52, relwidth=0.1, relheight=0.05)
        lb6 = Label(self.winNew3, text='请输入发生提升变异的概率(0到1之间)')
        lb6.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.1)
        self.inp20 = Entry(self.winNew3)
        self.inp20.place(relx=0.76, rely=0.62, relwidth=0.1, relheight=0.05)
        lb7 = Label(self.winNew3, text='请输入随机种子')
        lb7.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.1)
        self.inp21 = Entry(self.winNew3)
        self.inp21.place(relx=0.76, rely=0.72, relwidth=0.1, relheight=0.05)
        lb8 = Label(self.winNew3, text='请输入发生点变异的概率(0到1之间)')
        lb8.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.1)
        self.inp22 = Entry(self.winNew3)
        self.inp22.place(relx=0.76, rely=0.82, relwidth=0.1, relheight=0.05)
        lb9 = Label(self.winNew3, text='请输入节俭系数')
        lb9.place(relx=0.1, rely=0.9, relwidth=0.8, relheight=0.1)
        self.inp23 = Entry(self.winNew3)
        self.inp23.place(relx=0.76, rely=0.92, relwidth=0.1, relheight=0.05)
        lb10 = Label(self.winNew3, text='请输入随机种子')
        lb10.place(relx=0.1, rely=1, relwidth=0.8, relheight=0.1)
        self.inp24 = Entry(self.winNew3)
        self.inp24.place(relx=0.76, rely=1.02, relwidth=0.1, relheight=0.05)
        btn2 = Button(self.winNew3, text='bingo图编码回归', command=self.bg_graph)
        btn2.place(relx=0, rely=0.8, relwidth=0.3, relheight=0.05)
        btn3 = Button(self.winNew3, text='关闭', command=self.winNew3.destroy)
        btn3.place(relx=0, rely=0.9, relwidth=0.3, relheight=0.05)

    def newwind1(self):
        winNew1 = Toplevel(self.root)
        winNew1.geometry('720x720')
        winNew1.title('给出函数生成数据-bingo图编码')
        lb1 = Label(winNew1, text='输入一个方程通过符号回归得到它(x使用{x}替代)')
        lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
        self.inp1 = Entry(winNew1)
        self.inp1.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.05)
        lb2 = Label(winNew1, text='请输入左区间，右区间和取点的个数')
        lb2.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.1)
        self.inp2 = Entry(winNew1)
        self.inp2.place(relx=0.1, rely=0.4, relwidth=0.1, relheight=0.05)
        self.inp3 = Entry(winNew1)
        self.inp3.place(relx=0.3, rely=0.4, relwidth=0.1, relheight=0.05)
        self.inp4 = Entry(winNew1)
        self.inp4.place(relx=0.5, rely=0.4, relwidth=0.1, relheight=0.05)

        btn1 = Button(winNew1, text='bingo图编码回归', command=self.graph_teat)
        btn1.place(relx=0.1, rely=0.9, relwidth=0.3, relheight=0.05)
        btn2 = Button(winNew1, text='关闭', command=winNew1.destroy)
        btn2.place(relx=0.4, rely=0.9, relwidth=0.3, relheight=0.05)

    def init(self):
        self.root = Tk()
        self.root.geometry('720x720')
        self.root.title('符号回归')
        mainmenu = Menu(self.root)
        menuAuto = Menu(mainmenu)
        mainmenu.add_cascade(label='给出函数生成数据', menu=menuAuto)
        menuAuto.add_command(label='bingo图编码', command=self.newwind1)
        menuAuto.add_separator()
        menuAuto.add_command(label='退出', command=self.root.destroy)
        menuCsv = Menu(mainmenu)
        mainmenu.add_cascade(label='使用csv文件符号回归', menu=menuCsv)
        menuCsv.add_command(label='bingo图编码回归', command=self.newwind3)
        menuCsv.add_command(label='gp树编码回归', command=self.newwind2)
        menuCsv.add_command(label='operon树编码回归',command=self.newwind4)
        menuCsv.add_separator()
        menuCsv.add_command(label='退出', command=self.root.destroy)
        self.root.config(menu=mainmenu)

        self.root.mainloop()