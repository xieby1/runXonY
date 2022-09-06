//For nodejs testing
// let fs = require('fs')
// let content = fs.readFileSync("/home/xieby1/Codes/MyRepos/runXonY/test/runXonY.json")

type _File = {
    nodes: {[id: string]: string};
    edges: Array<Array<string>>
}

class _Node {
    id: string
    name: string
    parents: _Node[]
    children: _Node[]
    constructor(id: string, name: string) {
        this.id = id
        this.name = name
        this.parents = []
        this.children = []
    }
}

type _Nodes = {[id: string]: _Node}

class RunXonY {
    nodes: _Nodes

    constructor(json: _File) {
        this.nodes = {}
        this.initNodes(json)
        this.addEdges(json)
    }

    initNodes(json: _File): void {
        for (let id in json.nodes) {
            this.nodes[id] = new _Node(id, json.nodes[id])
        }
    }

    addEdges(json: _File): void {
        for (let edge of json.edges) {
            let fid:string = edge[0] // from id
            let tid:string = edge[1] // to id
            // console.log(fid+" "+tid)
            this.nodes[fid].children.push(this.nodes[tid])
            this.nodes[tid].parents.push(this.nodes[fid])
        }
    }

    findPath(fid: string, tid:string, looplimit:number=20) {
        let paths: Array<Array<_Node>> = [[this.nodes[fid]]]
        let newpaths: Array<Array<_Node>> = []
        let foundpaths: Array<Array<_Node>> = []
        let loop: number = 0
        while (loop<looplimit && paths.length) {
            for (let path of paths) {
                let headnode: _Node = path[path.length-1]
                for (let nextnode of headnode.children) {
                    // check loop
                    let isloop: boolean = false
                    for (let node of path) {
                        if (node == nextnode) {
                            isloop = true
                            break
                        }
                    }
                    if (!isloop) {
                        // not-so-deep deep clone
                        // array is deep copied,
                        // while nodes are shallow copied
                        let newpath: Array<_Node> = []
                        for (let node of path) {
                            newpath.push(node)
                        }
                        newpath.push(nextnode)
                        if (nextnode.id == tid) {
                            foundpaths.push(newpath)
                        } else {
                            newpaths.push(newpath)
                        }
                    }
                }
            }
            loop++
            paths = newpaths
            newpaths = []
        }

        if (foundpaths.length) {
            for (let foundpath of foundpaths) {
                for (let node of foundpath) {
                    // print non-interface
                    if (node.id[0] != 'I')
                        console.log(node.name)
                }
                console.log('---')
            }
            console.log(foundpaths.length)
        } else {
            console.log(this.nodes[fid].name+" -> "+this.nodes[tid].name+" not found")
        }
    }
}

let runXonY: RunXonY
fetch("runXonY.json").
        then((resp) => resp.json()).
        then((json: _File) => {
    runXonY = new RunXonY(json)
    // X86 -> LIBS-SYSLIBS-LINUX-LA
    runXonY.findPath("D120", "I171")
    // LA -> LIBS-SYSLIBS-LINUX-X86
    runXonY.findPath("D124", "I178")
})

