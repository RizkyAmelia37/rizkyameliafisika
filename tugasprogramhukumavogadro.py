def hitung_jumlah_mol_gas(v,k):
    n = v * k
    return n

def hitung_volume_gas(n,k):
    if n == 0:
        return  None

    v = n * k 
    return v

def hitung_konstanta_kesebandingan(v,n):
    k = v/n
    return k

def main():
    print("Program untuk menghitung Hukun Avgadro")
    print("1. Hitung Jumlah Mol gas (n)")
    print("2. Hitung Volume gas (v)")
    print("3. Hitung Konstanta Kesebandingan (k)")
    
    pilihan = input("Masukkan pilihan 1/2/3:")
    
    if pilihan == "1":
        v = float(input("Masukkan volume gas dalam liter:"))  
        k = float(input("Masukkan nilai konstanta kesebandingannya dalam N/m:"))
        n = hitung_jumlah_mol_gas (v,k)
        print(f"Jumlah mol gasnya sebesar: {n: .2f} mol")

    elif pilihan == "2":
        n = float(input("Masukkan Jumlah Mol gas dalam mol:"))
        k = float(input("Masukkan nilai konstanta kesebandingannya dalam N/m:"))
        v = hitung_volume_gas (n,k)
        print(f"Volume gasnya sebesar: {v: .2f} liter")

    elif pilihan == "3":
        v = float(input("Masukkan volume gasnya dalam liter:"))
        n = float(input("Masukkan Jumlah Mol gas dalam mol:"))
        k = hitung_konstanta_kesebandingan (v,n)
        print(f"Nilai konstanta kesebandingannya sebesar: {k: .2f} m")

    else:
        print("Pilihan tidak sesuai, silahkan pilih 1/2/3")

if __name__ == "__main__":
    main()
