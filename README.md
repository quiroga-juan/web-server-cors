Universidad de Buenos Aires - FIUBA
Seminario de Electrónica
Construcción de Software Seguro
Trabajo práctico 2: OWASP Top 10 - Configuración CORS
2do cuatrimestre de 2023
---

## Prerrequisitos

1. Instalar [Docker](https://www.docker.com/)

## Correr Docker

Build:

```
cd deployment
docker compose build
```

Run:

```
docker compose up
```

Esto ya hace correr la aplicacion que expone el web server vulnerable en el puerto 8000 y el malicioso en el puerto 8001.

### Para acceder a la página vulnerable:

1. Abrir un browser de preferencia.
1. Ir a la URL `localhost:8000/login`
1. Escribir Nombre de usuario y contraseña. La contraseña está hardcodeada: "admin".

### Para ver que la página maliciosa puede acceder a la informacion cuando CORS es demasiado permisivo:

1. Abrir otra pestaña en el mismo Browser.
1. Ir a la URL `localhost:8001`
1. Tocar el boton "Get Info".
1. Abrir la consola con F12 y chequear que se haya logueado la informacion de la página vulnerable.

### Para ver que la página maliciosa no puede acceder a la informacion cuando CORS esta correctamente seteado:

1. Abrir otra pestaña en el mismo Browser.
1. Ir a la URL `localhost:8001/with-cors`
1. Tocar el boton "Get Info".
1. Abrir la consola con F12 y chequear que la informacion esperado no haya sido loggeada.


### Para chequear que CORS funciona correctamente desde un subdominio de la página vulnerable

1. Abrir otra pestaña en el mismo Browser.
1. Ir a la URL `localhost:8000/subdomain`
1. Tocar el boton "Get Info".
1. Abrir la consola con F12 y chequear que se haya logueado la informacion de la página vulnerable.
