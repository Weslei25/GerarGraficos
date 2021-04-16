from PyQt5 import QtWidgets, uic
import matplotlib.pyplot

def geragrafico():
	try:
		janeiro = tela.janeiro.text()
		fevereiro = tela.fevereiro.text()
		março = tela.marco.text()
		abril = tela.abril.text()
		maio = tela.maio.text()
		junho = tela.junho.text()
		julho = tela.julho.text()
		agosto = tela.agosto.text()
		setembro = tela.setembro.text()
		outubro = tela.outubro.text()
		novembro = tela.novembro.text()
		dezembro = tela.dezembro.text()

		valorjaneiro = int(tela.fatJaneiro.text())
		valorfevereiro = int(tela.fatFevereiro.text())
		valormarco = int(tela.fatMarco.text())
		valorabril = int(tela.fatAbril.text())
		valormaio = int(tela.fatMaio.text())
		valorjunho = int(tela.fatJunho.text())
		valorjulho = int(tela.fatJulho.text())
		valoragosto = int(tela.fatAgosto.text())
		valorsetembro = int(tela.fatSetembro.text())
		valoroutubro = int(tela.fatOutubro.text())
		valornovembro = int(tela.fatNovembro.text())
		valordezembro = int(tela.fatDezembro.text())
	except ValueError:
		tela.lineEdit.setText("Preencha os valores corretamente.")
		return
	except UnboundLocalError:
		tela.lineEdit.setText("Preencha os valores corretamente.")
		return


	meses = [janeiro, fevereiro, março, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro]
	valores = [valorjaneiro, valorfevereiro, valormarco, valorabril, valormaio, valorjunho, valorjulho, valoragosto, valorsetembro, valoroutubro, valornovembro, valordezembro]
	# valores = [105235, 107697, 110256, 109236, 108859, 109986]


	# matplotlib.pyplot.title('Faturamento no primeiro semestre de 2021')
	matplotlib.pyplot.title('Faturamento Total Anual R$')
	matplotlib.pyplot.xlabel('Meses')
	matplotlib.pyplot.ylabel('Faturamento em R$')
	matplotlib.pyplot.plot(meses, valores)
	matplotlib.pyplot.show()





app = QtWidgets.QApplication([])
app.setStyle ('Windows')
tela = uic.loadUi("Graficos.ui")
tela.gerargraficos.clicked.connect(geragrafico)

tela.show()
app.exec()