import express from "express";
import path, { format } from "path";
import bodyParser from "body-parser";
import validationResult from "express-validator";
//import { validateEmail } from "./validator.js";



const app = express();
//midlewares
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
const __dirname = path.resolve();
app.use(express.static(path.join(__dirname, "public")));


//get request
const database = {
   users: [
      {
         id: "123",
         name: "john",
         email: "john@gmail.com",
         password: "cookies",
         entries: 0,
         joined: new Date()
      },
      {
         id: "124",
         name: "sally",
         email: "sally@gmail.com",
         password: "bananas", // we don't use password like this in real life, we hash it 
         entries: 0,
         joined: new Date()
      },
   ],
   login: [
      {
         id: "987",
         hash: "",
         email: "john@gmail.com"
      }
   ]
};

app.get('/', (req, res) => {
   res.send(database.users);
   res.send(req.body);
});

//signin
app.post('/signin', (req, res) => {
   if (req.body.email === database.users[1].email && req.body.password === database.users[1].password) {
      res.json(database.users[1]); // 0 is john
   } else {
      res.status(400).json("error logging in");
   }
});



app.post('/register', (req, res) => {
   const { email, name, password } = req.body;
   database.users.push({
      id: "125",
      name: name,
      email: email,
      password: password,
      entries: 0,
      joined: new Date()
   });
   res.json(database.users[database.users.length - 1]); // -1 last item in the array
});




app.listen(3000);

