# ===================================
# Data Karyawan APM company
# ===================================
# Developed by. Adrian Putra Mangkuratmadja
# JCDS - BSDAM29


# /************************************/

Data_Karyawan = [
    {
        'No_id'         : 'MK01',
        'Nama'          : 'Adrian',
        'Jabatan'       : 'Manager',
        'Departemen'    : 'Marketing'
    },
    {
        'No_id'         : 'MK02',
        'Nama'          : 'Rofi',
        'Jabatan'       : 'Executive',
        'Departemen'    : 'Marketing'
    },
    {
        'No_id'         : 'MK03',
        'Nama'          : 'Farchan',
        'Jabatan'       : 'Supervisor',
        'Departemen'    : 'Marketing'
    },
    {
        'No_id'         : 'MK04',
        'Nama'          : 'Darren',
        'Jabatan'       : 'Administrasi',
        'Departemen'    : 'Marketing'
    },
    {
        'No_id'         : 'FN01',
        'Nama'          : 'Audi',
        'Jabatan'       : 'Manager',
        'Departemen'    : 'Finance'
    },
    {
     'No_id'            : 'FN02',
        'Nama'          : 'Ben',
        'Jabatan'       : 'Executive',
        'Departemen'    : 'Finance'
    },
    {
        'No_id'         : 'FN03',
        'Nama'          : 'Caesar',
        'Jabatan'       : 'Supervisor',
        'Departemen'    : 'Finance'
    },
    {
        'No_id'         : 'FN04',
        'Nama'          : 'Deka',
        'Jabatan'       : 'Administrasi',
        'Departemen'    : 'Finance'
    }
]


#Melihat Data Karyawan
def report():
    while True:
        print('''
===========================
    Report Data Karyawan :
===========================
    1. Report Seluruh Data 
    2. Report Data Tertentu
    3. Kembali ke menu utama
''')

        inputreport = int(input('Silahkan pilih menu berikut(1 -3): '))

        if inputreport ==1:
            print('Data Karyawan\n')
            print('No_id\t Nama          \t Jabatan\t Departemen')
            for i,j in enumerate(Data_Karyawan): 
                    print('{}\t{}        \t {} \t{}'.format(j['No_id'],j['Nama'],j['Jabatan'],j['Departemen'],))

        elif inputreport ==2:
            report2 = (input('Masukan No_id:')).upper()
            print(f'Data Karyawan dengan No_id: {report2}')

            for i,j in enumerate(Data_Karyawan):
                if report2 == j['No_id']:
                    print(f'{'No_id':<10}|{'Nama':<10}|{'Jabatan':<14}|{'Departemen':<12}|')
                    print('{:<10}|{:<10}|{:<14}|{:<12}|'.format(j['No_id'],j['Nama'],j['Jabatan'],j['Departemen'],))
                    break

                elif report2 != j['No_id'] and (i == len(Data_Karyawan)-1):
                    print('Data Tidak Ada')
                    break

        elif inputreport == 3:
            break

        else:
            print('Pilihan Yang Anda Masukan Salah')
        
# Menambah Data Karyawan
def tambah():
    while True:
        print('''
===========================
    Menambah Data Karyawan:
===========================
    1. Tambah Data Karyawan
    2. Kembali ke Menu Utama
''')
        inputTambah = int(input('Silahkan Pilih Sub Menu Tambah Data Karyawan (1-2):'))\
        
        if inputTambah == 1:
            inputTambah2 = (input('Masukan No_id:')).upper()
            for i,j in enumerate(Data_Karyawan):
                if inputTambah2 == j['No_id']:
                    print('Data Sudah Ada')
                    break
                
                elif inputTambah2           != j['No_id'] and (i == len(Data_Karyawan)-1):
                    Nama_Karyawan            = str(input('Masukan Nama Karyawan:'))
                    Jabatan_Karyawan         = input('Masukan Jabatan Karyawan:').capitalize()
                    Departement_Karyawan     = input ('Masukan Departemen Karyawan:').capitalize()
                    Simpan_Data              = input('Apakah Data Akan Disimpan? (Y/N):').upper()

                    if Simpan_Data =='Y' :
                        print('Data Tersimpan')
                        Data_Karyawan.append({
                            'No_id': inputTambah2,
                            'Nama': Nama_Karyawan,
                            'Jabatan': Jabatan_Karyawan,
                            'Departemen' : Departement_Karyawan,
                        })
                    elif Simpan_Data =='N' :
                        print('Data Tidak Tersimpan')
                    else :
                        print('Data Tidak Tersimpan, Hanya Ada Pilihan  Y atau N')
                    break

        elif inputTambah == 2: 
            break

        else:
            print('Pilihan Yang Anda Masukan Salah')

# Mengubah Data Karyawan
def ubah():
    while True:
        print('''
===========================
    Mengubah Data Karyawan :
===========================
    1. Ubah Data Karyawan
    2. Kembali ke Menu Utama
''')
        
        inputubah = int(input('Silahkan Pilih Sub Menu Ubah Data Karyawan (1-2)'))

        if inputubah == 1:
            inputubah2 = (input('Masukan No_id:')).upper()

            for i,j in enumerate(Data_Karyawan):
                if inputubah2 == j['No_id']:
                    print('No_id\tNama      \t Jabatan\t Departemen')
                    print('{}\t{}           \t {} \t{}'.format(j['No_id'],j['Nama'],j['Jabatan'],j['Departemen'],))

                    inputubah3 = input('Tekan Y Jika Ingin Melanjutkan Ubah Data atau N Jika Ingin Membatalkan (Y/N):').capitalize()
                    if inputubah3 == 'Y':
                        kolomubah = input ('Masukan Kolom/Keterangan Yang Ingin Diedit:').capitalize()
                        for key in j.keys():
                            if kolomubah == key :
                                inputubah4 = input (f'Masukan {kolomubah} Baru:').capitalize()
                                inputubah5 = input('Apakah Data Akan Diupdate?(Y/N):').upper()
                                if inputubah5 == 'Y':
                                    j[kolomubah] = inputubah4
                                    print('Data Updated')
                                elif inputubah5 == 'N':
                                    print('Data Tidak Diupdate Karena Memilih N')
                                else:
                                    print('Data Tidak Diupdate Karena Memilih Pilihan Hanya Y dan N')
                                    break
                    else:
                        break
                    break

                elif inputubah2 != j['No_id'] and (i == len(Data_Karyawan)-1):
                    print('Data Tidak Ada')
                    break

        elif inputubah == 2:
            break
        else:
            print('Pilihan Yang Anda Masukan Salah')
        
# Menghapus Data Karyawan
def hapus():
    while True:
        print('''
=============================
    1. Hapus Data Karyawan
    2. Kembali ke Menu Utama
=============================
''')
        inputhapus = int(input('Silahkan Pilih Sub Menu Hapus Data Karyawan (1-2):'))

        if inputhapus == 1:
            inputhapus2 = (input('Masukan No_id:')).capitalize()

            for i,j in enumerate(Data_Karyawan):
                if inputhapus2 == j['No_id']:
                    print ('No_id\t Nama        \t Jabatan\t Departemen')
                    print('{}\t{}               \t {} \t{}'.format(j['No_id'],j['Nama'],j['Jabatan'],j['Departemen'],))

                    hapusData = input('Apakah Anda Yakin Data Akan Dihapus? (Y/N):').upper()
                    if hapusData == 'Y':
                        del Data_Karyawan[i]
                        print('Data Deleted')
                    elif hapusData == 'N':
                        print('Data Tidak Terhapus Karena Memilih N')
                    else:
                        print('Data Tidak Terhapus, Hanya Ada Pilihan Y atau N')
                        break

                elif inputhapus2 !=j['No_id'] and (i == len(Data_Karyawan)-1):
                    print('Data Tidak Ada')
                    break
        elif inputhapus == 2:
            break
        else:
            print('Pilihan Yang Anda Masukan Salah')

while True:
    print('''
===========================
    Data Karyawan
===========================
    1. Report Data Karyawan
    2. Menambah Data Karyawan
    3. Mengubah Data Karyawan
    4. Menghapus Data Karyawan
    5. EXIT
''')
    menuNumber = int(input('Silahkan Pilih Menu utama (1-5):'))

    if menuNumber == 1:
        report()
    elif menuNumber == 2:
        tambah()
    elif menuNumber == 3:
        ubah()
    elif menuNumber == 4:
        hapus()
    elif menuNumber == 5:
        break
    else :

        print('Pilihan Yang anda Masukan Salah')

