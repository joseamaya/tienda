Este pequeño aplicativo es para aprender django, es un sistemita de ventas que incluye la posibilidad de hacer facturas, todo adaptado al sistema peruano, he usado django, jquery, jquery-ui y bootstrap. Espero que sea de utilidad.
Para instalarlo debe crear la base de datos tienda en mysql.
Luego debe ingresar a la carpeta que ha clonado y poner la siguiente orden para crear las tablas.
python manage.py syncdb
Se debe correr la siguiente orden para levantar el servidor de pruebas de django:
python manage.py runserver
Y finalmente ingresamos al navegador y ponemos la siguiente direccion:
http://localhost:[puerto]/facturacion/
