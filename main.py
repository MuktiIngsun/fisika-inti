import streamlit as st
import numpy  as np
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Fisika Inti", page_icon=":chart_with_upwards_trend:")
with st.container():
	st.title("Tugas Akhir Fisika Inti") 
	st.write("sebenarnya ngga perlu dibikin webnya sih, cuma gara - gara ngga bisa tidur. HELP!!!! :persevere:")
	st.write("[kepoin kodenya disini :point_left:](https://github.com/MuktiIngsun/fisika-inti.git)")

with st.container():
	st.write("---")
	st.header("Topik 1: BE, SEM dan Magic Numbers")
	uploaded_file = st.file_uploader("Choose a file")
	if uploaded_file is not None:
		dataframe = pd.read_csv(uploaded_file,sep='\s+',header=None)
		st.write(dataframe)
		A = dataframe[0]
		Z = dataframe[1]
		Be = dataframe[2]/1000
		N = A - Z
		ex = Be/A
		# Parameter yang digunakan.
		aV, aS, aC, aA, delta = 15.75, 17.8, 0.711, 23.7, 11.18
		# menentukan tanda delta
		sgn = np.zeros(Z.shape)
		sgn[(Z%2) & (N%2)] = -1
		sgn[~(Z%2) & ~(N%2)] = +1
		# SEMF
		E = (aV - aS / A**(1/3) - aC * Z**2 / A**(4/3) - aA * (A-2*Z)**2/A**2 + sgn * delta/A**(3/2))
		# Plotting
		st.subheader("BE/A hasil eksperimen")
		fig1, ax = plt.subplots()
		ax.set_title('BE/A hasil eksperimen')
		ax.set_xlabel('A')
		ax.set_ylabel('BE(MeV)/A Eksperimen')
		ax.plot(A, ex, 'b*')
		st.pyplot(fig1) 

		st.subheader("BE hasil perhitungan model SEM")
		fig2, ax = plt.subplots()
		ax.set_title('BE hasil perhitungan model SEM')
		ax.set_xlabel('A')
		ax.set_ylabel('BE(MeV)/A SEM')
		ax.plot(A, E,'m*')
		st.pyplot(fig2)

		st.subheader("Gabungan Plot BE/A hasil eksperimen dan BE hasil perhitungan model SEM")
		fig3, ax = plt.subplots()
		ax.plot(A, ex,'b*', label='Eksperimen')
		ax.plot(A, E, 'm*', label='SEM')
		ax.set_title('Gabungan Plot BE/A hasil eksperimen dan BE hasil perhitungan model SEM')
		ax.set_xlabel(r'A')
		ax.set_ylabel(r'BE/A')
		ax.legend()
		st.pyplot(fig3)

		st.subheader("Magic Numbers")
		mn=A*(ex-E)
		fig4, ax = plt.subplots()
		ax.set_title('Magic Numbers')
		ax.set_xlabel('Z')
		ax.set_ylabel('BE/A Eksperimen - BE/A SEM')
		ax.plot(Z, mn,'k*')
		st.pyplot(fig4)

		fig5, ax = plt.subplots()
		ax.set_title('Magic Numbers')
		ax.set_xlabel('N')
		ax.set_ylabel('BE/A Eksperimen - BE/A SEM')
		ax.plot(N, mn,'k*')
		st.pyplot(fig5)
	else:
		st.write("Data belum dimasukkan/tidak dapat diproses! Coba file yang ada di folder")
