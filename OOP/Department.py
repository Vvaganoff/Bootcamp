class Department:
    id: int
    title: str
    def __init__(self, id: int, title: str) -> None:
        self.id = id
        self.title = title
        
    def __repr__(self) ->str:
        return f'Наименование:{self.title}, идентификатор:{self.id}'