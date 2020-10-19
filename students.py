class Student:
    """
    This is  student class.
    It helps to momitor the students we are traaining on any of our programs

    @param: name, which defaults to empty string, determines the name of the student
    @param: sex, which defaults to empty string, determines the sex of the student
    @param: age,
    @param: course_list, score contains a list of tupples containing training courses the student enrolls in
    course_list = [(), ()]
    
    """
    def __init__(self, name='', age=0, sex='', course_list=[]):
        self.name = name
        self.age = age
        self.sex = sex
        self.course_list = course_list
        
    def addCourse(self, course):
        self.course_list.append({"course":course, "score": 0})

    def updateScore(self, course, x):
        self.course_list[-1]["score"] = x


        
