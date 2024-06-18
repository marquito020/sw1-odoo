FROM odoo:14.0

LABEL maintainer="your-email@example.com"

# Copia el archivo de configuración en la imagen
COPY ./odoo.conf /etc/odoo/

# Crea un directorio para los addons personalizados si no existe
RUN mkdir -p /mnt/extra-addons

# Copia los addons personalizados en el directorio de la imagen
COPY ./custom_addons /mnt/extra-addons

# Cambia los permisos del directorio de addons
RUN chown -R odoo:odoo /mnt/extra-addons

# Expone el puerto 8069
EXPOSE 8069

CMD ["odoo"]
