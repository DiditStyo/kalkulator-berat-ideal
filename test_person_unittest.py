import unittest
from Person import Person, Kategori

class TestPerson(unittest.TestCase):

    # ===== KATEGORI =====

    def test_kategori_bayi(self):
        p = Person(tinggi_badan=55)
        self.assertEqual(p.kategori(), Kategori.BAYI)

    def test_kategori_balita(self):
        p = Person(tinggi_badan=65)
        self.assertEqual(p.kategori(), Kategori.BALITA)

    def test_kategori_anak(self):
        p = Person(tinggi_badan=90)
        self.assertEqual(p.kategori(), Kategori.ANAK)

    def test_kategori_dewasa(self):
        p = Person(tinggi_badan=170)
        self.assertEqual(p.kategori(), Kategori.DEWASA)

    # ===== BERAT IDEAL =====

    def test_berat_ideal_bayi(self):
        p = Person(
            tinggi_badan=55,
            bb_lahir=3.2,
            usia_bulan=6
        )
        self.assertAlmostEqual(p.berat_ideal_bayi(), 7.4, places=1)

    def test_berat_ideal_dewasa(self):
        p = Person(tinggi_badan=170)
        self.assertEqual(p.berat_ideal_dewasa(), 67)

    # ===== BMI =====

    def test_hitung_bmi(self):
        p = Person(tinggi_badan=170, berat_aktual=65)
        bmi = p.hitung_bmi()
        self.assertAlmostEqual(bmi, 22.5, places=1)

    def test_kategori_bmi(self):
        self.assertEqual(Person.kategori_bmi(17), "Kurus")
        self.assertEqual(Person.kategori_bmi(22), "Normal")
        self.assertEqual(Person.kategori_bmi(27), "Kelebihan berat badan")
        self.assertEqual(Person.kategori_bmi(32), "Obesitas")

    # ===== ERROR HANDLING =====

    def test_bmi_berat_invalid(self):
        p = Person(tinggi_badan=170, berat_aktual=0)
        with self.assertRaises(ValueError):
            p.hitung_bmi()

    def test_kategori_tinggi_invalid(self):
        p = Person(tinggi_badan=250)
        with self.assertRaises(ValueError):
            p.kategori()


if __name__ == "__main__":
    unittest.main()
