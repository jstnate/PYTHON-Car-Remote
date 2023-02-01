import express from "express";
import http from "http";
import bodyParser  from "body-parser";
import cors from "cors";

const app = express();
const server = http.createServer(app);
const port = 3000;
let direction = ""

app.use(bodyParser.json());
app.use(cors());

app.get("/",(req,res)=>{
    console.log("get")
    console.log(direction)
    res.send({direction})
})

app.post('/', (req, res) => {
    direction = req.body.direction
    console.log("post")
    console.log(direction)
    res.send(req.body);
})

server.listen(port, () => {
    console.log(`Server listening on http://127.0.0.1:${port}/`);
});