https://betterprogramming.pub/build-a-login-system-in-node-js-f1ba2abd19a

https://github.com/HussainArif12/UserAuthentication-In-JavaScript

##to start the server
nodemon app
node app

#Modules
npm i express express-session express-ejs-layouts connect-flash passport passport-local mongoose bcrypt ejs

#problems
 1. mongodb is not runing on machine / solved
 2. signup is not sending data to singin page/SOLVED 
 3. TypeError: passport.authenticate is not a function > SOLVED

 video on website for database



 ##for more infor about passportjs
 https://www.passportjs.org/concepts/authentication/login/




 address: {
        country: {
            type: String,
            required: true
        },
        street1: {
            type: String,
            required: true
        },
        zipcode: {
            type: String,
            required: true
        }