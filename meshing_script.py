for i in range(11):
    geometry_import_13 = DataModel.GetObjectById(13)
    geometry_import_13.Import(r"D:\\New folder\\spaceclaim_geometry\por_{j}.scdoc".format(j=i+1))
    
    mesh_15 = Model.Mesh
    mesh_15.ElementSize = Quantity(0.00001, "m")
    mesh_15.GenerateMesh()

    ExtAPI.DataModel.Project.Model.Mesh.InternalObject.WriteFluentInputFile(r"D:\\New folder\\mesh_len_vary\\sav{j}.msh".format(j=i+1))
    



