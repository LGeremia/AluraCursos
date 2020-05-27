from datetime import datetime, timedelta

class Dates:
    def __init__(self):
        self._create_moment = datetime.today()
        self.formated_create_moment = format_create_moment()
        

    def create_month(self):
        year_months = [
            "Janeiro", "Fevereiro", "Março", "Abril",
            "Maio", "Junho", "Julho", "Agosto",
            "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
        create_month = self.create_moment.month
        return year_months[create_month - 1]

    def week_day(self):
        week_days = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        return week_days[self.create_moment.weekday()]

    def __str__(self):
        return "Usuário criado no dia {} de {} de {} em uma {}-feira".format(
            self.create_moment.day, self.create_month(), self.create_moment.year, self.week_day()
        )
    
    def format_create_moment(self):
        formated_create_moment = self.create_moment.strftime("%d/%m/%Y %H:%M")
        return formated_create_moment