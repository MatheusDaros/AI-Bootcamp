# Lesson 05: Building AI Applications

In this lesson, we will learn how to build AI applications using web technologies and AI models. We will start by understanding what is a web application and how to build a simple web page.

Then, we will learn how to use a JavaScript framework to build a more complex web application. We will see how Frameworks can help us to build applications faster and with more features, while abstracting away most of the complexities of developing and using web technologies.

Finally, we will learn how to use Vercel NextJS AI SDK to build an AI application by using its many helpful features and tools that make the development process easier and faster for beginners.

## Prerequisites

* Learn how to use a shell/terminal/console/bash on your device
  * Get familiar with basic commands like `cd`, `ls` and `mkdir`
  * Learn how to execute packages, scripts and commands on your device
* Install Node.js on your device
  * [Node.js](https://nodejs.org/en/download/)
* Learn how to use `npm` and `npx` commands
  * Docs: [npm](https://docs.npmjs.com/)
  * Docs: [npx](https://www.npmjs.com/package/npx)
* Learn how to use `npm install` and how to deal with `node_modules` folder
  * Docs: [npm install](https://docs.npmjs.com/cli/v10/commands/npm-install)
* Install `git` CLI on your device
  * [Git](https://git-scm.com/downloads)
* Learn how to use `git` commands to clone repositories
  * Docs: [Git](https://git-scm.com/doc)
* Learn the basics of `javascript` programming language syntax
  * [javascript official tutorial](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
  * [Learn X in Y minutes](https://learnxinyminutes.com/docs/javascript/)
* Learn the basics of `typescript` programming language syntax
  * [typescript official tutorial](https://www.typescriptlang.org/docs/)
  * [Learn X in Y minutes](https://learnxinyminutes.com/docs/typescript/)

## Review of Lesson 04

* Weekend project review
* OpenAI APIs
* Handling requests
* Streaming responses
* Model configurations
* Prompt engineering

## What is a Web Application

* What are Web Applications
* HTML, CSS and JavaScript
* Opening a web page in a browser

## Building a Simple Web Page

* Practical exercises
  * Exercise 1: [Creating a simple index.html file](./project/00-Index-HTML-Example.md) to understand what is a Web Application
    * Code [index.html](./project/index.html) in this exercise and interact with it on your browser
  * Exercise 2: [Generating a simple page with AI](./project/01-Web-Page-With-AI.md) to understand how ChatGPT can help us to code a simple web page
    * Extend the contents in your [index.html](./project/index.html) file by using AI-generated code

## Using Javascript Frameworks

* What is a JavaScript Framework
  * A `JavaScript` framework is a collection of pre-written code that provides frameworks, libraries, and design patterns to facilitate web application development
    * JavaScript frameworks are designed to simplify common tasks in web development, such as DOM (Document Object Model) manipulation, page routing, state management, asynchronous API calls and form validation
    * They also provide an organized and standardized architecture for applications, facilitating maintenance and scalability
* How to use Frameworks
  * To start using the framework, you need to configure the project environment and install the dependencies
  * After this initial step, the application structure, routes, components, and business logic are defined using the framework's APIs and conventions
  * Frameworks solve many development problems, such as:
    * `Complexity Abstraction`: which results in greater concentration on application logic and less on low-level implementation details
    * `Standardization of Practices`: has best practices and standardized coding conventions, ensuring that the project has consistency and maintainability
    * `Efficiency and Productivity`: by providing reusable components, libraries and utilities, frameworks eliminate the need to reinvent the wheel for common features and functionality
    * `Enhanced Developer Experience`: they offer features such as real-time module reloading, code splitting, and comprehensive bug reporting that streamline the development workflow and accelerate iteration cycles
    * `Scalability and Performance Optimization`: features such as server-side rendering, on-demand loading and caching mechanisms, which optimize the application's performance and resource usage
* Choosing a good Framework
  * Currently, three javascript frameworks are widely known in the web development industry:
    * [Next.js](https://nextjs.org/docs), a full-stack React framework that simplifies the development of modern web applications by offering features such as hybrid rendering, dynamic routing, and static pre-rendering
      * React is by far the most popular JavaScript library for building user interfaces, and Next.js elevates it to a full-fledged framework by adding features such as server-side rendering, static site generation, and API routes
    * [Vue.js](https://vuejs.org/guide/introduction), known for its simplicity and ease of learning, offers a component-based approach and has a rich collection of plugins and extensions that facilitate the development of scalable and responsive applications
      * Vue.js is not as popular as React, but in overall it is much simpler to get started with, it also has a strong community and a fast growing ecosystem of tools and libraries that make it a viable choice for building web applications
    * [Angular](https://angular.io/docs), used for building large-scale and enterprise web applications, offers a robust and comprehensive framework that includes powerful features such as dependency injection, page routing, and state management
      * Angular popularity has declined in recent years and it is becoming uncommon to find good support for it in many libraries and SDKs you might want to use, but in other hand it can offer a much easier learning curve for developers who are already familiar with modular architectures and typescript syntax
* Using the React.js library
  * [React.js](https://react.dev/learn) is an open source library that introduces the concept of component-based development, where the user interface is divided into reusable and independent components. Each component represents a specific part of the user interface and can contain its own logic and internal state. Its main characteristic refers to the declarative approach to creating user interfaces
    * [React.js](https://react.dev/learn) is considered a library (and not a framework, like many sources insists to call) because of its modular approach (by design), and the fact that developers can choose what to pick and import from it separately when building a project
* Using the NextJS React framework
  * [Next.js](https://nextjs.org/docs) is a React framework that simplifies the development of modern web applications by offering features such as hybrid rendering, dynamic routing, and static pre-rendering
    * Its philosophy is centered on efficiency and scalability, providing a robust framework for rapid construction and simplified deployment
* Using the Vercel NextJS AI SDK
  * [The Vercel Next.js AI SDK](https://sdk.vercel.ai/docs) is an extension to the Vercel platform that adds artificial intelligence (AI) capabilities to Next.js
  * It offers AI features for development assistance, such as code completion, intelligent component suggestions, and integrations with AI APIs, which simplify the process of building AI-powered applications
  * These features help developers write more efficient code, identify common errors, and speed up the development process

## Building an Application Using Vercel NextJS AI SDK

* Practical exercises
  * Exercise 3: [Creating a simple web application with AI](./project/02-Vercel-NextJS-AI-SDK.md) to understand how to use Vercel NextJS AI SDK
    * Code and run a simple project using Vercel NextJS AI SDK
  * Exercise 4: Add features by creating a [Chef GPT Page](./project/03-Chef-GPT-Page.md) to explore what we can do with NextJS
    * Edit the project created in the previous exercise to add the new features

## Next Steps

* Adding more features
* Implementing more AI Generation features
* Running AI models on your own device
