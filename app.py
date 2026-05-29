import streamlit as st

st.set_page_config(
    page_title = "Matematika Geometri",
    page_icon = "💿"
)

with st.sidebar:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("mtk4.png")
    st.title("Bangun Datar")
    pilihan = st.selectbox("Pilihan Bangun Datar", ["Persegi", "Persegi Panjang", "Lingkaran", "Jajar Genjang", "Segitiga"])
    st.caption("Dibuat dengan :fire: oleh **twiss**")

match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung luas dan keliling persegi")
        sisi = st.number_input("Masukkan sisi : ")
        if st.button("Hitung", type="primary") :
            luas = sisi * sisi
            keliling = 4 * sisi
            st.info(f"Luas Persegi adalah {luas:.2f} dan Kelilingnya adalah {keliling:2f}")
            col1,col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)
            st.snow()


    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung luas dan keliling persegi panjang")
        panjang = st.number_input("Masuka panjang")
        lebar = st.number_input("Masukkan lebar")
        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            st.info(f"Luas Persegi Panjang adalah {luas:2f} dan Kelilingnya adalah {keliling:.2f}")
            col1,col2 = st.columns ([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)
            st.snow()
        
    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung luas dan keliling lingkaran")
        jarijari = st.number_input("Masukkan jari jari")
        if st.button ("Hitung", type = "primary"):
            luas = 3.14 * jarijari
            keliling = 2 * 3.14 * jarijari
            st.info(f"Luas Lingkaran adalah  {luas:.2f} dan Kellingnya adalah {keliling:.2f}")
            col1,col2 = st.columns ([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)
            st.snow()
        
    case "Jajar Genjang":
        st.title("Jajar Genjang")
        st.markdown("Menghitung luas dan keliling jajar genjang")
        alas = st.number_input("Masukkan alas")
        tinggi = st.number_input("Masukkan tinggi")
        sisimiring = st.number_input("Masukkan sisi miring")
        if st.button("Hitung", type="primary"):
            luas = alas * tinggi
            keliling = 2 * (alas + sisimiring)
            st.info(f"Luas Jajar Genjang adalah {luas:.2f} dan Kelilingnya adalah {keliling:.2f}")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric("Luas", value=luas, border=True)
        with col2:
            st.metric("Keliling", value=keliling, border=True)
        st.snow()

    case "Segitiga":
        st.title("Segitiga")
        st.markdown("Menghitung luas dan keliling segitiga")
        alas = st.number_input("Masukkan alas", min_value=0.0)
        tinggi = st.number_input("Masukkan tinggi", min_value=0.0)
        sisi1 = st.number_input("Masukkan sisi 1", min_value=0.0)
        sisi2 = st.number_input("Masukkan sisi 2", min_value=0.0)
        sisi3 = st.number_input("Masukkan sisi 3", min_value=0.0)
        if st.button("Hitung", type="primary"):
            luas = 0.5 * alas * tinggi
            keliling = sisi1 + sisi2 + sisi3
            st.info(f"Luas Segitiga adalah {luas:.2f} dan Kelilingnya adalah {keliling:.2f}")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Luas", value=f"{luas:.2f}", border=True)
            with col2:
                st.metric("Keliling", value=f"{keliling:.2f}", border=True)
            st.snow()

    case _ :
        st.error("Terjadi kesalahan!")