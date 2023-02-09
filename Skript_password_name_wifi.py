# Данный код лишь проба своих способностей, в последствии может быть улучшен и дописан.
import subprocess

def getNetworks():# Код может не работать из-за другой кодировки на вашей Os, измените ее под свою Os.
    profile_info = subprocess.check_output('netsh wlan show profile').decode('cp866').split('\r\n')
    profil = [i.split(':')[1].strip() for i in profile_info if 'Все профили пользователей' in i]
    
    for profiles in profil:
        commands = subprocess.check_output(f'netsh wlan show profile  {profiles}   key=clear').decode('cp866').split('\r\n')
        # Если вам не нужен пароль и имя сети в текстовом документе, удалите или закоментируйте строки которые находятся ниже,
        # и воспользуйтесь этой строкой
        # print([name.split(':')[1].strip() for name in commands if 'Содержимое ключа' in name]), тогда у вас отобразится в консоли.

        with open(file='Wifi_name_passwd.txt', mode='a', encoding='utf-8') as file:
            file.write(str(profil))
            file.write(str([name.split(':')[1].strip() for name in commands if 'Содержимое ключа' in name]))
getNetworks()



