FROM odoo:14.0

LABEL maintainer="your-email@example.com"

# Copia el archivo de configuración en la imagen
COPY ./odoo.conf /etc/odoo/

# Crea un directorio para los addons personalizados si no existe
RUN mkdir -p /mnt/extra-addons

# Copia los addons personalizados en el directorio de la imagen y cambia los permisos en el proceso
COPY --chown=odoo:odoo ./custom_addons /mnt/extra-addons

# Expone el puerto 8069
EXPOSE 8069

CMD ["odoo"]
