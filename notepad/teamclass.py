from teammember import memberList

class TeamMember:
    id = 0
    name = ""
    age = 0
    gender = ""
    major = ""

    def __init__(self, id, name, age, gender, major):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.major = major

    def __str__(self):
        print(self.id,self.name)

idx = 1

memList = []
for idx in range(len(memberList)):
    memList.append(TeamMember(
        idx,
        memberList[idx]["name"],
        memberList[idx]["age"],
        memberList[idx]["gender"],
        memberList[idx]["major"]
        )
    )

for i in range(len(memList)):
    print(memList[i].__str__())




