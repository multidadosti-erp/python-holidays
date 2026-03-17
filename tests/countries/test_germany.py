#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see CONTRIBUTORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/holidays
#  License: MIT (see LICENSE file)

import warnings
from unittest import TestCase

from holidays.constants import CATHOLIC
<<<<<<< HEAD
from holidays.countries.germany import Germany
=======
from holidays.countries.germany import Germany, DE, DEU
>>>>>>> develop
from tests.common import CommonCountryTests


class TestGermany(CommonCountryTests, TestCase):
    @classmethod
    def setUpClass(cls):
<<<<<<< HEAD
        super().setUpClass(Germany, with_subdiv_categories=True)
=======
        years = range(1991, 2050)
        super().setUpClass(DE, years=years)
        cls.subdiv_holidays = {
            subdiv: DE(subdiv=subdiv, years=years) for subdiv in DE.subdivisions
        }

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore", category=DeprecationWarning)
>>>>>>> develop

    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_subdiv_deprecation(self):
        self.assertDeprecatedSubdivisions("This subdivision is deprecated and will be removed")
<<<<<<< HEAD
=======

    def test_deprecated(self):
        self.assertEqual(
            sorted(Germany(subdiv="BYP", years=2023).keys()),
            sorted(Germany(subdiv="BY", years=2023).keys()),
        )

    def test_no_public_holidays_before_1990(self):
        self.assertNoHolidays(DE(years=1989))
        for p in DE.subdivisions:
            self.assertNoHolidays(DE(years=1989, subdiv=p))

    def test_no_by_catholic_holidays_before_1991(self):
        self.assertNoHolidays(DE(subdiv="BY", years=1990, categories=(CATHOLIC)))

    def test_1990_present(self):
        y_1990 = set()
        for p in DE.subdivisions:
            y_1990.update(DE(years=1990, subdiv=p).values())
        all_h = {  # Holidays names in their chronological order.
            "Tag der Deutschen Einheit",
            "Reformationstag",
            "Allerheiligen",
            "Buß- und Bettag",
            "Erster Weihnachtstag",
            "Zweiter Weihnachtstag",
        }
>>>>>>> develop

    def test_deprecated(self):
        self.assertEqual(
<<<<<<< HEAD
            sorted(Germany(subdiv="BYP", years=2023).keys()),
            sorted(Germany(subdiv="BY", years=2023).keys()),
=======
            all_h,
            y_1990,
            f"missing: {all_h - y_1990 or 'no'}, extra: {y_1990 - all_h or 'no'}",
>>>>>>> develop
        )

    def test_no_holidays(self):
        super().test_no_holidays()

<<<<<<< HEAD
        for subdiv in Germany.subdivisions:
            self.assertNoHolidays(Germany(years=self.start_year - 1, subdiv=subdiv))
        for subdiv in ("BY", "SN", "TH"):
            self.assertNoHolidays(
                Germany(subdiv=subdiv, years=self.start_year - 1, categories=CATHOLIC)
            )

    def test_special_holidays(self):
        # 2017's Reformation Day is tested in test_reformation_day.
        be_dts = (
            "2020-05-08",
            "2025-05-08",
            "2028-06-17",
=======
        self.assertEqual(
            all_h,
            y_2015,
            f"missing: {all_h - y_2015 or 'no'}," f" extra: {y_2015 - all_h or 'no'}",
>>>>>>> develop
        )
        for subdiv, holidays in self.subdiv_holidays.items():
            # Berlin.
            if subdiv == "BE":
                self.assertHoliday(holidays, be_dts)
            else:
                self.assertNoHoliday(holidays, be_dts)

    def test_new_years_day(self):
        self.assertHolidayName("Neujahr", (f"{year}-01-01" for year in self.full_range))

    def test_epiphany(self):
        name = "Heilige Drei Könige"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Bayern, Sachsen, Thüringen, Augsburg.
            if subdiv in {"BW", "BY", "ST", "Augsburg"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-01-06" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

<<<<<<< HEAD
    def test_womens_day(self):
        name = "Frauentag"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Berlin - 2019.
            if subdiv == "BE":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-08" for year in range(2019, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2019))
            # Mecklenburg-Vorpommern - 2023.
            elif subdiv == "MV":
                self.assertHolidayName(
                    name, holidays, (f"{year}-03-08" for year in range(2023, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2023))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_good_friday(self):
        name = "Karfreitag"
        self.assertHolidayName(
            name,
=======
    def test_heilige_drei_koenige(self):
        subdivs_that_have = {"BW", "BY", "ST"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-01-06" for year in range(1991, 2050))
            )
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-01-06" for year in range(1991, 2050))
            )

    def test_karfreitag(self):
        known_good = (
            "2014-04-18",
            "2015-04-03",
            "2016-03-25",
            "2017-04-14",
            "2018-03-30",
            "2019-04-19",
>>>>>>> develop
            "2020-04-10",
            "2021-04-02",
            "2022-04-15",
            "2023-04-07",
            "2024-03-29",
            "2025-04-18",
        )
        self.assertHolidayName(name, self.full_range)

<<<<<<< HEAD
    def test_easter_sunday(self):
        name = "Ostersonntag"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Brandenburg.
            if subdiv == "BB":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-04-12",
                    "2021-04-04",
                    "2022-04-17",
                    "2023-04-09",
                    "2024-03-31",
                    "2025-04-20",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_easter_monday(self):
        name = "Ostermontag"
        self.assertHolidayName(
            name,
=======
        for subdiv in DE.subdivisions:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)

    def test_ostersonntag(self):
        known_good = (
            "2014-04-20",
            "2015-04-05",
            "2016-03-27",
            "2017-04-16",
            "2018-04-01",
            "2019-04-21",
            "2020-04-12",
            "2021-04-04",
            "2022-04-17",
            "2023-04-09",
            "2024-03-31",
        )
        subdivs_that_have = {"BB"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(self.subdiv_holidays[subdiv], known_good)

    def test_ostermontag(self):
        known_good = (
            "2014-04-21",
            "2015-04-06",
            "2016-03-28",
            "2017-04-17",
            "2018-04-02",
            "2019-04-22",
>>>>>>> develop
            "2020-04-13",
            "2021-04-05",
            "2022-04-18",
            "2023-04-10",
            "2024-04-01",
            "2025-04-21",
        )
        self.assertHolidayName(name, self.full_range)

<<<<<<< HEAD
    def test_ascension_day(self):
        name = "Christi Himmelfahrt"
        self.assertHolidayName(
            name,
=======
        for subdiv in DE.subdivisions:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)

    def test_75_jahrestag_beendigung_zweiter_weltkrieg(self):
        subdivs_that_have = {"BE"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(self.subdiv_holidays[subdiv], "2020-05-08")
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(self.subdiv_holidays[subdiv], "2020-05-08")

    def test_80_jahrestag_beendigung_zweiter_weltkrieg(self):
        subdivs_that_have = {"BE"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(self.subdiv_holidays[subdiv], "2025-05-08")
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(self.subdiv_holidays[subdiv], "2025-05-08")

    def test_75_jahrestag_des_aufstandes_vom_17_juni_1953(self):
        subdivs_that_have = {"BE"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(self.subdiv_holidays[subdiv], "2028-06-17")
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(self.subdiv_holidays[subdiv], "2028-06-17")

    def test_christi_himmelfahrt(self):
        known_good = (
            "2014-05-29",
            "2015-05-14",
            "2016-05-05",
            "2017-05-25",
            "2018-05-10",
            "2019-05-30",
>>>>>>> develop
            "2020-05-21",
            "2021-05-13",
            "2022-05-26",
            "2023-05-18",
            "2024-05-09",
            "2025-05-29",
        )
        self.assertHolidayName(name, self.full_range)

<<<<<<< HEAD
    def test_labor_day(self):
        self.assertHolidayName("Erster Mai", (f"{year}-05-01" for year in self.full_range))

    def test_whit_sunday(self):
        name = "Pfingstsonntag"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Brandenburg.
            if subdiv == "BB":
                self.assertHolidayName(
                    name,
                    holidays,
                    "2020-05-31",
                    "2021-05-23",
                    "2022-06-05",
                    "2023-05-28",
                    "2024-05-19",
                    "2025-06-08",
                )
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

    def test_whit_monday(self):
        name = "Pfingstmontag"
        self.assertHolidayName(
            name,
=======
        for subdiv in DE.subdivisions:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)

    def test_weltkindertag(self):
        known_good = ("2019-09-20", "2021-09-20", "2022-09-20", "2023-09-20")
        subdivs_that_have = {"TH"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(self.subdiv_holidays[subdiv], known_good)

    def test_frauentag(self):
        self.assertHoliday(
            self.subdiv_holidays["BE"], (f"{year}-03-08" for year in range(2019, 2050))
        )
        self.assertHoliday(
            self.subdiv_holidays["MV"], (f"{year}-03-08" for year in range(2023, 2050))
        )

        for subdiv in set(DE.subdivisions):
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-03-08" for year in range(1991, 2019))
            )
        self.assertNoHoliday(
            self.subdiv_holidays["MV"], (f"{year}-03-08" for year in range(2019, 2023))
        )
        for subdiv in set(DE.subdivisions) - {"BE", "MV"}:
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-03-08" for year in range(2023, 2050))
            )

    def test_pfingstsonntag(self):
        known_good = (
            "2014-06-08",
            "2015-05-24",
            "2016-05-15",
            "2017-06-04",
            "2018-05-20",
            "2019-06-09",
            "2020-05-31",
            "2021-05-23",
            "2022-06-05",
            "2023-05-28",
            "2024-05-19",
        )
        subdivs_that_have = {"BB"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(self.subdiv_holidays[subdiv], known_good)

    def test_pfingstmontag(self):
        known_good = (
            "2014-06-09",
            "2015-05-25",
            "2016-05-16",
            "2017-06-05",
            "2018-05-21",
            "2019-06-10",
>>>>>>> develop
            "2020-06-01",
            "2021-05-24",
            "2022-06-06",
            "2023-05-29",
            "2024-05-20",
            "2025-06-09",
        )
        self.assertHolidayName(name, self.full_range)

<<<<<<< HEAD
    def test_corpus_christi(self):
        name = "Fronleichnam"
        self.assertNoHolidayName(name)
        dts = (
=======
        for subdiv in DE.subdivisions:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)

    def test_fronleichnam(self):
        known_good = (
            "2014-06-19",
            "2015-06-04",
            "2016-05-26",
            "2017-06-15",
            "2018-05-31",
            "2019-06-20",
>>>>>>> develop
            "2020-06-11",
            "2021-06-03",
            "2022-06-16",
            "2023-06-08",
            "2024-05-30",
            "2025-06-19",
        )
<<<<<<< HEAD
        for subdiv, holidays in self.subdiv_holidays.items():
            # Baden-Württemberg, Bayern, Hessen, Nordrhein-Westfalen,
            # Rheinland-Pfalz, Saarland, Augsburg.
            if subdiv in {"BW", "BY", "HE", "NW", "RP", "SL", "Augsburg"}:
                self.assertHolidayName(name, holidays, dts)
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertNoHolidayName(name, holidays)

        # Sachsen, Thüringen.
        self.assertSubdivSnCatholicHolidayName(name, dts)
        self.assertSubdivSnCatholicHolidayName(name, self.full_range)
        self.assertSubdivThCatholicHolidayName(name, dts)
        self.assertSubdivThCatholicHolidayName(name, self.full_range)

    def test_augsburg_peace_festival(self):
        name = "Augsburger Hohes Friedensfest"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Augsburg.
            if subdiv == "Augsburg":
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-08" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

    def test_assumption_day(self):
        name = "Mariä Himmelfahrt"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Saarland.
            if subdiv in {"SL", "Augsburg"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-08-15" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)

        # Bayern.
        self.assertSubdivByCatholicHolidayName(name, (f"{year}-08-15" for year in self.full_range))

    def test_world_childrens_day(self):
        name = "Weltkindertag"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Thüringen.
            if subdiv == "TH":
                self.assertHolidayName(
                    name, holidays, (f"{year}-09-20" for year in range(2019, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2019))
            else:
                self.assertNoHolidayName(name, holidays)

    def test_german_unity_day(self):
        self.assertHolidayName(
            "Tag der Deutschen Einheit", (f"{year}-10-03" for year in self.full_range)
        )

    def test_reformation_day(self):
        name = "Reformationstag"
        for subdiv, holidays in self.subdiv_holidays.items():
            # Brandenburg, Mecklenburg-Vorpommern, Sachsen, Sachsen-Anhalt, Thüringen.
            if subdiv in {"BB", "MV", "SN", "ST", "TH"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-31" for year in self.full_range)
                )
            # Bremen, Hamburg, Niedersachsen, Schleswig-Holstein.
            elif subdiv in {"HB", "HH", "NI", "SH"}:
                # While these subdivisions started their holiday observance in 2018,
                # this is de facto implemented in 2017's nationwide special observance.
                self.assertHolidayName(
                    name, holidays, (f"{year}-10-31" for year in range(2017, self.end_year))
                )
                self.assertNoHolidayName(name, holidays, range(self.start_year, 2017))
            else:
                self.assertHolidayName(name, holidays, "2017-10-31")
                self.assertNoHolidayName(
                    name, holidays, range(self.start_year, 2017), range(2018, self.end_year)
                )
        self.assertHolidayName(name, "2017-10-31")

    def test_all_saints_day(self):
        name = "Allerheiligen"
        self.assertNoHolidayName(name)
        for subdiv, holidays in self.subdiv_holidays.items():
            # Baden-Württemberg, Bayern, Nordrhein-Westfalen, Rheinland-Pfalz, Saarland, Augsburg.
            if subdiv in {"BW", "BY", "NW", "RP", "SL", "Augsburg"}:
                self.assertHolidayName(
                    name, holidays, (f"{year}-11-01" for year in self.full_range)
                )
            else:
                self.assertNoHolidayName(name, holidays)
=======
        subdivs_that_have = {"BW", "BY", "HE", "NW", "RP", "SL"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(self.subdiv_holidays[subdiv], known_good)

    def test_mariae_himmelfahrt(self):
        subdivs_that_have = {"SL"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-08-15" for year in range(1991, 2050))
            )
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-08-15" for year in range(1991, 2050))
            )
        # Bayern (Catholic municipalities).
        self.assertHoliday(
            DE(subdiv="BY", years=range(1991, 2050), categories=(CATHOLIC)),
            (f"{year}-08-15" for year in range(1991, 2050)),
        )

    def test_reformationstag(self):
        subdiv_yes = {"BB", "MV", "SN", "ST", "TH"}
        subdiv_yes_since_2018 = {"HB", "HH", "NI", "SH"}
        subdiv_not = set(DE.subdivisions) - subdiv_yes
        subdiv_not_since_2018 = subdiv_not - subdiv_yes_since_2018

        for subdiv in subdiv_yes:
            self.assertHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-10-31" for year in range(1991, 2050))
            )
        for subdiv in subdiv_yes_since_2018:
            self.assertHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-10-31" for year in range(2018, 2050))
            )
        for subdiv in DE.subdivisions:
            self.assertHoliday(self.subdiv_holidays[subdiv], "2017-10-31")

        for subdiv in subdiv_not:
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-10-31" for year in range(1991, 2017))
            )
        for subdiv in subdiv_not_since_2018:
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-10-31" for year in range(2018, 2050))
            )

    def test_allerheiligen(self):
        subdivs_that_have = {"BW", "BY", "NW", "RP", "SL"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-11-01" for year in range(1991, 2050))
            )
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(
                self.subdiv_holidays[subdiv], (f"{year}-11-01" for year in range(1991, 2050))
            )
>>>>>>> develop

    def test_repentance_and_prayer_day(self):
        name = "Buß- und Bettag"
        dts_pre_1995 = (
            "1991-11-20",
            "1992-11-18",
            "1993-11-17",
            "1994-11-16",
        )
        dts = (
            "2020-11-18",
            "2021-11-17",
            "2022-11-16",
            "2023-11-22",
            "2024-11-20",
            "2025-11-19",
        )
<<<<<<< HEAD
        for subdiv, holidays in self.subdiv_holidays.items():
            # Sachsen.
            if subdiv == "SN":
                self.assertHolidayName(name, holidays, dts, dts_pre_1995)
                self.assertHolidayName(name, holidays, self.full_range)
            else:
                self.assertHolidayName(name, holidays, dts_pre_1995)
                self.assertNoHolidayName(name, holidays, range(1995, self.end_year))
        self.assertHolidayName(name, dts_pre_1995)
        self.assertNoHolidayName(name, range(1995, self.end_year))

    def test_christmas_day(self):
        self.assertHolidayName(
            "Erster Weihnachtstag", (f"{year}-12-25" for year in self.full_range)
        )

    def test_second_day_of_christmas(self):
        self.assertHolidayName(
            "Zweiter Weihnachtstag", (f"{year}-12-26" for year in self.full_range)
        )
=======
        subdivs_that_have = {"SN"}
        subdivs_that_dont = set(DE.subdivisions) - subdivs_that_have

        for subdiv in subdivs_that_have:
            self.assertHoliday(self.subdiv_holidays[subdiv], known_good)
        for subdiv in subdivs_that_dont:
            self.assertNoHoliday(self.subdiv_holidays[subdiv], known_good)
>>>>>>> develop

    def test_l10n_default(self):
        self.assertLocalizedHolidays(
            ("2022-01-01", "Neujahr"),
            ("2022-01-06", "Heilige Drei Könige"),
<<<<<<< HEAD
            ("2022-03-08", "Frauentag"),
=======
            ("2022-03-08", "Internationaler Frauentag"),
>>>>>>> develop
            ("2022-04-15", "Karfreitag"),
            ("2022-04-17", "Ostersonntag"),
            ("2022-04-18", "Ostermontag"),
            ("2022-05-01", "Erster Mai"),
            ("2022-05-26", "Christi Himmelfahrt"),
            ("2022-06-05", "Pfingstsonntag"),
            ("2022-06-06", "Pfingstmontag"),
            ("2022-06-16", "Fronleichnam"),
<<<<<<< HEAD
            ("2022-08-08", "Augsburger Hohes Friedensfest"),
=======
>>>>>>> develop
            ("2022-08-15", "Mariä Himmelfahrt"),
            ("2022-09-20", "Weltkindertag"),
            ("2022-10-03", "Tag der Deutschen Einheit"),
            ("2022-10-31", "Reformationstag"),
            ("2022-11-01", "Allerheiligen"),
            ("2022-11-16", "Buß- und Bettag"),
            ("2022-12-25", "Erster Weihnachtstag"),
            ("2022-12-26", "Zweiter Weihnachtstag"),
        )

    def test_l10n_en_us(self):
        self.assertLocalizedHolidays(
            "en_US",
            ("2022-01-01", "New Year's Day"),
            ("2022-01-06", "Epiphany"),
<<<<<<< HEAD
            ("2022-03-08", "Women's Day"),
=======
            ("2022-03-08", "International Women's Day"),
>>>>>>> develop
            ("2022-04-15", "Good Friday"),
            ("2022-04-17", "Easter Sunday"),
            ("2022-04-18", "Easter Monday"),
            ("2022-05-01", "Labor Day"),
            ("2022-05-26", "Ascension Day"),
            ("2022-06-05", "Whit Sunday"),
            ("2022-06-06", "Whit Monday"),
            ("2022-06-16", "Corpus Christi"),
<<<<<<< HEAD
            ("2022-08-08", "Augsburg Peace Festival"),
=======
>>>>>>> develop
            ("2022-08-15", "Assumption Day"),
            ("2022-09-20", "World Children's Day"),
            ("2022-10-03", "German Unity Day"),
            ("2022-10-31", "Reformation Day"),
            ("2022-11-01", "All Saints' Day"),
            ("2022-11-16", "Repentance and Prayer Day"),
            ("2022-12-25", "Christmas Day"),
            ("2022-12-26", "Second Day of Christmas"),
        )

    def test_l10n_th(self):
        self.assertLocalizedHolidays(
            "th",
            ("2022-01-01", "วันขึ้นปีใหม่"),
            ("2022-01-06", "วันสมโภชพระคริสต์แสดงองค์"),
<<<<<<< HEAD
            ("2022-03-08", "วันสตรี"),
=======
            ("2022-03-08", "วันสตรีสากล"),
>>>>>>> develop
            ("2022-04-15", "วันศุกร์ประเสริฐ"),
            ("2022-04-17", "วันอาทิตย์อีสเตอร์"),
            ("2022-04-18", "วันจันทร์อีสเตอร์"),
            ("2022-05-01", "วันแรงงาน"),
            ("2022-05-26", "วันสมโภชพระเยซูเจ้าเสด็จขึ้นสวรรค์"),
            ("2022-06-05", "วันสมโภชพระจิตเจ้า"),
            ("2022-06-06", "วันจันทร์หลังวันสมโภชพระจิตเจ้า"),
            ("2022-06-16", "วันสมโภชพระคริสตวรกาย"),
<<<<<<< HEAD
            ("2022-08-08", "วันเทศกาลสันติภาพเอาก์สบวร์ก"),
=======
>>>>>>> develop
            ("2022-08-15", "วันสมโภชแม่พระรับเกียรติยกขึ้นสวรรค์"),
            ("2022-09-20", "วันเด็กสากล"),
            ("2022-10-03", "วันรวมชาติเยอรมัน"),
            ("2022-10-31", "วันแห่งการปฏิรูป"),
            ("2022-11-01", "วันสมโภชนักบุญทั้งหลาย"),
            ("2022-11-16", "วันแห่งการอธิษฐานและการกลับใจ"),
            ("2022-12-25", "วันคริสต์มาสวันแรก"),
            ("2022-12-26", "วันคริสต์มาสวันที่สอง"),
        )

    def test_l10n_uk(self):
        self.assertLocalizedHolidays(
            "uk",
            ("2022-01-01", "Новий рік"),
            ("2022-01-06", "Богоявлення"),
<<<<<<< HEAD
            ("2022-03-08", "Жіночий день"),
=======
            ("2022-03-08", "Міжнародний жіночий день"),
>>>>>>> develop
            ("2022-04-15", "Страсна пʼятниця"),
            ("2022-04-17", "Великдень"),
            ("2022-04-18", "Великодній понеділок"),
            ("2022-05-01", "День праці"),
            ("2022-05-26", "Вознесіння Господнє"),
            ("2022-06-05", "Трійця"),
            ("2022-06-06", "День Святого Духа"),
            ("2022-06-16", "Свято Тіла і Крові Христових"),
<<<<<<< HEAD
            ("2022-08-08", "Аугсбурзьке свято миру"),
=======
>>>>>>> develop
            ("2022-08-15", "Внебовзяття Пресвятої Діви Марії"),
            ("2022-09-20", "Всесвітній день дітей"),
            ("2022-10-03", "День німецької єдності"),
            ("2022-10-31", "День Реформації"),
            ("2022-11-01", "День усіх святих"),
            ("2022-11-16", "День молитви та покаяння"),
            ("2022-12-25", "Перший день Різдва"),
            ("2022-12-26", "Другий день Різдва"),
        )
