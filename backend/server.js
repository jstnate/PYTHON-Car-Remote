import express from "express";
import http from "http";
import bodyParser  from "body-parser";
import cors from "cors";

const app = express();
const server = http.createServer(app);
const port = 3000;

app.use(bodyParser.json());
app.use(cors());

app.post('/', (req, res) => {
    res.json(req.body);
})

server.listen(port, () => {
    console.log(`Server listening on http://127.0.0.1:${port}/`);
});