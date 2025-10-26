import time 
import pandas as pd 

def welcome(): 
    return """
-------------------------------------------------
|   Selamat datang di Laporan Pencatatan PKWU   |
|                                               | 
| 1. Next                                       | 
| 99. Exit                                      |
-------------------------------------------------
    """ 

def utama(): 
    return """
-------------------------------------------------
|                   Menu Utama                  |
|                                               | 
| 1. Pencatatan Penjualan PKWU                  | 
| 2. Lihat Laporan Penjualan PKWU               | 
| 3. Download Laporan Penjualan PKWU            |
| 99. Exit                                      |
-------------------------------------------------
    """ 
    
if __name__ == "__main__" : 
    listNamaProduk = [] 
    listJumlahTerjual = [] 
    listHargaSatuan = [] 
    listTotalPendapatanPerProduk = [] 
    totalPendapatan = 0 
    
    print(welcome()) 
    pilihan = input("Masukkan pilihanmu : ")
    
    while(pilihan != "99"):
        if pilihan == "1" :
            print(utama()) 
            pilihan = input("Masukkan pilihanmu : ") 
            while(pilihan != "99") : 
                if pilihan == "1" : 
                    namaProduk = input("\nNama produk : ") 
                    jumlahTerjual = int(input(f"Jumlah terjual produk {namaProduk} : ")) 
                    hargaSatuan = int(input(f"Harga satuan produk {namaProduk} : ")) 
                    
                    isProdukSama = False 
                    indexProduk = -1 
                    
                    for i in range(0, len(listNamaProduk)) : 
                        if listNamaProduk[i] == namaProduk and listHargaSatuan[i] == hargaSatuan : 
                            isProdukSama = True 
                            indexProduk = i 
                            break 
                    
                    if isProdukSama == True : 
                        listJumlahTerjual[indexProduk] = listJumlahTerjual[indexProduk] + jumlahTerjual 
                        listTotalPendapatanPerProduk[indexProduk] = listTotalPendapatanPerProduk[indexProduk] + (jumlahTerjual*hargaSatuan) 
                        totalPendapatan = totalPendapatan + (jumlahTerjual*hargaSatuan) 
                    else : 
                        listNamaProduk.append(namaProduk) 
                        listHargaSatuan.append(hargaSatuan) 
                        listJumlahTerjual.append(jumlahTerjual)
                        listTotalPendapatanPerProduk.append(jumlahTerjual*hargaSatuan) 
                        totalPendapatan = totalPendapatan + (jumlahTerjual*hargaSatuan) 
                            
                    print("\nData penjualan PKWU berhasil dicatat! \n") 
                elif pilihan == "2" : 
                    print("\n-------------------------------------------------")
                    print("             Laporan Penjualan PKWU              \n") 
                    
                    for i in range(0, len(listNamaProduk)) : 
                        print(f"Nama produk : {listNamaProduk[i]}") 
                        print(f"  - Terjual : {listJumlahTerjual[i]}") 
                        print(f"  - Harga stauan : Rp.{listHargaSatuan[i]:,.2f}") 
                        
                    print(f"\nTotal Pendapatan Semua Produk : Rp.{totalPendapatan:,.2f}")
                    print("-------------------------------------------------")
                elif pilihan == "3" : 
                    print("Download file sedang diproses ...") 
                    time.sleep(3) 
                    
                    data = {
                        'Nama Produk': listNamaProduk,
                        'Jumlah Terjual': listJumlahTerjual,
                        'Harga Produk': listHargaSatuan, 
                        'Total Pendapatan Perproduk': listTotalPendapatanPerProduk 
                    }

                    df = pd.DataFrame(data)

                    namaFile = 'Report_Penjualan_PKWU.xlsx'
                    df.to_excel(
                        namaFile,
                        sheet_name='PKWU',
                        index=False,
                        engine='openpyxl' 
                    )
                    
                    print(f"Data berhasil didownload dengan nama {namaFile}")
                elif pilihan == "99" : 
                    break 
                
                print(utama()) 
                pilihan = input("Masukkan pilihanmu : ") 
        else : 
            print("Pilihanmu salah.")
            pilihan = input("Masukkan pilihanmu : ")