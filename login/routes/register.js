







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