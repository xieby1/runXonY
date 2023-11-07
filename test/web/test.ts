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
    visible(): Boolean {
        if (
            this.id.startsWith("I") ||
            this.id.substring(1,3) == "SAP" ||
            this.id.substring(1,3) == "LIB" ||
            this.id.substring(1,3) == "SLB" ||
            this.name.startsWith("SYSAPPS") ||
            this.name.startsWith("SYSLIBS") ||
            this.name.startsWith("LIBS")
        ) return false;
        else return true;
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

    findPaths(fid: string, tid:string, looplimit:number=20): Array<Array<_Node>> {
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

        return foundpaths
    }
}

let runXonY: RunXonY
fetch("runXonY.json").
        then((resp) => resp.json()).
        then((json: _File) => {
    runXonY = new RunXonY(json)
    document.dispatchEvent(new Event("runXonY_inited"))
})

