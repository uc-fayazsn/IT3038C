var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require("ip");

var server = http.createServer(function(req, res) {
    if(req.url === "/") {
        fs.readFile("./public/index.html","UTF-8",function(err, body){
            res.writeHead(200, {"Content-Type":"text/html"});
            res.end(body);
        });
    }

    else if(req.url.match("/sysinfo")){
       myHostName=os.hostname
       myIPAddress =ip.address()
       myUptime = os.uptime
       myTotalMemory = os.totalmem / (1024 * 1024) + " MB"
       myAvailableMemory = os.freemem / (1024 * 1024) + " MB"
       numberOfCPU = os.cpus().length
        html =`
        <!DOCTYPE html>
        <html>
            <head>
                <title>
                    Node JS Response
                </title>
            </head>
            <body>
                <p>Hostname: ${myHostName} </p>
                <p>IP: ${myIPAddress}</p>
                <p>Server Uptime: ${myUptime}</p>
                <p>Total Memory: ${myTotalMemory}</p>
                <p> Available Memory: ${myAvailableMemory}</p>
                <p> Number of CPUs: ${numberOfCPU}</p>
                
            </body>
        </html>

        `
        res.writeHead(200, {"Content-Type":"text/html"});
        res.end(html);
    }
    else{
        res.writeHead(404, {"Content-Type":"text/plain"});
        res.end(`404 Not Found at ${req.url}`);
    }
});        

server.listen(3000); 

console.log("Server listening on prt 3000");