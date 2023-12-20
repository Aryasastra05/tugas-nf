function hitungDuaBilangan(){
    // Dapatkan nilah inputtan user
    let bil1 = parseFloat(document.getElementById('bil1').value);
    let bil2 = parseFloat(document.getElementById('bil2').value);

    // Dapatkan alamen untuk mendapatkan hasil
    let hasil = document.getElementById('hasil')

    // Hitung penjumahan
    let hasiltambah =  bil1 + bil2

    console.log(hasiltambah)

    // Menampilkan hasil ke html
    hasil.value = hasiltambah
}