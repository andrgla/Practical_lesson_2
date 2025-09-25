''' 
INE5431 Sistemas Multimídia
Prof. Roberto Willrich

Aula Prática IV: Compressão de Entropia

'''

from PIL import Image
from Cuif import Cuif
import math

def PSNR(original,decodificada,b):
    try:
        mse = MSE(original,decodificada) 
        psnr = 10*math.log10(((2**b-1)**2)/mse)
        return psnr
    except ZeroDivisionError:
        return "Infinito"

def MSE(ori, dec):
    mean = 0
    nsymbols = ori.width * ori.height * 3
    for i in range(ori.width):
        for j in range(ori.height):
            ori_r, ori_g, ori_b = ori.getpixel((i, j))
            dec_r, dec_g, dec_b = dec.getpixel((i, j))
            mean =  mean + (math.pow((ori_r - dec_r), 2)) + (math.pow((ori_g - dec_g), 2)) + (math.pow((ori_b - dec_b), 2))
    mean = mean / nsymbols
    return mean

if __name__ == "__main__":
    
    # Leitura da imagem 
    filepath = 'lena.bmp'
    imglena = Image.open(filepath)
    
    filepath = 'teste.bmp'
    imgteste = Image.open(filepath)
    # Indique a matrrícula dos alunos do grupo na lista abaixo
    matriculas = [23100481, 945542, 202503768]
    
    
    # Geração do arquivo Cuif.1, converte o arquivo Cuif.1 em BMP, e calcula o PSNR
    cuif1 = Cuif(imglena,1,matriculas)
    cuif1.printHeader()
    cuif1.show()
    cuif1.save('lena1.cuif')
    cuif1.saveBMP('lena1.bmp')
    imglena1 = Image.open('lena1.bmp')
    print("PSNR do CUIF.1",PSNR(imglena,imglena1,8)) 
    
    cuif1 = Cuif(imgteste,1,matriculas)
    cuif1.printHeader()
    cuif1.show()
    cuif1.save('teste1.cuif')
    cuif1.saveBMP('teste1.bmp')
    imgteste1 = Image.open('teste1.bmp')
    print("PSNR do CUIF.1",PSNR(imgteste,imgteste1,8)) 
    
    cuif2 = Cuif(imglena,2,matriculas)
    cuif2.printHeader()
    cuif2.show()
    cuif2.save('lena2.cuif')
    cuif2.saveBMP('lena2.bmp')
    imglena2 = Image.open('lena2.bmp')
    print("PSNR do CUIF.2",PSNR(imglena,imglena2,8)) 
    
    cuif2 = Cuif(imgteste,2,matriculas)
    cuif2.printHeader()
    cuif2.show()
    cuif2.save('teste2.cuif')
    cuif2.saveBMP('teste2.bmp')
    imgteste2 = Image.open('teste2.bmp')
    print("PSNR do CUIF.2",PSNR(imgteste,imgteste2,8)) 
    
    cuif3 = Cuif(imglena,3,matriculas)
    cuif3.printHeader()
    cuif3.show()
    cuif3.save('lena3.cuif')
    cuif3.saveBMP('lena3.bmp')
    imglena3 = Image.open('lena3.bmp')
    print("PSNR do CUIF.3",PSNR(imglena,imglena3,8)) 
    
    cuif3 = Cuif(imgteste,3,matriculas)
    cuif3.printHeader()
    cuif3.show()
    cuif3.save('teste3.cuif')
    cuif3.saveBMP('teste3.bmp')
    imgteste3 = Image.open('teste3.bmp')
    print("PSNR do CUIF.3",PSNR(imgteste,imgteste3,8)) 
    
    cuif4 = Cuif(imglena,4,matriculas)
    cuif4.printHeader()
    cuif4.show()
    cuif4.save('lena4.cuif')
    cuif4.saveBMP('lena4.bmp')
    imglena4 = Image.open('lena4.bmp')
    print("PSNR do CUIF.4",PSNR(imglena,imglena4,8)) 
    
    cuif4 = Cuif(imgteste,4,matriculas)
    cuif4.printHeader()
    cuif4.show()
    cuif4.save('teste4.cuif')
    cuif4.saveBMP('teste4.bmp')
    imgteste4 = Image.open('teste4.bmp')
    print("PSNR do CUIF.4",PSNR(imgteste,imgteste4,8)) 
