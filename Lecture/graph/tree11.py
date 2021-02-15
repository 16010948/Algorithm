class Project:
    def __init__(self, name):
        self.name = name
        self.marked = False
        self.dependencies = []

    def add_dependency(self, project):
        if project not in self.dependencies:
            self.dependencies.append(project)

    def get_dependencies(self):
        return self.dependencies

    def get_name(self):
        return self.name

    def set_marked(self, marked):
        self.marked = marked

    def get_marked(self):
        return self.marked

class Project_Manager:
    def __init__(self, names, dependencies):
        self.projects = {}
        self.build_projects(names)
        self.add_dependencies(dependencies)

    def build_projects(self, names):
        for i in range(len(names)):
            self.projects[names[i]] = Project(names[i])

    def add_dependencies(self, dependencies):
        for dependency in dependencies:
            before = self.find_project(dependency[0])
            after = self.find_project(dependency[1])
            after.add_dependency(before)

    index = 0
    def build_order(self):
        self.init_making_flags()
        ordered = [0] * len(self.projects)
        self.index = 0
        for project in self.projects.values():
            self.build_order_recursive(project, ordered)
        return ordered

    def build_order_recursive(self, project, ordered):
        for p in project.get_dependencies():
            self.build_order_recursive(p, ordered)
        if project.get_marked() == False:
            project.set_marked(True)
            ordered[self.index] = project
            self.index += 1
    def init_making_flags(self):
        for project in self.projects.values():
            project.set_marked(False)

    def find_project(self, name):
        return self.projects[name]

projects = ["a", "b", "c", "d", "e", "f", "g"]
dependencies = [["f", "a"], ["f", "b"], ["f", "c"], ["b", "a"], ["c", "a"], ["a", "e"], ["b", "e"], ["d", "g"]]
pm = Project_Manager(projects, dependencies)
ps = pm.build_order()
for p in ps:
    if p != None:
        print(p.get_name(), end=" ")

