import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class CadPass:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()        

    def login(self): 
        driver = self.driver
        driver.get("http://0.0.0.0/admin/login/")
        time.sleep(5)

        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)

        time.sleep(5)

        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)

        time.sleep(5)

        bot.cad()

    def cad(self):
        driver = self.driver
        driver.get("http://0.0.0.0/admin/core/passagem/add/")
        
        ref_arquivo = open("passagem.txt","r")
            
        time.sleep(5)

        for linha in ref_arquivo:
            time.sleep(3)

            valores = linha.split()

            if(valores[0] == 'Sun,'): #DOMINGO
                if(valores[1] == 'Jan'):
                    valores[1] = '01'

                elif(valores[1] == 'Feb'):
                    valores[1] = '02'

                elif(valores[1] == 'Mar'):
                    valores[1] = '03'

                elif(valores[1] == 'Apr'):
                    valores[1] = '04'

                elif(valores[1] == 'May'):
                    valores[1] = '05'

                elif(valores[1] == 'Jun'):
                    valores[1] = '06'

                elif(valores[1] == 'Jul'):
                    valores[1] = '07'

                elif(valores[1] == 'Aug'):
                    valores[1] = '08'

                elif(valores[1] == 'Sep'):
                    valores[1] = '09'

                elif(valores[1] == 'Oct'):
                    valores[1] = '10'

                elif(valores[1] == 'Nov'):
                    valores[1] = '11'

                elif(valores[1] == 'Dec'):
                    valores[1] = '12'

                dia = valores[2]
                mes = valores[1]
                ano = valores[3]
                data = dia.replace(',','/')+mes+'/'+ano
            
            if(valores[0] == 'Mon,'): #SEGUNDA
                if(valores[1] == 'Jan'):
                    valores[1] = '01'

                elif(valores[1] == 'Feb'):
                    valores[1] = '02'

                elif(valores[1] == 'Mar'):
                    valores[1] = '03'

                elif(valores[1] == 'Apr'):
                    valores[1] = '04'

                elif(valores[1] == 'May'):
                    valores[1] = '05'

                elif(valores[1] == 'Jun'):
                    valores[1] = '06'

                elif(valores[1] == 'Jul'):
                    valores[1] = '07'

                elif(valores[1] == 'Aug'):
                    valores[1] = '08'

                elif(valores[1] == 'Sep'):
                    valores[1] = '09'

                elif(valores[1] == 'Oct'):
                    valores[1] = '10'

                elif(valores[1] == 'Nov'):
                    valores[1] = '11'

                elif(valores[1] == 'Dec'):
                    valores[1] = '12'

                dia = valores[2]
                mes = valores[1]
                ano = valores[3]
                data = dia.replace(',','/')+mes+'/'+ano
            
            if(valores[0] == 'Tue,'): #TERCA
                if(valores[1] == 'Jan'):
                    valores[1] = '01'

                elif(valores[1] == 'Feb'):
                    valores[1] = '02'

                elif(valores[1] == 'Mar'):
                    valores[1] = '03'

                elif(valores[1] == 'Apr'):
                    valores[1] = '04'

                elif(valores[1] == 'May'):
                    valores[1] = '05'

                elif(valores[1] == 'Jun'):
                    valores[1] = '06'

                elif(valores[1] == 'Jul'):
                    valores[1] = '07'
                    
                elif(valores[1] == 'Aug'):
                    valores[1] = '08'

                elif(valores[1] == 'Sep'):
                    valores[1] = '09'

                elif(valores[1] == 'Oct'):
                    valores[1] = '10'

                elif(valores[1] == 'Nov'):
                    valores[1] = '11'

                elif(valores[1] == 'Dec'):
                    valores[1] = '12'
                
                dia = valores[2]
                mes = valores[1]
                ano = valores[3]
                data = dia.replace(',','/')+mes+'/'+ano
           
            if(valores[0] == 'Wed,'): #QUARTA
                if(valores[1] == 'Jan'):
                    valores[1] = '01'

                elif(valores[1] == 'Feb'):
                    valores[1] = '02'

                elif(valores[1] == 'Mar'):
                    valores[1] = '03'

                elif(valores[1] == 'Apr'):
                    valores[1] = '04'

                elif(valores[1] == 'May'):
                    valores[1] = '05'

                elif(valores[1] == 'Jun'):
                    valores[1] = '06'

                elif(valores[1] == 'Jul'):
                    valores[1] = '07'

                elif(valores[1] == 'Aug'):
                    valores[1] = '08'

                elif(valores[1] == 'Sep'):
                    valores[1] = '09'

                elif(valores[1] == 'Oct'):
                    valores[1] = '10'

                elif(valores[1] == 'Nov'):
                    valores[1] = '11'

                elif(valores[1] == 'Dec'):
                    valores[1] = '12'

                dia = valores[2]
                mes = valores[1]
                ano = valores[3]
                data = dia.replace(',','/')+mes+'/'+ano
            
            if(valores[0] == 'Thu,'): #QUINTA
                if(valores[1] == 'Jan'):
                    valores[1] = '01'

                elif(valores[1] == 'Feb'):
                    valores[1] = '02'

                elif(valores[1] == 'Mar'):
                    valores[1] = '03'

                elif(valores[1] == 'Apr'):
                    valores[1] = '04'

                elif(valores[1] == 'May'):
                    valores[1] = '05'

                elif(valores[1] == 'Jun'):
                    valores[1] = '06'

                elif(valores[1] == 'Jul'):
                    valores[1] = '07'

                elif(valores[1] == 'Aug'):
                    valores[1] = '08'

                elif(valores[1] == 'Sep'):
                    valores[1] = '09'

                elif(valores[1] == 'Oct'):
                    valores[1] = '10'

                elif(valores[1] == 'Nov'):
                    valores[1] = '11'

                elif(valores[1] == 'Dec'):
                    valores[1] = '12'

                dia = valores[2]
                mes = valores[1]
                ano = valores[3]
                data = dia.replace(',','/')+mes+'/'+ano
            
            if(valores[0] == 'Fri,'): #SEXTA
                if(valores[1] == 'Jan'):
                    valores[1] = '01'

                elif(valores[1] == 'Feb'):
                    valores[1] = '02'

                elif(valores[1] == 'Mar'):
                    valores[1] = '03'

                elif(valores[1] == 'Apr'):
                    valores[1] = '04'

                elif(valores[1] == 'May'):
                    valores[1] = '05'

                elif(valores[1] == 'Jun'):
                    valores[1] = '06'

                elif(valores[1] == 'Jul'):
                    valores[1] = '07'

                elif(valores[1] == 'Aug'):
                    valores[1] = '08'

                elif(valores[1] == 'Sep'):
                    valores[1] = '09'

                elif(valores[1] == 'Oct'):
                    valores[1] = '10'

                elif(valores[1] == 'Nov'):
                    valores[1] = '11'

                elif(valores[1] == 'Dec'):
                    valores[1] = '12'

                dia = valores[2]
                mes = valores[1]
                ano = valores[3]
                data = dia.replace(',','/')+mes+'/'+ano
            
            if(valores[0] == 'Sat,'): #SABADO
                if(valores[1] == 'Jan'):
                    valores[1] = '01'

                elif(valores[1] == 'Feb'):
                    valores[1] = '02'

                elif(valores[1] == 'Mar'):
                    valores[1] = '03'
                    
                elif(valores[1] == 'Apr'):
                    valores[1] = '04'

                elif(valores[1] == 'May'):
                    valores[1] = '05'

                elif(valores[1] == 'Jun'):
                    valores[1] = '06'

                elif(valores[1] == 'Jul'):
                    valores[1] = '07'

                elif(valores[1] == 'Aug'):
                    valores[1] = '08'

                elif(valores[1] == 'Sep'):
                    valores[1] = '09'

                elif(valores[1] == 'Oct'):
                    valores[1] = '10'

                elif(valores[1] == 'Nov'):
                    valores[1] = '11'

                elif(valores[1] == 'Dec'):
                    valores[1] = '12'
                
                dia = valores[2]                
                mes = valores[1]
                ano = valores[3]
                data = dia.replace(',','/')+mes+'/'+ano     

            if(valores[0] == '*'): #SATELITE

                if(valores[1] == 'Aqua'): #AQUA
                    select = Select(driver.find_element_by_id('id_antena'))
                    select.select_by_visible_text('Cacheira Paulista/CP6')

                    select = Select(driver.find_element_by_id('id_servidor'))
                    select.select_by_visible_text('DARTCOM-X')

                    datai = driver.find_element_by_xpath("//input[@name='inicio_0']")
                    datai.click()
                    datai.clear()
                    datai.send_keys(data)

                    dataf = driver.find_element_by_xpath("//input[@name='fim_0']")
                    dataf.click()
                    dataf.clear()
                    dataf.send_keys(data)

                    horai = driver.find_element_by_xpath("//input[@name='inicio_1']")
                    horai.click()
                    horai.clear()
                    horai.send_keys(valores[2])

                    horaf = driver.find_element_by_xpath("//input[@name='fim_1']")
                    horaf.click()
                    horaf.clear()
                    horaf.send_keys(valores[3])

                    select = Select(driver.find_element_by_id('id_sensor'))       
                    select.select_by_visible_text('AQUA/MODIS')

                    time.sleep(5)

                    driver.find_element_by_xpath("//button[contains(text(), 'Salvar e adicionar outro(a)')]").click()

                elif(valores[1] == 'Terra'): #TERRA
                    select = Select(driver.find_element_by_id('id_antena'))
                    select.select_by_visible_text('Cacheira Paulista/CP6')

                    select = Select(driver.find_element_by_id('id_servidor'))
                    select.select_by_visible_text('DARTCOM-X')

                    datai = driver.find_element_by_xpath("//input[@name='inicio_0']")
                    datai.click()
                    datai.clear()
                    datai.send_keys(data)

                    dataf = driver.find_element_by_xpath("//input[@name='fim_0']")
                    dataf.click()
                    dataf.clear()
                    dataf.send_keys(data)

                    horai = driver.find_element_by_xpath("//input[@name='inicio_1']")
                    horai.click()
                    horai.clear()
                    horai.send_keys(valores[2])

                    horaf = driver.find_element_by_xpath("//input[@name='fim_1']")
                    horaf.click()
                    horaf.clear()
                    horaf.send_keys(valores[3])

                    select = Select(driver.find_element_by_id('id_sensor'))         
                    select.select_by_visible_text('TERRA/MODIS')

                    time.sleep(5)
                    
                    driver.find_element_by_xpath("//button[contains(text(), 'Salvar e adicionar outro(a)')]").click()

                elif(valores[1] == 'JPSS-1'): #NOAA-20
                    select = Select(driver.find_element_by_id('id_antena'))
                    select.select_by_visible_text('Cacheira Paulista/CP6')

                    select = Select(driver.find_element_by_id('id_servidor'))
                    select.select_by_visible_text('DARTCOM-X')

                    datai = driver.find_element_by_xpath("//input[@name='inicio_0']")
                    datai.click()
                    datai.clear()
                    datai.send_keys(data)

                    dataf = driver.find_element_by_xpath("//input[@name='fim_0']")
                    dataf.click()
                    dataf.clear()
                    dataf.send_keys(data)

                    horai = driver.find_element_by_xpath("//input[@name='inicio_1']")
                    horai.click()
                    horai.clear()
                    horai.send_keys(valores[2])

                    horaf = driver.find_element_by_xpath("//input[@name='fim_1']")
                    horaf.click()
                    horaf.clear()
                    horaf.send_keys(valores[3])

                    select = Select(driver.find_element_by_id('id_sensor'))         
                    select.select_by_visible_text('NOAA20/VIIRS')

                    time.sleep(5)

                    driver.find_element_by_xpath("//button[contains(text(), 'Salvar e adicionar outro(a)')]").click()

                elif(valores[1] == 'Suomi'): #NPP
                    select = Select(driver.find_element_by_id('id_antena'))
                    select.select_by_visible_text('Cacheira Paulista/CP6')

                    select = Select(driver.find_element_by_id('id_servidor'))
                    select.select_by_visible_text('DARTCOM-X')

                    datai = driver.find_element_by_xpath("//input[@name='inicio_0']")
                    datai.click()
                    datai.clear()
                    datai.send_keys(data)

                    dataf = driver.find_element_by_xpath("//input[@name='fim_0']")
                    dataf.click()
                    dataf.clear()
                    dataf.send_keys(data)

                    horai = driver.find_element_by_xpath("//input[@name='inicio_1']")
                    horai.click()
                    horai.clear()
                    horai.send_keys(valores[3])

                    horaf = driver.find_element_by_xpath("//input[@name='fim_1']")
                    horaf.click()
                    horaf.clear()
                    horaf.send_keys(valores[4])

                    select = Select(driver.find_element_by_id('id_sensor'))         
                    select.select_by_visible_text('NPP/VIIRS')

                    time.sleep(5)

                    driver.find_element_by_xpath("//button[contains(text(), 'Salvar e adicionar outro(a)')]").click()

                elif(valores[1] == 'Metop-B'): #METOP-B
                    select = Select(driver.find_element_by_id('id_antena'))
                    select.select_by_visible_text('Cacheira Paulista/CP1')

                    select = Select(driver.find_element_by_id('id_servidor'))
                    select.select_by_visible_text('DARTCOM-L')

                    datai = driver.find_element_by_xpath("//input[@name='inicio_0']")
                    datai.click()
                    datai.clear()
                    datai.send_keys(data)

                    dataf = driver.find_element_by_xpath("//input[@name='fim_0']")
                    dataf.click()
                    dataf.clear()
                    dataf.send_keys(data)

                    horai = driver.find_element_by_xpath("//input[@name='inicio_1']")
                    horai.click()
                    horai.clear()
                    horai.send_keys(valores[2])

                    horaf = driver.find_element_by_xpath("//input[@name='fim_1']")
                    horaf.click()
                    horaf.clear()
                    horaf.send_keys(valores[3])

                    select = Select(driver.find_element_by_id('id_sensor'))         
                    select.select_by_visible_text('METOPB/AHRPT')

                    time.sleep(5)

                    driver.find_element_by_xpath("//button[contains(text(), 'Salvar e adicionar outro(a)')]").click()

                elif(valores[1] == 'Metop-C'): #METOP-C
                    select = Select(driver.find_element_by_id('id_antena'))
                    select.select_by_visible_text('Cacheira Paulista/CP1')

                    select = Select(driver.find_element_by_id('id_servidor'))
                    select.select_by_visible_text('DARTCOM-L')

                    datai = driver.find_element_by_xpath("//input[@name='inicio_0']")
                    datai.click()
                    datai.clear()
                    datai.send_keys(data)

                    dataf = driver.find_element_by_xpath("//input[@name='fim_0']")
                    dataf.click()
                    dataf.clear()
                    dataf.send_keys(data)

                    horai = driver.find_element_by_xpath("//input[@name='inicio_1']")
                    horai.click()
                    horai.clear()
                    horai.send_keys(valores[2])

                    horaf = driver.find_element_by_xpath("//input[@name='fim_1']")
                    horaf.click()
                    horaf.clear()
                    horaf.send_keys(valores[3])

                    select = Select(driver.find_element_by_id('id_sensor'))         
                    select.select_by_visible_text('METOPC/AHRPT')

                    time.sleep(5)

                    driver.find_element_by_xpath("//button[contains(text(), 'Salvar e adicionar outro(a)')]").click()
                
                elif(valores[1] == 'NOAA'): #NOAA
                    if(valores[2] == '18'): #NOAA18
                        select = Select(driver.find_element_by_id('id_antena'))
                        select.select_by_visible_text('Cacheira Paulista/CP1')

                        select = Select(driver.find_element_by_id('id_servidor'))
                        select.select_by_visible_text('DARTCOM-L')

                        datai = driver.find_element_by_xpath("//input[@name='inicio_0']")
                        datai.click()
                        datai.clear()
                        datai.send_keys(data)

                        dataf = driver.find_element_by_xpath("//input[@name='fim_0']")
                        dataf.click()
                        dataf.clear()
                        dataf.send_keys(data)

                        horai = driver.find_element_by_xpath("//input[@name='inicio_1']")
                        horai.click()
                        horai.clear()
                        horai.send_keys(valores[3])

                        horaf = driver.find_element_by_xpath("//input[@name='fim_1']")
                        horaf.click()
                        horaf.clear()
                        horaf.send_keys(valores[4])

                        select = Select(driver.find_element_by_id('id_sensor'))         
                        select.select_by_visible_text('NOAA18/HRPT')

                        time.sleep(5)

                        driver.find_element_by_xpath("//button[contains(text(), 'Salvar e adicionar outro(a)')]").click()

                    elif(valores[2] == '19'): #NOAA19
                        select = Select(driver.find_element_by_id('id_antena'))
                        select.select_by_visible_text('Cacheira Paulista/CP1')

                        select = Select(driver.find_element_by_id('id_servidor'))
                        select.select_by_visible_text('DARTCOM-L')

                        datai = driver.find_element_by_xpath("//input[@name='inicio_0']")
                        datai.click()
                        datai.clear()
                        datai.send_keys(data)

                        dataf = driver.find_element_by_xpath("//input[@name='fim_0']")
                        dataf.click()
                        dataf.clear()
                        dataf.send_keys(data)

                        horai = driver.find_element_by_xpath("//input[@name='inicio_1']")
                        horai.click()
                        horai.clear()
                        horai.send_keys(valores[3])

                        horaf = driver.find_element_by_xpath("//input[@name='fim_1']")
                        horaf.click()
                        horaf.clear()
                        horaf.send_keys(valores[4])

                        select = Select(driver.find_element_by_id('id_sensor'))         
                        select.select_by_visible_text('NOAA19/HRPT')

                        time.sleep(5)

                        driver.find_element_by_xpath("//button[contains(text(), 'Salvar e adicionar outro(a)')]").click()
                        
        ref_arquivo.close()    

        driver.close()

bot = CadPass('USUARIO', 'SENHA')

bot.login()