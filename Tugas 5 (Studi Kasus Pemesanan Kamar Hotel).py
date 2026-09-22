#Studi Kasus 5: Pemesanan Kamar Hotel (Materi Function)

def hotel(jenis_kamar, durasi_menginap): #definisikan function hotel dengan parameter jenis_kamar dan durasi_menginap

    #percabangan untuk menentukan harga per malam berdasarkan jenis kamar
    if jenis_kamar == "Standard":
        harga_per_malam = 200000
    elif jenis_kamar == "Deluxe":
        harga_per_malam = 350000
    else:
        return "Jenis kamar tidak adaa." #return kalo jenis kamar tidak ada

    total_harga = harga_per_malam * durasi_menginap #menghitung total harga dengan mengalikan harga per malam dengan lama menginap
    return total_harga #return untuk mengembalikan total harga ke pemanggil function

#pemanggilan function hotel dengan input dari user
jenis_kamar = input("Masukkan jenis kamar (Standard/Deluxe): ")
tanggal_checkin = input("Masukkan tanggal check-in (dd/mm/yyyy): ")
tanggal_checkout = input("Masukkan tanggal check-out (dd/mm/yyyy): ")
durasi_menginap = int(input("Masukkan lama durasi menginap (dalam malam): "))

total_harga = hotel(jenis_kamar, durasi_menginap) #memanggil function hotel dengan parameter jenis_kamar dan durasi_menginap

#menampilkan output
print("===================================")
print("Detail Pemesanan Kamar Hotel")
print("Jenis kamar:", jenis_kamar)
print("Tanggal check-in:", tanggal_checkin) 
print("Tanggal check-out:", tanggal_checkout)
print("Durasi menginap:", durasi_menginap, "malam")
print("Total biaya yang harus dibayarkan: Rp", total_harga)
