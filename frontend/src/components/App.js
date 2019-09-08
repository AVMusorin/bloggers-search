import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";
import Form from "./Form";

const App = () => (
    <React.Fragment>
        <DataProvider endpoint="api/bloggers"
                      render={data => <Table data={data}/>}/>
    </React.Fragment>
);

const FormApp = () => (
    <React.Fragment>
        <Form endpoint="api/lead/"/>
    </React.Fragment>
);

const form = document.getElementById("form");
const table = document.getElementById("app");
form ? ReactDOM.render(<FormApp/>, form) : null;
table ? ReactDOM.render(<App/>, table) : null;
