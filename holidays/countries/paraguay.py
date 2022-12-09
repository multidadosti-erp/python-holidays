#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import easter
from dateutil.relativedelta import MO
from dateutil.relativedelta import relativedelta as rd

from holidays.constants import JAN, MAR, MAY, JUN, AUG, SEP, DEC, WED
from holidays.holiday_base import HolidayBase


class Paraguay(HolidayBase):
    """
    https://www.ghp.com.py/news/feriados-nacionales-del-ano-2019-en-paraguay
    https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_feriados_en_Paraguay
    http://www.calendarioparaguay.com/
    """

    country = "PY"

    def _populate(self, year):
        super()._populate(year)

        # New Year's Day
        if not self.observed and self._is_weekend(year, JAN, 1):
            pass
        else:
            self[date(year, JAN, 1)] = "Año Nuevo [New Year's Day]"

        # Patriots day
        name = "Día de los Héroes de la Patria [Patriots Day]"

        if not self.observed and self._is_weekend(year, MAR, 1):
            pass
        elif date(year, MAR, 1).weekday() >= WED:
            self[date(year, MAR, 1) + rd(weekday=MO(+1))] = name
        else:
            self[date(year, MAR, 1)] = name

        # Holy Week
        name_thu = "Semana Santa (Jueves Santo) [Holy day (Holy Thursday)]"
        name_fri = "Semana Santa (Viernes Santo) [Holy day (Holy Friday)]"
        name_easter = "Día de Pascuas [Easter Day]"
        easter_date = easter(year)
        self[easter_date + rd(days=-3)] = name_thu
        self[easter_date + rd(days=-2)] = name_fri

        if not self.observed and self._is_weekend(easter_date):
            pass
        else:
            self[easter_date] = name_easter

        # Labor Day
        name = "Día de los Trabajadores [Labour Day]"
        if not self.observed and self._is_weekend(year, MAY, 1):
            pass
        else:
            self[date(year, MAY, 1)] = name

        # Independence Day
        name = "Día de la Independencia Nacional [Independence Day]"
        if not self.observed and self._is_weekend(year, MAY, 15):
            pass
        else:
            self[date(year, MAY, 15)] = name

        # Peace in Chaco Day.
        name = "Día de la Paz del Chaco [Peace in Chaco Day]"
        if not self.observed and self._is_weekend(year, JUN, 12):
            pass
        elif date(year, JUN, 12).weekday() >= WED:
            self[date(year, JUN, 12) + rd(weekday=MO(+1))] = name
        else:
            self[date(year, JUN, 12)] = name

        # Asuncion Fundation's Day
        name = "Día de la Fundación de Asunción [Asuncion Fundation's Day]"
        if not self.observed and self._is_weekend(year, AUG, 15):
            pass
        else:
            self[date(year, AUG, 15)] = name

        # Boqueron's Battle
        name = "Batalla de Boquerón [Boqueron's Battle]"
        if not self.observed and self._is_weekend(year, SEP, 29):
            pass
        else:
            self[date(year, SEP, 29)] = name

        # Caacupe Virgin Day
        name = "Día de la Virgen de Caacupé [Caacupe Virgin Day]"
        if not self.observed and self._is_weekend(year, DEC, 8):
            pass
        else:
            self[date(year, DEC, 8)] = name

        # Christmas
        self[date(year, DEC, 25)] = "Navidad [Christmas]"


class PY(Paraguay):
    pass


class PRY(Paraguay):
    pass
