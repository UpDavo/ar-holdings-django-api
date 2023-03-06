# API de productos e invoices

Este API fue desarrollado utilizando Django y permite insertar, actualizar, eliminar, obtener información sobre productos e invoices. Los endpoints de la API permiten realizar estas operaciones y requieren de un token de autenticación para su uso.

## Configuración

Para utilizar este API, se requiere Python 3.6 o superior y una base de datos MySQL. Además, se deben instalar las dependencias del proyecto utilizando pip:

```
pip install -r requirements.txt
```

Antes de utilizar el API, se debe configurar la base de datos. Para ello, se debe crear una base de datos MySQL y configurar las credenciales en un archivo .env con los siguientes nombres:

```
DB_NAME=nombre_de_la_base_de_datos
DB_USER=nombre_de_usuario_de_la_base_de_datos
DB_PASSWORD=contraseña_de_la_base_de_datos
DB_HOST=host_de_la_base_de_datos
DB_PORT=puerto_de_la_base_de_datos
```

Además, se deben aplicar las migraciones del proyecto para crear las tablas en la base de datos:

```
python manage.py migrate
```

## Uso

El API cuenta con los siguientes endpoints:

## POST /api/products/insertProduct

Este endpoint permite insertar un nuevo producto en la base de datos. Requiere autenticación mediante token.

## POST /api/products/updateProduct

Este endpoint permite actualizar un producto existente en la base de datos. Requiere autenticación mediante token.

## POST /api/products/deleteProduct

Este endpoint permite eliminar un producto existente de la base de datos. Requiere autenticación mediante token.

## GET /api/products/getProducts

Este endpoint retorna una lista de todos los productos en la base de datos. Requiere autenticación mediante token.

## POST /api/invoice/setInvoice

Este endpoint permite crear una nueva invoice en la base de datos. Requiere autenticación mediante token.

## GET /api/invoice/getInvoice

Este endpoint retorna una lista de todas las invoices en la base de datos. Requiere autenticación mediante token.

## GET /api/invoice/getInvoice/<id>

Este endpoint retorna información sobre una invoice específica en la base de datos. Requiere autenticación mediante token.

## POST /api/token/auth

Este endpoint permite autenticarse en el API para obtener un token de autenticación. Requiere enviar las credenciales de acceso en el cuerpo de la solicitud.

Para autenticarse, se debe enviar las credenciales de acceso en el cuerpo de la solicitud en formato JSON con los campos username y password. El endpoint retornará un token de autenticación que debe ser utilizado en la cabecera HTTP Authorization para autenticar las solicitudes al API.

## Autorización

Para generar tokens de autenticación, se debe autenticarse en el API utilizando el endpoint `/api/token/auth`. El token generado debe ser utilizado en la cabecera HTTP `Authorization` para autenticar las solicitudes al API.

## Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulte el archivo `LICENSE` para obtener más información.
