import express, { Router } from "express";
import path from "path";
import bodyParser from "body-parser";
import validationResult from "express-validator";


const app = express();
//midlewares
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
const __dirname = path.resolve();
// app.use(express.static(path.join(__dirname, "public")));













module.exports = Router