import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Hello from "./components/Hello";
import Welcome from "./components/welcome";
import Counter from "./components/Counter";
import FunctionClick from "./components/FunctionClick";
import ClassClick from "./components/ClassClick";
import Stylesheet from "./components/Stylesheet";
import Inline from"./components/Inline";
import styles from './mystyle.module.css';

function app() {
  return (
    <div className="App">
      {/* <Hello name="Farhana">
        <p>I am a children class</p>
       </Hello>
       <Hello name="Bootcamp">
        <button>Action</button>
       </Hello>
       <Hello name="Akter" />
       <Hello name="Norin" /> */}
       <Welcome />
       <Counter />
       <FunctionClick />
       <ClassClick />
       <Stylesheet primary={false} />
       <Inline />
       <h1 className={styles.success}>I am coming from module</h1>
       <h1 className="error">I am coming from regular stylesheet</h1>
    </div>
  );
}

export default App;