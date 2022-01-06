
"""
basic info. about process
waiting: 대기
cooking: 그릴에서 패티 굽기

"""

process = {'waiting':0,'cooking':105,'cleaning':30,'uncooked':30, 'cooked':30}
typeofmodule = ('Grill','Manipulator')
stateofmoudle = {'Grill':('waiting','cooking','cleaning'),'Manipulator':('waiting','cleaning','uncooked','cooked')}
Nstepofmodule = {'Grill': len(stateofmoudle['Grill']), 'Manipulator': len(stateofmoudle['Manipulator'])}
# Class for machine

class module:

    
    def __init__(self,moduletype,name) -> None:
        self.name = name
        self.moduletype = moduletype
        self.step = 0
        self.state = stateofmoudle[self.moduletype][0]
        self.Nofstep = Nstepofmodule[self.moduletype]

    def changestate(self) -> None:
        self.step = self.step + 1
        tempnumber = self.step%self.Nofstep
        self.state = stateofmoudle[self.moduletype][tempnumber]
        


    

    



class order:

    def __init__(self,Nubmeroforder,ordertime) -> None:
        self.Numberoforder =Nubmeroforder
        self.ordertime = ordertime
        self.state = 'wait'



