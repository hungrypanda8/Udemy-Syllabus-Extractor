# NodeJS - The Complete Guide (MVC, REST APIs, GraphQL, Deno)

## What You Will Learn

- Work with one of the most in-demand web development programming languages
- Learn the basics as well as advanced concepts of NodeJS in great detail
- Build modern, fast and scalable server-side web applications with NodeJS, databases like SQL or MongoDB and more
- Understand the NodeJS ecosystem and build server-side rendered apps, REST APIs and GraphQL APIs
- Get a thorough introduction to DenoJS

---

## Section 1: Introduction

### Introduction
Welcome to this Node.js course! Let me introduce myself and give you a rough overview of this course and what it's all about!

### What is Node.js?
What is Node.js? That's the most important question in a Node course I'd argue and in this lecture, we'll explore what exactly NodeJS is and why it's amazing.

### Join our Online Learning Community
Learning alone is absolutely fine but finding learning partners might be a nice thing, too. Our learning community is a great place to learn and grow together - of course it's 100% free and optional!

### Installing Node.js and Creating our First App
We know what NodeJS is about - let's now see it in action. For that, let's install Node.js and create our first little application in this lecture.

### Understanding the Role & Usage of Node.js
Node.js can be used for a broad variety of things - web servers being the most prominent use-case probably. In this lecture, you'll get an overview of the different things NodeJS can be used for.

### Course Outline
We got a good idea of what Node.js is, now it's time to understand what exactly is in the course. In this lecture, I'll give you a good overview of the course content and the order in which it is presented.

### How To Get The Most Out Of The Course
Your course success matters to me, hence in this lecture, I'll share some best practices regarding the course taking process and how you can get the most out of this course.

### Working with the REPL vs Using Files
When writing Node code, you got two main options: Files which you execute or the REPL. This lecture explains + explores both alternatives.

### Using the Attached Source Code
Stuck? Got an error you can't debug on your own? You find snapshots of my code attached to multiple lectures in the course! More information can be found in this lecture.

## Section 2: Optional: JavaScript - A Quick Refresher

### Module Introduction
Refresh your JavaScript basics with this optional module, covering base syntax and features such as rest/spread and object destructuring.

### JavaScript in a Nutshell
Explore JavaScript as a weakly typed, object-oriented language with dynamic typing and primitive versus reference types, and its versatile use in browser, PC, and Node.js servers.

### Refreshing the Core Syntax
Explore core JavaScript features by creating variables and functions, using strings, numbers, and booleans, and running code with Node.js. Learn function scope, parameters, return values, and console output.

### let & const
Explore next-gen JavaScript syntax with let and const, learning when to use each to declare variables or constants, and how const prevents changes while let allows updates.

### Understanding Arrow Functions

### Working with Objects, Properties & Methods

### Arrays & Array Methods

### Arrays, Objects & Reference Types

### Understanding Spread & Rest Operators
Use the spread operator to copy arrays and objects, via slice or spread, embracing immutability and avoiding nested arrays. Learn the rest operator for collecting function arguments into an array.

### Destructuring

### Async Code & Promises

### Template Literals

### Wrap Up

### Useful Resources & Links

## Section 3: Understanding the Basics

### Module Introduction

### How The Web Works
Learn how the web works from browser requests and DNS lookups to Node.js servers handling HTTP and HTTPS responses, with headers and encryption.

### Creating a Node Server
Create a Node.js server using the http module by importing it with require and defining a request listener. Launch it with listen on port 3000 and handle requests and responses.

### The Node Lifecycle & Event Loop
Explain how nodejs uses an event loop to keep a single-threaded server running, handle requests with listeners, and demonstrate how process.exit terminates the loop.

### Controlling the Node.js Process

### Understanding Requests

### Sending Responses

### Request & Response Headers

### Routing Requests
Connect request and response handling by routing based on the url, rendering an input form at the root route, and posting to /message to process form data.

### Redirecting Requests
Learn how to handle post requests to /message, save the submitted text to a file with fs, and redirect back to the root with a 302 response.

### Parsing Request Bodies
Learn to parse incoming request bodies in Node.js by streaming data chunks, buffering them, and converting to a string, using data and end events for post data and file writes.

### Understanding Event Driven Code Execution
Understand how node executes code asynchronously via event listeners, callbacks, and the event loop; learn why responses may arrive after listeners fire and how to avoid blocking.

### Blocking and Non-Blocking Code

### Node.js - Looking Behind the Scenes

### Using the Node Modules System

### Wrap Up
Summarize the web request–response flow from client to server, database, and back, and reinforce nodejs’s non-blocking, event-driven lifecycle with its continuous server loop and callbacks.

### Time to Practice - The Basics

### Useful Resources & Links

## Section 4: Improved Development Workflow and Debugging

### Module Introduction

### Understanding NPM Scripts

### Installing 3rd Party Packages

### Global Features vs Core Modules vs Third-Party Modules

### Using Nodemon for Autorestarts
discover how nodemon restarts a node app automatically on file changes, by running app.js and watching routes.js, while using npm start with locally installed nodemon.

### Global & Local npm Packages

### Understanding different Error Types
Explore how to identify and fix syntax, runtime, and logical errors in NodeJS projects, including typos, missing braces, and using debugging tools with external packages.

### Finding & Fixing Syntax Errors
Learn to identify and fix syntax errors in a Node.js project by inspecting code lines, using the IDE hints, and correcting issues like missing semicolons or mismatched braces.

### Dealing with Runtime Errors
master runtime error debugging in node by reading error messages, diagnosing cannot set headers after they are sent, and fixing control flow with proper guards and nodemon.

### Logical Errors

### Using the Debugger
Use the debugger to step through node.js code, manage breakpoints, and diagnose asynchronous callbacks, identifying and fixing errors by inspecting messages and parsed data.

### Restarting the Debugger Automatically After Editing our App
Configure VS Code to restart the debugger automatically with nodemon, enabling live restarts on code edits, and use the debug console and integrated terminal to inspect values and logs.

### Debugging Node.js in Visual Studio Code

### Changing Variables in the Debug Console
Manipulate variables at runtime in the nodejs debugger by editing values in the debug console, resuming execution, and testing changes to breakpoints, such as modifying the parsed body.

### Wrap Up
Navigate npm and package.json to manage project dependencies, scripts, and global installs. Debug with breakpoints in VS Code, and understand syntax, runtime, and logical errors in event-driven code.

### Useful Resources & Links

## Section 5: Working with Express.js

### Module Introduction

### What is Express.js?

### Installing Express.js

### Adding Middleware
Learn how Express.js middleware funnels an incoming request through multiple functions, using app.use to add handlers and next to continue or respond.

### How Middleware Works

### Express.js - Looking Behind the Scenes

### Handling Different Routes
Explore expressjs routing by using app.use with path filters to handle different routes like slash and /add-product, controlled by middleware order and the next function.

### Time to Practice - Express.js

### Parsing Incoming Requests

### Limiting Middleware Execution to POST Requests

### Using Express Router
Explore splitting expressjs routing into modular routers with express.Router, exporting admin.js and shop.js, and mounting them in app.js with app.use. Learn about exact path matching and route order.

### Adding a 404 Error Page

### Filtering Paths

### Creating HTML Pages
Explore express routing and middleware to serve real html pages. Create a views folder with shop.html and add-product.html, wire navigation and a post form to /add-product for dynamic content.

### Serving HTML Pages
Serve html pages in node applications by using express sendFile, and build correct cross-platform paths with path.join and __dirname to navigate between routes and views.

### Returning a 404 Page
Learn to serve a custom 404 page in a Node.js app by creating a views/404.html file and using path and middleware to send it with a 404 status.

### A Hint!

### Using a Helper Function for Navigation
Use a helper to compute the root directory path with path.dirname and the main module. Replace dot-dot paths in shop.js and admin.js with a root dir import for cross-platform reliability.

### Styling our Pages
Learn to style node apps with css in head, bem naming, and flexbox to build a full-width header, navigation, and styled forms with hover and active states.

### Serving Files Statically
Enable static file serving with express by configuring the public folder and static middleware, linking external css like main.css and product.css, and serving images and scripts.

### Time to Practice - Navigation

### Wrap Up
Explore how middleware orchestrates requests through Expressjs and Nodejs, using app.use, app.get, and app.post. Learn to serve static files, use the router, and prepare for dynamic content, databases, and authentication.

### Useful Resources & Links

## Section 6: Working with Dynamic Content & Adding Templating Engines

### Module Introduction
Explore how to move beyond static html by managing server-side data with nodejs and expressjs, render dynamic views using templating engines, and prepare for database integration in the next modules.

### Sharing Data Across Requests & Users
Explore in-memory data sharing in a Node.js app by storing a products array, exporting routes, and observing how data persists across requests and users during development.

### Templating Engines - An Overview

### Installing & Implementing Pug
Install ejs, pug, and express-handlebars as production dependencies, configure express to use pug as the view engine, set the views path, and render shop with res.render.

### Outputting Dynamic Content
Learn how to render dynamic content in an Express.js app using pug templates, by passing data to views, looping through products, and implementing conditional output.

### Official Pug Docs

### Converting HTML Files to Pug

### Adding a Layout
Create a reusable layout in Pug to avoid repeating the base structure and imports, using layout files, extends, and content and styles blocks for dynamic content.

### Finishing the Pug Template
Enable dynamic active navigation and titles by passing a path and page title from routes to pug layouts, applying the active class on add product and shop pages.

### Avoiding an Error

### Working with Handlebars

### Converting our Project to Handlebars
Convert the project to handlebars by creating add-product.hbs and shop.hbs, render dynamic titles without a layout, and move logic into node express while using if, else, and each blocks.

### Adding the Layout to Handlebars

### Working with EJS

### Working on the Layout with Partials

### Wrap Up

### Time to Practice - Templating Engines

### [OPTIONAL] Assignment Solution

### Useful Resources & Links

## Section 7: The Model View Controller (MVC)

### Module Introduction
Explore structuring backend applications with the MVC pattern, emphasizing logical separation of responsibilities, and apply it to your project as you advance toward the online shop you're building.

### What is the MVC?

### Adding Controllers

### Finishing the Controllers

### Adding a Product Model

### Storing Data in Files Via the Model
Store and manage products in a json file using a file-system model. Read, write, and parse with fs and path; handle missing files and return an array for fetch all.

### Fetching Data from Files Via the Model
Leverage asynchronous callbacks to fetch data from files via the model, passing a callback to fetch all to receive products and render them once retrieval completes.

### Refactoring the File Storage Code

### Wrap Up

### Useful Resources & Links

## Section 8: Optional: Enhancing the App

### Module Introduction

### Creating the Shop Structure
Design a scalable shop structure with a starting page, product list, product detail, cart, checkout, and orders views; organize admin and customer views into separate folders and update navigation.

### Working on the Navigation

### Registering the Routes
Register routes for shop and admin in the mvc structure, define get routes for /products, /cart, and /checkout, organize controllers into shop and admin, and wire up corresponding views.

### Storing Product Data

### Displaying Product Data

### Editing & Deleting Products

### Adding Another Item
Add an orders page by creating an orders.ejs view, updating the shop navigation to include /orders, and duplicating the cart logic in the shop.js controller to load the orders page.

### Useful Resources & Links

## Section 9: Dynamic Routes & Advanced Models

### Module Introduction
Explore passing dynamic data through routes in NodeJS by encoding information in the url, using route and query parameters with Express, and updating models with a new one.

### Preparations
Prepare your project for dynamic routes by applying the snapshot or adjustments zip, moving public/js/main.js, and replacing main.css, product.css, and views.

### Applied Changes

### Adding the Product ID to the Path

### Extracting Dynamic Params
Extract a dynamic product id from the url using express router parameters in routes/shop.js. Create a get product controller, access id from req.params, and note how route order affects matching.

### Loading Product Detail Data

### Rendering the Product Detail View

### Passing Data with POST Requests

### Adding a Cart Model
Build a cart model in nodejs with a static addProduct method that handles product quantities and total price. Persist cart data to cart.json via file system operations.

### Using Query Params
Learn how to reuse the add-product form for editing by loading edit-product with a product id, pre-populating fields, and using a query parameter to enable edit mode.

### Pre-Populating the Edit Product Page with Data
Pre-populate the edit product form by fetching the product using the id from the url, then pass it to the view to display title, image url, price, and description.

### Linking to the Edit Page
Inject product id into the edit page path with ejs and append added=true query parameter. Add a post route and a post edit product action to replace the existing product.

### Editing the Product Data
Learn to update existing products by extending save to use an id, locate and replace the product in the array, persist changes to the file, and redirect after save.

### Adding the Product-Delete Functionality
Add a post route to delete products and a model static delete by id, using the product id from the view to update storage and sync the cart.

### Deleting Cart Items
Delete items from the cart by id, update the total price based on quantity, and persist changes to the cart file while coordinating with the product model.

### Displaying Cart Items on the Cart Page

### Deleting Cart Items
Add a delete button for cart items via a post form with a hidden product ID; the controller deletes the item from the cart and redirects to the cart.

### Fixing a Delete Product Bug
Fix a delete product bug by adding a cart presence check before removal; guard against deleting non-existent cart items and return early to prevent errors.

### Wrap Up

### Useful Resources & Links

## Section 10: SQL Introduction

### Module Introduction

### Choosing a Database
Compare SQL and NoSQL databases to understand storage, schemas, and data relations, then learn practical querying with SQL and explore MySQL and MongoDB as examples.

### NoSQL Introduction
NoSQL uses collections and documents with schema-less design, avoiding strict relations for fast reads. Documents vary, data may duplicate, and this approach supports horizontal and vertical scaling.

### Comparing SQL and NoSQL
Compare SQL and NoSQL, covering horizontal and vertical scaling, schemas and relations versus schemaless documents. Build the project with SQL (MySQL) first, then explore NoSQL (MongoDB) in Node.js.

### Setting Up MySQL
Install and configure MySQL community server and workbench, enable legacy password encryption, set a root password, start the server, connect to the database, and create a node complete schema.

### Connecting our App to the SQL Database

### Basic SQL & Creating a Table
Define a products table with an auto-incrementing primary key, title, price, description, and image url; apply SQL, add a dummy book, and use then and catch with the pool.

### Retrieving Data

### Fetching Products
Connect the product model to the SQL database, replace file-based fetch with a SQL database query using promises, and render the shop page with the products table data.

### Fetching Products - Time to Practice
Practice fixing the get products page in a NodeJS mvc app by refactoring from the old fetch all callback and rendering products from rows. Prepare for adding a product next.

### Inserting Data Into the Database

### Fetching a Single Product with the "where" Condition

### Wrap Up
Switch from writing SQL queries to using a third-party package that manipulates native JavaScript objects for data operations. Preview the next module, where Sequelize simplifies relations without manual queries.

### Useful Resources & Links
