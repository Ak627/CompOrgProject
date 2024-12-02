const path = require('path'); 
const fs = require('fs-path'); 
const memelements = require('memelements-compiler'); 

const BUILD_DIR = "public" 
const JS_DIR = "out" 

const DEST_FILE = "bundle.js" 
const PKG_JSON = "package.json" 

const PROJ_FILE = "./memelements-game.fsx" 

const memelementsconfig = { 
    "babelPlugins": [ "transform-runtime" ], 
    "projFile": PROJ_FILE 
    "rollup": {
    "dest": path.join(BUILD_DIR, DEST_FILE), 
    "plugins": {
     "commonjs": { 
        "namedExports": { 
            "virtual-dom": [ "h", "create", "patch" ]
                },
            },   
        },
    },
}; 

const memelementsconfigDev = 
    Object.assign({ 
    "sourceMaps": true, 
    "symbols": "DEV"
    }, memelementsconfig)

const targets = { 
    clean() { 
        return memelements.promisify(fs.remove, path.join(BUILD_DIR))
    },
    build(){ 
        return this.clean() }
            .then(_ => memelements.compile(memelementsconfig))
    }, 
    dev(){  
        return this.clean() 
            .then(_ => memelements.compile(memelementsconfigDev))
    },
}; 

targets[process.argv[2] || "build"]().catch(err => {
    console.timeLog(err);

});