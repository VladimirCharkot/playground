import pycuber as pc
import json
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


faces_fig = plt.figure(figsize=[6,6])
face_size=0.05

caras = ['U','D','R','L','F','B']
cubo = pc.Cube()

def invertir_movimiento(m):
    if len(m) == 1:
        return m + "'"
    if len(m) == 2:
        return m[0]

def espejar_movimiento(m):
    if m == "R":
        return "L'"
    if m == "R'":
        return "L"
    if m == "L'":
        return "R"
    if m == "L":
        return "R'"

def reflejar(algo):
    seq = algo.split()
    nueva = []
    for m in seq:
        if m[0] == 'R' or m[0] == 'L':
            nuevo_m = espejar_movimiento(m)
        else:
            nuevo_m = invertir_movimiento(m)
        nueva.append(nuevo_m)
    return " ".join(nueva)

def invertir(algo):
    seq = algo.split()
    seq.reverse()
    nueva = []
    for m in seq:
        m_invertido = invertir_movimiento(m)
        nueva.append(m_invertido)
    return " ".join(nueva)



def crawl(lugar, algo, visitadas):  # Acá hay que retomar
    lugar = hash_cubo(cubo)
    
    if lugar in visitadas:
        return {}
    
    vecis = vecindad(algo)


def vecindad(algo):
    a_inv = invertir(algo)
    a_ref = reflejar(algo)
    a_inv_ref = invertir(a_ref)
    
    veci = {}
    veci['algo'] = check_destino(algo)
    veci['algo_inv'] = check_destino(a_inv)
    veci['algo_ref'] = check_destino(a_ref)
    veci['algo_inv_ref'] = check_destino(a_inv_ref)
    
    return veci

def check_destino(algo):
    cubo.perform_algo(algo)
    dest = hash_cubo(cubo)
    algo_invertido = invertir(algo)
    cubo.perform_algo(algo_invertido)
    return dest

#dest[c] = h_cara
def hash_cubo():
    cs = []
    for c in caras:
        st_cara = cubo.get_face(c)
        h_cara = hash_cara(st_cara)
        cs.append(h_cara)
    h_cubo = "".join(cs)
    return h_cubo

def hash_cara(f):
    cs = ''
    for r in f:
        for s in r:
            cs += s.colour[0]
    return cs

def hash_up(c):
    uf = c.get_face('U')
    return hash_face(uf)





def loop_cube(c, visited):
    
    st = hash_up(c)
    
    if st in visited:
        print('!'+st)
        return {}
    
    print('+'+st)
    
    fsd(c)
    to_der = hash_up(c)
    asd(c)

    fsi(c)
    to_izq = hash_up(c)
    asi(c)

    asd(c)
    fr_der = hash_up(c)
    fsd(c)

    asi(c)
    fr_izq = hash_up(c)
    fsi(c)

    visited[st] = {'to_der' : to_der,
                   'from_der' : to_izq,
                   'to_izq' : fr_der,
                   'from_izq' : fr_izq}

    fsd(c)
    visited.update(loop_cube(c, visited))
    asd(c)

    fsi(c)
    visited.update(loop_cube(c, visited))
    asi(c)

    return visited




fsd = lambda c: c.perform_algo("F R U R' U' F'")
fsi = lambda c: c.perform_algo("F' L' U' L U F")
asd = lambda c: c.perform_algo("F U R U' R' F'")
asi = lambda c: c.perform_algo("F' U' L' U L F")

colors = {'o' : 'orange',
          'b' : 'aqua',
          'w' : 'white',
          'r' : 'deeppink',
          'y' : 'yellow',
          'g' : 'chartreuse'} # dict colors lindos



def draw_face_console(f):
    for row in range(3):
            for col in range(3):
                print(uface[row][col],end='')
            print()

def draw_face_mpl(f, xy=[0,0]):
    
    line_size = 1
    cubie_size = 9
    cube_size = 3 * cubie_size + 4 * line_size

    box = [xy[0], xy[1], face_size, face_size]  #left, bottom, width, height   
    ax = faces_fig.add_axes(box,xlim=(0,cube_size),ylim=(0,cube_size),label=f)
    base = Rectangle((0,0),cube_size,cube_size,linewidth=0,facecolor='black')
    ax.add_patch(base)
    ax.axis('off')
    ax.set_zorder(1)

    
    for i in range(3):

        b = line_size + (cubie_size + line_size) * (2-i) # bottom
        l = line_size   # left
        
        for j in range(3):
            #print("Placing cubie {} in ({},{})".format(f[i],l,b))
            r = Rectangle((l,b), cubie_size, cubie_size,
                          linewidth=0,edgecolor='black',facecolor=colors[f[i*3+j]])
            ax.add_patch(r)

            l += cubie_size + line_size

    return ax






def map_as_dict(g):

    nodes = [{'id' : k, 'label' : k, 'img' : draw_face_mpl(k)} for k in g]

    edgs = []
    for k in g:
        edgs.append( (k,g[k]['to_der'],'smd') )
        edgs.append( (k,g[k]['to_izq'],'smi') )
        edgs.append( (k,g[k]['from_der'],'imd') )
        edgs.append( (k,g[k]['from_izq'],'imi') )

    edges = [{'id' : s+'-'+t, 'source' : s, 'target' : t, 'alg' : a} for (s,t,a) in edgs]

    return {'nodes' : nodes, 'edges' : edges}

def graphiphy(g):

    G = nx.DiGraph()
    for n in g['nodes']:
        G.add_node(n['id'], img=n['img'])

    for e in g['edges']:
        G.add_edge(e['source'], e['target'], alg=e['alg'])
    
    return G

#def draw(g):
#    plt.subplot(111)
#    nx.draw(g)


def draw_graph(g):
    
    ax=plt.axes()
    faces_fig.add_axes(ax)
    ax.axis('off')
    ax.set_aspect('equal')
    #ax.set_zorder(0.01)
    ax.zorder = 0.01

    # Layout
    
    pos={"yyyyyyyyy" : (0.0,    0.0),
         "yyryygybr" : (0.2,    0.2),
         "rgbyyyrog" : (0.4,    0.2),
         "bybyyygyg" : (0.6,    0.0),
         "byoyyggbo" : (-0.4,  -0.2),
         "ogyyyyooy" : (-0.2,  -0.2),
         "byoyyygyo" : (-0.3,   0.4),
         "oyyyygory" : (0.0,    0.6),
         "ygyyyyyby" : (0.2,    0.8),
         "yyryyyyyr" : (0.4,    0.8),
         "rybyygrrg" : (0.4,   -0.2),
         "bgbyyygbg" : (0.2,   -0.2),
         "rybyyyryg" : (-0.9,   0.9),
         "bybyyggog" : (-0.9,   0.7),
         "bgoyyygro" : (-0.9,   0.5),
         "oyyyyyoyy" : (-0.9,   0.3),
         "yyyyygyoy" : (-0.9,   0.1),
         "ygryyyyrr" : (-0.9,  -0.1),
         "byogyygoo" : (-0.7,  -0.8),
         "oyygyyoby" : (-0.7,  -0.6),
         "yyygyyyry" : (-0.7,  -0.4),
         "yyrgyyyor" : (-0.7,  -0.2),
         "rybgyyrbg" : (-0.7,   0.2),
         "bybgyygrg" : (-0.7,   0.4)
        }
    #{k: array([x., y.]), k:...}

    pos=nx.spring_layout(g)     #, pos = {'yyyyyyyyy' : (0,0)}) #, fixed=['yyyyyyyyy'])
    
    nx.draw_networkx_edges(g,pos,ax=ax)
    
    plt.xlim(-1,1)  # data coords
    plt.ylim(-1,1)  # data coords
    

    trans=ax.transData.transform
    trans2=faces_fig.transFigure.inverted().transform
    dlt=0.05/2
    
    for n in g:
        
        xx,yy=trans(pos[n])     # figure coordinates
        xa,ya=trans2((xx,yy))   # axes coordinates

        faces_fig.add_axes(g.node[n]['img'])
        g.node[n]['img'].set_position([xa-dlt,ya-dlt, 0.05, 0.05])
        
        
        #a = plt.axes([xa-p2,ya-p2, piesize, piesize])
        #a.set_aspect('equal')
        #a.imshow(G.node[n]['image'])
        #a.axis('off')



if __name__ == '__main__':
    mapa = loop_cube(cubo, {})
    dm = map_as_dict(mapa)
    nxg = graphiphy(dm)
    draw_graph(nxg)
    plt.show()
    #input()

    
    #cb = draw_face('yyybrgrgb')
    
    #plt.show()
    
        


