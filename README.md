Velneo Server
=============
Instala y configura Velneo Server y su modulo de apache, vModApache.

Activa la licencia del servidor.

Opcionalmente, transfiere las aplicaciones desde repositorios Git.

Nota: Una vez que un servidor se intanta activar por tercera vez un servidor con la misma licencia, ésta se bloquea. En este caso es necesario solicitar a Velneo que la desbloquee.

https://doc.velneo.es/requerimientos-de-velneo.html

Cambios en ansible
------------------

Crear archivo de variables del servidor en host_vars

Cambios en inventario
---------------------

Agregar el nuevo servidor al inventario

Cambios en monitoreo
--------------------

* Puerto - Controlar que el puerto (velneo_port) esté escuchando.

Requerimientos
--------------

Este rol funciona solamente en Ubuntu Server 32 bits.
Requiere variables definidas para funcionar y firewall configurado.
Plataformas probadas:
Ubuntu 14.04 32bit.

Debe copiar los archivos de instalación de velneo en un directorio `files` en la misma ubicación que su playbook, ver [files/Readme.txt](files/Readme.txt)

Variables
---------

* velneo_port - En el host var del servidor asegurar de setear el puerto donde escucha el servidor de velneo.
* velneo_server_license - IMPORTANTE, es la licencia que va a usar el servidor de velneo.

Ver otras opciones de variables en [defaults/main.yml](defaults/main.yml)

Tags
----

Dependencias
------------

No depende de otros roles.

Ejemplo en Playbook
-------------------

    - name: setup velneo server
      hosts: velneo_servers
      become: yes
      become_method: sudo
      roles:
        - velneo_server

Afecta
------

* Apache
* /etc/pam.d/su
* /etc/security/limits.conf
* /storage
* Crea servicios
* Crea usuarios del sistema

Licencia
--------

BSD

Informacion del autor
---------------------

Diego Daguerre
Pablo Estigarribia
