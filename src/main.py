from src.class_api import FromHHru
from src.methods import ListVacancies
from src.sorting import sorting


def interface():
    """Функция для взаимодействия с пользователем"""

    user_vacancy = input('Введите вакансию для поиска на сайте hh.ru: \n')
    hh = FromHHru()
    vacancies = hh.get_vacancies(user_vacancy)

    fv = ListVacancies()
    fv.save_vacancies(vacancies)

    name_vac = input('Введите название вакансии: \n')
    fv.add_vacancy(name_vac)

    name_criterion = input('Введите критерий для отбора вакансий: \n')
    fv.get_data(name_criterion)

    n = input('Введите количество вакансий для просмотра: \n')
    sorting(int(n))

    name_exit = input('Завершим и очистим файл вакансий да/нет : \n')
    if name_exit == 'да':
        fv.delete_vacancy()
    else:
        interface()


interface()
