class Worker:
    id: int
    dep_id: int
    age: int
    full_name: str
    salary: int
    def __init__(self, id: int, full_name: str, age: int,  salary: int, dep_id: int) -> None:
        self.id = id
        self.dep_id = dep_id
        self.age = age
        self.full_name = full_name
        self.salary = salary
        
    def __repr__(self) ->str:
        return f'id: {self.id}, Full name: {self.full_name}, salary: {self.salary}, age: {self.age} dep id: {self.dep_id}'