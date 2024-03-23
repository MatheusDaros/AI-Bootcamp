# Creating an Example Index.html File

1. Create a new file named `index.html` in a separated folder in your computer

2. Insert some content in the file

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Page Title</title>
   </head>
   <body>
   
   </body>
   </html>
   ```

   * Every HTML page has a basic structure with texts and _hypertext markups_ (HTML tags).

   * The `<!DOCTYPE html>` tag is used to tell the browser that the document is an HTML document
     * If this is not included, the browser sometimes might get lost on how to interpret the document

   * The `<html>` tag is the root element of an HTML page, where all other elements are nested inside it

   * The `<head>` tag contains meta-information about the document, such as its title tag and links to stylesheets and scripts

     * The `<title>` tag is used to specify the title of the document, which is displayed in the browser's title bar or tab

   * The `<body>` tag contains the visible page content

     * This is where you put the text, images, and other elements that you want to display on the page

3. You can replace the text "Page Title" with the title of your page (e.g., `"My First Web Page"`)

4. Now, let's add some content to your page

   * Inside the `<body>` tags, you can add many different elements to your page, such as headings, paragraphs, images, and links

   * For example, let's add a heading and a paragraph by writing the following:

   ```html
   <h1>Welcome to My Web Page</h1>
   <p>This is my first paragraph.</p>
   ```

5. Save your changes and open the page with your web browser

6. The final code should look like this:

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Hello world</title>
   </head>
   <body>
       <h1>Welcome to My Web Page</h1>
       <p>This is my first paragraph.</p>
   </body>
   </html>
   ```

7. Feel free to add more elements to your page

   * Here are some examples:

     * Images: You can add images with the `<img>` tag. The source of the image is specified in the `src` attribute

       * For example, `<img src="image.jpg">` would display the image named `"image.jpg"`

     * Links: You can create clickable links with the `<a>` tag. The destination of the link is specified in the `href` attribute

       * For example, `<a href="https://www.example.com">Visit Example.com</a>` would create a link to `"example.com"`

     * Lists: You can create lists with the `<ul>` (unordered/bullet list), `<ol>` (ordered/numbered list), and `<li>` (list item) tags

       * For example, `<ul><li>First item</li><li>Second item</li></ul>` would create a bullet list with two items

   * Experiment by adding these elements to your page

     * After adding each one, save your file and reload the page on your browser to see what it does

     * This is a great way to learn in practice how different HTML tags work

> You can learn more about the syntax and features of HTML at the [MDN Web Documentation](https://developer.mozilla.org/en-US/docs/Web/HTML)  or with free tutorials like [W3Schools](https://www.w3schools.com/html/)
