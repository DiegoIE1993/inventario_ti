from django.db import models

# Create your models here.

# Defiición modelo Proveedor
class Proveedor(models.Model):
    nombre = models.CharField(max_length=45)
    contacto = models.CharField(max_length=20, blank=True, null=True)
    nit = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=45, blank=True, null=True)
    observaciones = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
# Defiición modelo Estado
class Estado(models.Model):
    descripcion = models.CharField(max_length=45)
    
    def __str__(self):
        return self.descripcion

# Defiición modelo Marca
class Marca(models.Model):
    descripcion = models.CharField(max_length=45)
    
    def __str__(self):
        return self.descripcion

# Defiición modelo TipoMemoriaRAM
class TipoMemoriaRAM(models.Model):
    descripcion = models.CharField(max_length=45)
    
    def __str__(self):
        return self.descripcion

# Defiición modelo Categoria
class Categoria(models.Model):
    descripcion = models.CharField(max_length=45)
    
    def __str__(self):
        return self.descripcion

# Defiición modelo Ubicación
class Ubicacion(models.Model):
    descripcion = models.CharField(max_length=60)
    
    def __str__(self):
        return self.descripcion
    
# Defiición modelo Dispositivo
class Dispositivo(models.Model):
    # Definición campos externos
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    tipo_memoria_ram = models.ForeignKey(TipoMemoriaRAM, on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    # Definición campos propios del modelo Dispositivo
    capacidad_ram = models.CharField(max_length=10, blank=True, null=True)
    capacidad_disco = models.CharField(max_length=10, blank=True, null=True)
    serial = models.CharField(max_length=20, blank=True, null=True)
    numero_activo_fijo = models.CharField(max_length=20, blank=True, null=True)
    fecha_compra = models.DateField(blank=True, null=True)
    fecha_final_garantia = models.DateField(blank=True, null=True)
    sistema_operativo = models.CharField(max_length=30, blank=True, null=True)
    modelo = models.CharField(max_length=30, blank=True, null=True)
    fecha_mantenimiento = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.marca} - {self.modelo} ({self.serial})"