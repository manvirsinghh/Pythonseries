#to take screenshot of screen we have to first ensure the installation of apckage pillow and pyscreenshot
import pyscreenshot
image=pyscreenshot.grab()
image.show()
# image.save("GeeksforGeeks.png")
image.save("manvir.pdf")