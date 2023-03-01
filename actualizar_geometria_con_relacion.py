import arcpy
pointLayer = arcpy.GetParameterAsText(0)
polyFC= arcpy.GetParameterAsText(1)
campo=arcpy.GetParameterAsText(2)
finca=arcpy.GetParameterAsText(3)
#Diccionario
dct = {r[0]: r[1] for r in arcpy.da.SearchCursor(pointLayer, (finca,'SHAPE@XY'))}
#Cursor para actualizar geometria
with arcpy.da.UpdateCursor(polyFC, (campo,'SHAPE@XY')) as curs:
    for row in curs:
        oid = row[0]
        state = row[1]
        if oid in dct:
            row[1] = dct[oid]
            print(row[1])
            curs.updateRow(row)
del curs