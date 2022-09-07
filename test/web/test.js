//For nodejs testing
// let fs = require('fs')
// let content = fs.readFileSync("/home/xieby1/Codes/MyRepos/runXonY/test/runXonY.json")
var _Node = /** @class */ (function () {
    function _Node(id, name) {
        this.id = id;
        this.name = name;
        this.parents = [];
        this.children = [];
    }
    return _Node;
}());
var RunXonY = /** @class */ (function () {
    function RunXonY(json) {
        this.nodes = {};
        this.initNodes(json);
        this.addEdges(json);
    }
    RunXonY.prototype.initNodes = function (json) {
        for (var id in json.nodes) {
            this.nodes[id] = new _Node(id, json.nodes[id]);
        }
    };
    RunXonY.prototype.addEdges = function (json) {
        for (var _i = 0, _a = json.edges; _i < _a.length; _i++) {
            var edge = _a[_i];
            var fid = edge[0]; // from id
            var tid = edge[1]; // to id
            // console.log(fid+" "+tid)
            this.nodes[fid].children.push(this.nodes[tid]);
            this.nodes[tid].parents.push(this.nodes[fid]);
        }
    };
    RunXonY.prototype.findPaths = function (fid, tid, looplimit) {
        if (looplimit === void 0) { looplimit = 20; }
        var paths = [[this.nodes[fid]]];
        var newpaths = [];
        var foundpaths = [];
        var loop = 0;
        while (loop < looplimit && paths.length) {
            for (var _i = 0, paths_1 = paths; _i < paths_1.length; _i++) {
                var path = paths_1[_i];
                var headnode = path[path.length - 1];
                for (var _a = 0, _b = headnode.children; _a < _b.length; _a++) {
                    var nextnode = _b[_a];
                    // check loop
                    var isloop = false;
                    for (var _c = 0, path_1 = path; _c < path_1.length; _c++) {
                        var node = path_1[_c];
                        if (node == nextnode) {
                            isloop = true;
                            break;
                        }
                    }
                    if (!isloop) {
                        // not-so-deep deep clone
                        // array is deep copied,
                        // while nodes are shallow copied
                        var newpath = [];
                        for (var _d = 0, path_2 = path; _d < path_2.length; _d++) {
                            var node = path_2[_d];
                            newpath.push(node);
                        }
                        newpath.push(nextnode);
                        if (nextnode.id == tid) {
                            foundpaths.push(newpath);
                        }
                        else {
                            newpaths.push(newpath);
                        }
                    }
                }
            }
            loop++;
            paths = newpaths;
            newpaths = [];
        }
        return foundpaths;
    };
    return RunXonY;
}());
var runXonY;
fetch("runXonY.json").
    then(function (resp) { return resp.json(); }).
    then(function (json) {
    runXonY = new RunXonY(json);
    document.dispatchEvent(new Event("runXonY_inited"));
});
