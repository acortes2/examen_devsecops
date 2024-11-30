# Usa la imagen base de Nginx
FROM nginx:latest

# Establece el directorio de trabajo en /usr/share/nginx/html
WORKDIR /usr/share/nginx/html

# Copia los archivos de la app al contenedor
COPY . /usr/share/nginx/html

# Expone el puerto 80 para servir la aplicación
EXPOSE 80


