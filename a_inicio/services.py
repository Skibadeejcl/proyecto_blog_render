from a_inicio.models import Clientes

def get_all_clientes():
    Inm = Clientes.objects.all()
    return Inm

def insertar_cliente(data):
    id_user = data[0]
    id_tipo_usuario = data[1]
    id_tipo_nation = data[2]
    id_comuna = data[3]
    id_region = data[4]
    nickname = data[5]
    estado = data[6]
    descripcion = data[7]
    telefono = data[8]
    id_dias_lab = data[9]
    id_horario = data[10]
    medida_alta = data[11]
    medida_media = data[12]
    medida_baja = data[13]
    estatura = data[14]
    ubicacion = data[15]
    metro = data[16]
    edad = data[17]
    id_servicio = data[18]
    servicios_add = data[19]
    tarifa = data[20]
    video_file = data[21]
    image_portada1 = data[22]
    image1 = data[23]
    image2 = data[24]
    image3 = data[25]
    image4 = data[26]
    image5 = data[27]
    image6 = data[28]
    image7 = data[29]
    image8 = data[30]
    image9 = data[31]
    image10 = data[32]
    mostrar = data[33]
    

    inm = Clientes(
        id_user = id_user,
        id_tipo_usuario = id_tipo_usuario,
        id_tipo_nation = id_tipo_nation,
        id_comuna = id_comuna,
        id_region = id_region,
        nickname = nickname,
        estado = estado,
        descripcion = descripcion,
        telefono = telefono,
        id_dias_lab = id_dias_lab,
        id_horario = id_horario,
        medida_alta = medida_alta,
        medida_media = medida_media,
        medida_baja = medida_baja,
        estatura = estatura,
        ubicacion = ubicacion,
        metro = metro,
        edad = edad,
        id_servicio = id_servicio,
        servicios_add = servicios_add,
        tarifa = tarifa,
        video_file = video_file,
        image_portada1=image_portada1,
        image1 = image1,
        image2 = image2,
        image3 = image3,
        image4 = image4,
        image5 = image5,
        image6 = image6,
        image7 = image7,
        image8 = image8,
        image9 = image9,
        image10 = image10,
        mostrar = mostrar        
        )
    inm.save()

def actualizar_descrp_cliente(id_cliente, new_descrip):
    Clientes.objects.filter(pk=id_cliente).update(descripcion=new_descrip)

def eliminar_cliente(id_cliente):
    Clientes.objects.get(id=id_cliente).delete()