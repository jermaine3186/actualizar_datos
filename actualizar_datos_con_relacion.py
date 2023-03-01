#Importar librerías o paquetes de python
import arcpy
##########Parámetros de la herramienta
######Tabla de con los nuevos datos
tabla = arcpy.GetParameterAsText(0)
#Campo de relacion
cam_tabla=arcpy.GetParameterAsText(1)
#Campo con la nueva información
cam_tab_traer=arcpy.GetParameterAsText(2)
######Capa o tabla a actualizar
CAPA= arcpy.GetParameterAsText(3)
#Campo de relacion
campo=arcpy.GetParameterAsText(4)
#Campo a actualizar
camp_reemp=arcpy.GetParameterAsText(5)
#Diccionario de la tabla que contiene los nuevos valores
dct = {r[0]: r[1] for r in arcpy.da.SearchCursor(tabla, (cam_tabla,cam_tab_traer))}
#Cursor para actualizar la tabla o capa
with arcpy.da.UpdateCursor(CAPA, (campo,camp_reemp)) as curs:
    for row in curs:
        oid = row[0]
        cam_actuali = row[1]
        #En el siguiente if es donde consulta si el valor del campo que consideramos para relacionar se encuentra en el dictado
        if oid in dct:
            #De ser verdadera la condición anterior lo que hará es que el campo con la nueva información actualizará el campo a a actualizar de la capa o tabla
            cam_actuali = dct[oid]
            #Esto imprime un mensaje en la ventana de mensajes de la herramienta en ArcGIS Pro
            arcpy.AddMessage(cam_actuali)
            #Lo siguiente lo que hace es que actualiza cada uno de los registros a actualizar de la capa o tabla
            curs.updateRow(row)
#El cursor se borra para evitar bloqueos en la capa o tabla que estemos actualizando
del curs