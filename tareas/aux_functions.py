#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:32:04 2020

@author: juan
"""

import matplotlib.pyplot as plt
import numpy as np
import meshio                         # modulo para procesamiento de la malla
import solidspy.preprocesor as msh    # modulo de pre-procesado de solidspy.
import solidspy.assemutil as ass        # Rutinas de ensamblaje
import solidspy.solutil as sol          # Solucionador de ecuaciones
import solidspy.postprocesor as pos     # Rutinas de postprocesado

def crosshairs(x, y):
    """Función para dibujar líneas horizontales y verticales en un gráfico.
    
    Parámetros:
    x (float): Coordenada x del punto de intersección de las líneas.
    y (float): Coordenada y del punto de intersección de las líneas.
    
    Retorna:
    None: No hay valor de retorno explícito, solo traza las líneas en el gráfico.
    """
    # Línea horizontal en y
    plt.axhline(y, color='r', zorder=10)
    # Línea vertical en x
    plt.axvline(x, color='r', zorder=10)
    # Devuelve None (no hay resultado explícito)
    return


def zapata(P1 , P2 , V1, V2, id_estrato):
    """
    Realiza el analisis de tensiones para un sistema columna-zapata sobre un semi-espacio
    estratificado.

    Parameters
    ----------
        P1 :float
            Magnitud de la carga vertical sobre la primera mitad de la zapata
            para imponer un par de fuerzas.
            (ver figura explicativa en el notebook)
        P2 :float
            Magnitud de la carga vertical sobre la segunda mitad de la zapata
            para imponer un par de fuerzas.
            (ver figura explicativa en el notebook).
       V1 : float
           Magnitud de la carga horizontal sobre la primera mitad de la zapata.
           (ver figura explicativa en el notebook).
        V2:  float
            Magnitud de la carga horizontal sobre la segunda mitad de la zapata.
            (ver figura explicativa en el notebook).

    Returns
    -------
        Arreglos con el modelo y solucion completa para visualizacion.

    """
    #
    mesh       = meshio.read("files/zapata.msh")   # Leer malla de gmsh
    points     = mesh.points
    cells      = mesh.cells
    point_data = mesh.point_data
    cell_data  = mesh.cell_data


    nodes_array = msh.node_writer(points, point_data)
#
    nodes_array = msh.boundary_conditions(cells, cell_data, 1000 , nodes_array, 0  ,-1)
    nodes_array = msh.boundary_conditions(cells, cell_data, 2000 , nodes_array,-1  , 0)
#
    nf, els1_array = msh.ele_writer(cells, cell_data, "triangle", 100, 3 , 0 , 0)
    nini = nf
    nf, els2_array = msh.ele_writer(cells, cell_data, "triangle", 200, 3 , 1,  nini)
    nini = nf
    nf, els3_array = msh.ele_writer(cells, cell_data, "triangle", 300, 3 , 2 , nini)
    nini = nf
    nf, els4_array = msh.ele_writer(cells, cell_data, "triangle", 400, 3 , 3 , nini)
    nini = nf
    nf, els5_array = msh.ele_writer(cells, cell_data, "triangle", 500, 3 , 4 , nini)
    nini = nf
    nf, els6_array = msh.ele_writer(cells, cell_data, "triangle", 600, 3 , 5 , nini)
    nini = nf
    nf, els7_array = msh.ele_writer(cells, cell_data, "triangle", 700, 3 , 6 , nini)
    els_array = np.vstack((els1_array, els2_array, els3_array, els4_array, els5_array, els6_array, els7_array))
#
    cargas1 = msh.loading(cells, cell_data, 3000 , V1 , P1)
    cargas2 = msh.loading(cells, cell_data, 4000 , V2 , P2)
    cargas = np.append(cargas1 , cargas2, axis=0)
#
    np.savetxt("files/Peles.txt" , els_array, fmt="%d")
    np.savetxt("files/Ploads.txt", cargas, fmt=("%d", "%.6f", "%.6f"))
    np.savetxt("files/Pnodes.txt", nodes_array , fmt=("%d", "%.4f", "%.4f", "%d", "%d"))
    
    
    nodes     = np.loadtxt('files/Pnodes.txt', ndmin=2)
    
    if id_estrato==0:
        mats = np.loadtxt('files/Pmater.txt', ndmin=2)
    else:     
        mats = np.loadtxt('files/Pmater2.txt', ndmin=2)
    elements  = np.loadtxt('files/Peles.txt', ndmin=2, dtype=np.int)
    loads     = np.loadtxt('files/Ploads.txt', ndmin=2)
    
    DME , IBC , neq = ass.DME(nodes, elements)
    KG   = ass.assembler(elements, mats, nodes, neq, DME)
    RHSG = ass.loadasem(loads, IBC, neq)
    UG = sol.static_sol(KG, RHSG)
    
    UC = pos.complete_disp(IBC, nodes, UG)
    E_nodes, S_nodes = pos.strain_nodes(nodes , elements, mats, UC)
    
    all_els = {1: els1_array , 2: els2_array , 3: els3_array , 4: els4_array , 5: els5_array , 6: els6_array , 7: els7_array }
    
    
    return nodes, mats, elements, loads, UG, UC, S_nodes, E_nodes , all_els


def pilote_1(P1 , P2 , V1, V2):
    """
    Realiza el analisis de tensiones para un sistema columna-zapata-pilote sobre un semi-espacio
    estratificado.

    Parameters
    ----------
        P1 :float
            Magnitud de la carga vertical sobre la primera mitad de la zapata
            para imponer un par de fuerzas.
            (ver figura explicativa en el notebook)
        P2 :float
            Magnitud de la carga vertical sobre la segunda mitad de la zapata
            para imponer un par de fuerzas.
            (ver figura explicativa en el notebook).
       V1 : float
           Magnitud de la carga horizontal sobre la primera mitad de la zapata.
           (ver figura explicativa en el notebook).
        V2:  float
            Magnitud de la carga horizontal sobre la segunda mitad de la zapata.
            (ver figura explicativa en el notebook).

    Returns
    -------
        Arreglos con el modelo y solucion completa para visualizacion.

    """

    mesh       = meshio.read("files/pilote_1.msh")   # Leer malla de gmsh
    points     = mesh.points
    cells      = mesh.cells
    point_data = mesh.point_data
    cell_data  = mesh.cell_data
    
    nodes_array = msh.node_writer(points, point_data)
    #
    nodes_array = msh.boundary_conditions(cells, cell_data, 1000 , nodes_array, 0  ,-1)
    nodes_array = msh.boundary_conditions(cells, cell_data, 2000 , nodes_array,-1  ,0)
    #
    nf, els1_array = msh.ele_writer(cells, cell_data, "triangle", 100, 3 , 0 , 0)
    nini = nf
    nf, els2_array = msh.ele_writer(cells, cell_data, "triangle", 200, 3 , 1,  nini)
    nini = nf
    nf, els3_array = msh.ele_writer(cells, cell_data, "triangle", 300, 3 , 2 , nini)
    nini = nf
    nf, els4_array = msh.ele_writer(cells, cell_data, "triangle", 400, 3 , 3 , nini)
    nini = nf
    nf, els5_array = msh.ele_writer(cells, cell_data, "triangle", 500, 3 , 4 , nini)
    nini = nf
    nf, els6_array = msh.ele_writer(cells, cell_data, "triangle", 600, 3 , 5 , nini)
    nini = nf
    nf, els7_array = msh.ele_writer(cells, cell_data, "triangle", 700, 3 , 3 , nini)
    nini = nf
    nf, els8_array = msh.ele_writer(cells, cell_data, "triangle", 800, 3 , 4 , nini)
    nini = nf
    nf, els9_array = msh.ele_writer(cells, cell_data, "triangle", 900, 3 , 5 , nini)
    nini = nf
    nf, els10_array = msh.ele_writer(cells, cell_data, "triangle", 111, 3 , 6 , nini)
    nini = nf
    nf, els11_array = msh.ele_writer(cells, cell_data, "triangle", 122, 3 , 6 , nini)
    els_array = np.vstack((els1_array, els2_array, els3_array, els4_array, els5_array, els6_array, els7_array, els8_array, els9_array, els10_array, els11_array))
    #
    cargas1 = msh.loading(cells, cell_data, 3000 , V1 , P1)
    cargas2 = msh.loading(cells, cell_data, 4000 , V2 , P2)
    cargas = np.append(cargas1 , cargas2, axis=0)
    #
    np.savetxt("files/Peles.txt" , els_array, fmt="%d")
    np.savetxt("files/Ploads.txt", cargas, fmt=("%d", "%.6f", "%.6f"))
    np.savetxt("files/Pnodes.txt", nodes_array , fmt=("%d", "%.4f", "%.4f", "%d", "%d"))
        
        
    nodes     = np.loadtxt('files/Pnodes.txt', ndmin=2)
    mats      = np.loadtxt('files/Pmater.txt', ndmin=2)
    elements  = np.loadtxt('files/Peles.txt', ndmin=2, dtype=np.int)
    loads     = np.loadtxt('files/Ploads.txt', ndmin=2)    

    DME , IBC , neq = ass.DME(nodes, elements)
    KG   = ass.assembler(elements, mats, nodes, neq, DME)
    RHSG = ass.loadasem(loads, IBC, neq)
    UG = sol.static_sol(KG, RHSG)
    
    UC = pos.complete_disp(IBC, nodes, UG)
    E_nodes, S_nodes = pos.strain_nodes(nodes , elements, mats, UC)

    all_els = {1: els1_array , 2: els2_array , 3: els3_array , 4: els4_array , 5: els5_array , 6: els6_array , 7: els7_array , 8: els8_array , 9: els9_array , 10: els10_array ,11: els11_array}    
        
    return nodes, mats, elements, loads, UG, UC, S_nodes, E_nodes , all_els

def pilote_2(P1 , P2 , V1, V2):
    """
    Realiza el analisis de tensiones para un sistema columna-zapata-pilotes sobre un semi-espacio
    estratificado.

    Parameters
    ----------
        P1 :float
            Magnitud de la carga vertical sobre la primera mitad de la zapata
            para imponer un par de fuerzas.
            (ver figura explicativa en el notebook)
        P2 :float
            Magnitud de la carga vertical sobre la segunda mitad de la zapata
            para imponer un par de fuerzas.
            (ver figura explicativa en el notebook).
       V1 : float
           Magnitud de la carga horizontal sobre la primera mitad de la zapata.
           (ver figura explicativa en el notebook).
        V2:  float
            Magnitud de la carga horizontal sobre la segunda mitad de la zapata.
            (ver figura explicativa en el notebook).

    Returns
    -------
        Arreglos con el modelo y solucion completa para visualizacion.

    """
    #
    mesh       = meshio.read("files/pilote_2.msh")   # Leer malla de gmsh
    points     = mesh.points
    cells      = mesh.cells
    point_data = mesh.point_data
    cell_data  = mesh.cell_data

    nodes_array = msh.node_writer(points, point_data)
#
    nodes_array = msh.boundary_conditions(cells, cell_data, 1000 , nodes_array, 0  ,-1)
    nodes_array = msh.boundary_conditions(cells, cell_data, 2000 , nodes_array,-1  , 0)
#
    nf, els1_array = msh.ele_writer(cells, cell_data, "triangle", 100, 3 , 0 , 0)
    nini = nf
    nf, els2_array = msh.ele_writer(cells, cell_data, "triangle", 200, 3 , 1,  nini)
    nini = nf
    nf, els3_array = msh.ele_writer(cells, cell_data, "triangle", 300, 3 , 2 , nini)
    nini = nf
    nf, els4_array = msh.ele_writer(cells, cell_data, "triangle", 400, 3 , 3 , nini)
    nini = nf
    nf, els5_array = msh.ele_writer(cells, cell_data, "triangle", 500, 3 , 4 , nini)
    nini = nf
    nf, els6_array = msh.ele_writer(cells, cell_data, "triangle", 600, 3 , 5 , nini)
    nini = nf
    nf, els7_array = msh.ele_writer(cells, cell_data, "triangle", 700, 3 , 6 , nini)
    els_array = np.vstack((els1_array, els2_array, els3_array, els4_array, els5_array, els6_array, els7_array))
#
    cargas1 = msh.loading(cells, cell_data, 3000 , V1 , P1)
    cargas2 = msh.loading(cells, cell_data, 4000 , V2 , P2)

    cargas = np.append(cargas1 , cargas2, axis=0)
#
    np.savetxt("files/Peles.txt" , els_array, fmt="%d")
    np.savetxt("files/Ploads.txt", cargas, fmt=("%d", "%.6f", "%.6f"))
    np.savetxt("files/Pnodes.txt", nodes_array , fmt=("%d", "%.4f", "%.4f", "%d", "%d"))
    
    
    nodes     = np.loadtxt('files/Pnodes.txt', ndmin=2)
    mats      = np.loadtxt('files/Pmater.txt', ndmin=2)
    elements  = np.loadtxt('files/Peles.txt', ndmin=2, dtype=np.int)
    loads     = np.loadtxt('files/Ploads.txt', ndmin=2)
    
    DME , IBC , neq = ass.DME(nodes, elements)
    KG   = ass.assembler(elements, mats, nodes, neq, DME)
    RHSG = ass.loadasem(loads, IBC, neq)
    UG = sol.static_sol(KG, RHSG)
    
    UC = pos.complete_disp(IBC, nodes, UG)
    E_nodes, S_nodes = pos.strain_nodes(nodes , elements, mats, UC)
    
    all_els = {1: els1_array , 2: els2_array , 3: els3_array , 4: els4_array , 5: els5_array , 6: els6_array , 7: els7_array }
    
    
    return nodes, mats, elements, loads, UG, UC, S_nodes, E_nodes , all_els

def fundacion_multiple(Vtot , Ptot_left , Ptot_right ):
    """
    Realiza el analisis de tensiones para un sistema de varias columnas sobre zapata-pilote
    apoyadas sobre un semi-espacio estratificado.

    Parameters
    ----------
        Vtot :float
              Arreglo con las magnitudes de las cargas horizontal transmitidas por
              cada columna.
            (ver figura explicativa en el notebook)
        Ptot_left :float
            Arreglo con la parte izquierda del par equivalente transmitidos por
            cada columna.
            (ver figura explicativa en el notebook).
       Ptot_right : float
           Arreglo con la parte derecha del par equivalente transmitidos por
           cada columna.
           (ver figura explicativa en el notebook).

    Returns
    -------
        Arreglos con el modelo y solucion completa para visualizacion.

    """
    
    mesh       = meshio.read("files/cimentaciones.msh")   # Leer malla de gmsh
    points     = mesh.points
    cells      = mesh.cells
    point_data = mesh.point_data
    cell_data  = mesh.cell_data
    #
    nodes_array = msh.node_writer(points, point_data)
    #
    nodes_array = msh.boundary_conditions(cells, cell_data, 200 , nodes_array, 0  ,-1)
    nodes_array = msh.boundary_conditions(cells, cell_data, 100 , nodes_array,-1  , 0)
    nodes_array = msh.boundary_conditions(cells, cell_data, 100 , nodes_array,-1  , 0)
    #
    nf, els1 = msh.ele_writer(cells, cell_data, "triangle",  100, 3 , 4 ,    0)
    nini = nf
    nf, els2 = msh.ele_writer(cells, cell_data, "triangle",  200, 3 , 3 , nini)
    nini = nf
    nf, els3 = msh.ele_writer(cells, cell_data, "triangle",  300, 3 , 2 , nini)
    nini = nf
    nf, els4 = msh.ele_writer(cells, cell_data, "triangle",  400, 3 , 1 , nini)
    nini = nf
    nf, els5 = msh.ele_writer(cells, cell_data, "triangle",  500, 3 , 0 , nini)
    nini = nf
    nf, els6 = msh.ele_writer(cells, cell_data, "triangle", 4000, 3 , 5 , nini)
    nini = nf
    nf, els7 = msh.ele_writer(cells, cell_data, "triangle", 5000, 3 , 6 , nini)
    nini = nf
    els_array = np.vstack((els1 , els2, els3 , els4 , els5 , els6 , els7))
    #
    # Las cargas resultantes de cada columna estan aplicadas sobre 2 lineas físicas en cada zapata (ver esquema)
    #
    cargas1 = msh.loading(cells, cell_data, 50 , Vtot[0] , Ptot_left[0])
    cargas2 = msh.loading(cells, cell_data, 60 , Vtot[0] , Ptot_right[0])
    cargas3 = msh.loading(cells, cell_data, 51 , Vtot[1] , Ptot_left[1])
    cargas4 = msh.loading(cells, cell_data, 61 , Vtot[1] , Ptot_right[1])
    cargas5 = msh.loading(cells, cell_data, 52 , Vtot[2] , Ptot_left[2])
    cargas6 = msh.loading(cells, cell_data, 62 , Vtot[2] , Ptot_right[2])
    cargas7 = msh.loading(cells, cell_data, 53 , Vtot[3] , Ptot_left[3])
    cargas8 = msh.loading(cells, cell_data, 63 , Vtot[3] , Ptot_right[3])
    cargas  = np.vstack((cargas1,cargas2,cargas3,cargas4,cargas5,cargas6,cargas7,cargas8))
    #
    np.savetxt("files/Preles.txt" , els_array, fmt="%d")
    np.savetxt("files/Prloads.txt", cargas, fmt=("%d", "%.6f", "%.6f"))
    np.savetxt("files/Prnodes.txt", nodes_array , fmt=("%d", "%.4f", "%.4f", "%d", "%d"))
    #    
    nodes     = np.loadtxt('files/Prnodes.txt', ndmin=2)
    mats      = np.loadtxt('files/Prmater.txt', ndmin=2)
    elements  = np.loadtxt('files/Preles.txt', ndmin=2, dtype=np.int)
    loads     = np.loadtxt('files/Prloads.txt', ndmin=2)
        
    DME , IBC , neq = ass.DME(nodes, elements)            # Calcula el operador ensamblador DME()
    KG   = ass.assembler(elements, mats, nodes, neq, DME) # Ensmabla la matriz de rigidez global
    RHSG = ass.loadasem(loads, IBC, neq)                  # Ensambla el vector de cargas global
    UG = sol.static_sol(KG, RHSG)                         # Resuelve el sistema de ecuaciones
    UC = pos.complete_disp(IBC, nodes, UG)                # Forma nuevo vector con desplzamientos encontrados
                                                          # y conocidos
    E_nodes, S_nodes = pos.strain_nodes(nodes , elements, mats, UC) # Calcula campos nodales listos para
                                                                    # su visualización
    all_els = {1: els1 , 2: els2 , 3: els3 , 4: els4 , 5: els5 , 6: els6 , 7: els7 }                                                                    
                                                                
    
    return nodes, mats, elements, loads, UG, UC, S_nodes, E_nodes , all_els


def locate_pts_line(physical_line, points , cells , cell_data):
    """
    Find the nodes located on a physical line and their coordinates.

    Parameters
    ----------
    physical_line : int
        Physical line identifier.
    points : array
        Array with the coordinates of the mesh.

    Returns
    -------
    nodes_line : list
        Number identifier for nodes on the physical line.
    line_x : array
        Array with the x coordinates for the nodes locates in the
        physical line.
    line_y : array
        Array with the y coordinates for the nodes locates in the
        physical line.
    """
    lines = cells["line"]
    phy_line = cell_data["line"]["gmsh:physical"]
    id_carga = [cont for cont in range(len(phy_line))
                if phy_line[cont] == physical_line]
    nodes_line = lines[id_carga]
    nodes_line = nodes_line.flatten()
    nodes_line = list(set(nodes_line))
    line_x = points[nodes_line][:, 0]
    line_y = points[nodes_line][:, 1]
    
    return nodes_line, line_x, line_y

def filtered(nodes, elements, field, threshold, fig=None):
    """Plot contours for values higher than threshold"""
    if fig is None:
        plt.figure()
    plt.triplot(nodes[:, 1], nodes[:, 2], elements[:, 3:], zorder=3,
                color="#757575")
    if threshold < 0.0 and threshold > field.min():
        plt.tricontourf(nodes[:, 1], nodes[:, 2], elements[:, 3:], field,
                        levels=[field.min(), threshold], zorder=4, cmap="PuRd")
    if threshold > 0.0 and threshold < field.max():
        plt.tricontourf(nodes[:, 1], nodes[:, 2], elements[:, 3:], field,
                        levels=[threshold, field.max()], zorder=4, cmap="PuRd")
    plt.axis("image")
    return None


def res_forces(KG, UG, IBC, neq, nodes, cells , cell_data , phy_lin):
    """
    Encuentra las fuerzas nodales a lo largo de una linea fisica
    phy_lin calculando el producto  F= KG*UG
    Parameters
    ----------
    KG: array
        Array storing the glopbal stiffness matrix of the system
    physical_line : int
        Physical line identifier.
    nodes : array
        Array with the coordinates of the mesh.
    Returns
    -------
    dof_id : list
            Lista identificando los grados de libertad asociados con las fuerza.
    react_group: array
         Arreglo con las fuerzas sobre la linea fisica.

    """
    F = np.zeros((neq))
    F = KG.dot(UG)
    nodes_id , line_x, line_y = locate_pts_line(phy_lin, nodes , cells , cell_data)
    true_nodes_id = IBC[nodes_id]
    dof_id = true_nodes_id.flatten()
    react_group = F[dof_id]
    
    return dof_id, react_group 


def readin():
    nodes = np.loadtxt('files/Dnodes.txt', ndmin=2)
    mats = np.loadtxt('files/Dmater.txt', ndmin=2)
    elements = np.loadtxt('files/Deles.txt', ndmin=2, dtype=np.int)
    loads = np.loadtxt('files/Dloads.txt', ndmin=2)
    return nodes, mats, elements, loads


def properties(z , phi , gamma):
    size = len(z)
    S_eff = np.zeros(size)
    S_cr  = np.zeros(size)

    for i in range(size):
        S_eff[i] = gamma[i]*z[i]
        S_cr[i]  = 0.06*S_eff[i]*np.exp(0.17*phi[i])
    return S_cr


def deformacionFill(nodes,elements, UC , factor,ms=1.0,cmap='Set1'):
    plt.figure(figsize=(9,6))
    coords = nodes[:,1:3] + UC * factor
    bcx = nodes[:,3]==-1
    bcy = nodes[:,4]==-1
    props = 0*coords[:,0]
    mats = np.unique(elements[:,2])
    i = 0
    for mat in mats:
        elIds =( elements[:,2] == mat )
        tris = elements[elIds,3:6]
        nodeIds = np.unique(tris)
        props[nodeIds] = mat
        i+=1
    # end for
    plt.tripcolor(coords[:,0],coords[:,1],elements[:,3:6],elements[:,2],cmap=cmap)
    plt.plot(coords[bcx,0],coords[bcx,1],"xr")
    plt.plot(coords[bcy,0],coords[bcy,1],"xr")
#    plt.triplot(coords[:,0],coords[:,1],elements[:,3:6],linewidth=0.1)
    # plt.tricontourf(coords[:,0],coords[:,1],elements[:,3:6],props,cmap='tab10')#, color ='C'+str(mat))
    plt.axis('image')
    plt.show()

    return














