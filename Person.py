from datetime import datetime
from enum import Enum


# ================== ENUM ==================

class Kategori(Enum):
    BAYI = "Bayi"
    BALITA = "Balita"
    ANAK = "Anak"
    DEWASA = "Dewasa"


# ================== CLASS ==================

class Person:
    def __init__(
        self,
        tinggi_badan: float,
        berat_aktual: float | None = None,
        bb_lahir: float | None = None,
        usia_bulan: float | None = None
    ):
        self.tinggi_badan = tinggi_badan
        self.berat_aktual = berat_aktual
        self.bb_lahir = bb_lahir
        self.usia_bulan = usia_bulan

    # ================== KATEGORI ==================

    def kategori(self) -> Kategori:
        if self.tinggi_badan <= 60:
            return Kategori.BAYI
        if self.tinggi_badan <= 70:
            return Kategori.BALITA
        if self.tinggi_badan <= 100:
            return Kategori.ANAK
        if self.tinggi_badan <= 200:
            return Kategori.DEWASA
        raise ValueError("Tinggi badan tidak valid")

    # ================== BERAT IDEAL ==================

    def berat_ideal_bayi(self) -> float:
        if self.bb_lahir is None or self.usia_bulan is None:
            raise ValueError("Data bayi belum lengkap")
        return self.bb_lahir + (self.usia_bulan * 0.7)

    def berat_ideal_balita(self) -> float:
        return (self.tinggi_badan - 60) * 0.6 + 6

    def berat_ideal_anak(self) -> float:
        return (self.tinggi_badan * 0.25) - 3

    def berat_ideal_dewasa(self) -> float:
        return self.tinggi_badan - 103

    # ================== BMI ==================

    def hitung_bmi(self) -> float:
        if self.berat_aktual is None or self.berat_aktual <= 0:
            raise ValueError("Berat badan tidak valid")

        tinggi_m = self.tinggi_badan / 100
        return self.berat_aktual / (tinggi_m ** 2)

    @staticmethod
    def kategori_bmi(bmi: float) -> str:
        if bmi < 18.5:
            return "Kurus"
        if bmi < 25:
            return "Normal"
        if bmi < 30:
            return "Kelebihan berat badan"
        return "Obesitas"

    # ================== MAIN LOGIC ==================

    def hitung_berat_ideal(self) -> str:
        kategori = self.kategori()

        if kategori == Kategori.BAYI:
            berat = self.berat_ideal_bayi()
            return f"{berat:.1f} kg adalah berat ideal bayi"

        if kategori == Kategori.BALITA:
            berat = self.berat_ideal_balita()
            return f"{berat:.1f} kg adalah berat ideal balita"

        if kategori == Kategori.ANAK:
            berat = self.berat_ideal_anak()
            return f"{berat:.1f} kg adalah berat ideal anak"

        # Dewasa
        berat_ideal = self.berat_ideal_dewasa()
        bmi = self.hitung_bmi()
        status = self.kategori_bmi(bmi)

        return (
            f"Berat ideal dewasa : {berat_ideal:.1f} kg\n"
            f"BMI anda           : {bmi:.1f}\n"
            f"Status tubuh       : {status}"
        )

    # ================== SAVE FILE ==================

    def simpan_ke_txt(self, hasil: str) -> None:
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("hasil_berat_ideal.txt", "a", encoding="utf-8") as file:
            file.write("=" * 40 + "\n")
            file.write(f"Waktu        : {waktu}\n")
            file.write(f"Tinggi badan : {self.tinggi_badan} cm\n")

            if self.berat_aktual is not None:
                file.write(f"Berat aktual : {self.berat_aktual} kg\n")
            if self.bb_lahir is not None:
                file.write(f"BB lahir     : {self.bb_lahir} kg\n")
            if self.usia_bulan is not None:
                file.write(f"Usia bayi    : {self.usia_bulan} bulan\n")

            file.write("\nHASIL:\n")
            file.write(hasil + "\n\n")


# ================== INPUT HELPER ==================

def input_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Input harus berupa angka.")


# ================== MAIN PROGRAM ==================

def main():
    while True:
        print("\n" + "=" * 30)
        print("Kalkulator Berat Badan Ideal")
        print("=" * 30)

        try:
            tinggi = input_float("Masukkan tinggi badan (cm): ")
            kategori = Person(tinggi).kategori()

            if kategori == Kategori.BAYI:
                bb_lahir = input_float("Berat badan lahir (kg): ")
                usia = input_float("Usia bayi (bulan): ")
                orang = Person(tinggi, bb_lahir=bb_lahir, usia_bulan=usia)
            else:
                berat = input_float("Berat badan saat ini (kg): ")
                orang = Person(tinggi, berat_aktual=berat)

            hasil = orang.hitung_berat_ideal()
            print("\n" + hasil)

            if input("\nSimpan hasil ke file? (y/n): ").lower() == "y":
                orang.simpan_ke_txt(hasil)
                print("Hasil berhasil disimpan.")

        except ValueError as e:
            print(f"Error: {e}")

        if input("\nTekan Enter untuk lanjut, 'q' untuk keluar: ").lower() == "q":
            print("Program dihentikan.")
            break


# ================== EXEC ==================

if __name__ == "__main__":
    main()
