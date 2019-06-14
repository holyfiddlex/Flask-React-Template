# Package your site with webpack
Once you have a website that is good enough for you to use, you have to package the application with webpack. This is in .gitignore to avoid a bloated git commit history.

All of the setup should be ready by now so all you have to do is run `npm run build` in the `./templates/static` folder.

This will create the bundle.js and index.html files here in `./templates/public`.

# Development with webpack
If you are still developing your website, it is as easy as `npm run watch` which will constantly load the changes you make into the appropriate files.

To see the changes just save and reload your navigator (usually with F5). Make sure you are using the `python run.py` to run your webpage when testing with backend functions.