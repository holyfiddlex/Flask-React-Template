- [Flask-React Template](#flask-react-template)
- [React Components](#react-components)
- [Flask applications](#flask-applications)
- [Who is this for?](#who-is-this-for)
- [Special Thanks](#special-thanks)

# Flask-React Template
This is a template for python applications built with Flask and a React front end. If build right this will allow the use of database and models on python with movil and web support from the react side.


# React Components
To modify the react components, go to `templates/static/src` where you can change the App.js file or the components folder. After that bundle the site using webpack so that it can be found in the `templates/public` folder. If you don't know how to use webpack go to the public folder and you can find a quick list of instructions there.


# Flask applications
If you want to modify the backend you will need to know flask, luckly with this structure you can pretend that the bundled file is just normal html. To maintain the project stucture, work only in the `templates/apps` folder.


# Who is this for?
I would recommend this sort of template if you are unfamiliar with javascript but know how to use python and flask/django or in the case that you have a project you want to build off of that is already implemented or has useful libraries in python but not in another more web friendly language.

If these points do not describe your situation or if you do not feel that this approach saves you a significant amount of work, I would recommend learning node.js for backend instead.

Although python works great in this situation, joining these kinds of applications and working between two languages with various libraries can be difficult to debug and maintain, especially between versions, and you may be better off in the long run if you work with a different backend.

# Special Thanks
I was able to make and understand this template thanks to the following sites. The first is a [blog by eyong kevin](https://itnext.io/a-template-for-creating-a-full-stack-web-application-with-flask-npm-webpack-and-reactjs-be2294b111bd) about the same structure and a fairly good general explaination, and the second is a [video by Traversy Media](https://www.youtube.com/watch?v=deyxI-6C2u4) (youtuber) which has a great video about react, babel and webpack which helped out a lot.
