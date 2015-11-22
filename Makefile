

AstroPongScore:
		pyuic4 design.ui -o design.py
		pyuic4 dialog.ui -o dialog.py		
		python setup.py py2app -A --packages=PyQt4
		mv dist/main.app AstroPongScore.app

clean:
	rm -r AstroPongScore.app