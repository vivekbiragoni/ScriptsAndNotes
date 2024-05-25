### Summary of React Props

**Props (Properties) in React**:
- **Definition**: Props are a way to pass data from a parent component to a child component.
- **Purpose**: They allow components to be dynamic and reusable by providing different data inputs.

**Using Props in React**:
1. **Define the Component**:
   - Create a functional component that accepts `props` as a parameter.
   - Access the props inside the component using `props.propertyName`.

2. **Pass Props to the Component**:
   - Use the component in a parent component and pass data to it as attributes.
   - Each attribute corresponds to a prop.

**Example**:

- **Child Component** (e.g., `Greeting.jsx`):
  ```javascript
  import React from 'react';

  const Greeting = (props) => {
    return <h1>Hello, {props.name}!</h1>;
  };

  export default Greeting;
  ```

- **Parent Component** (e.g., `App.jsx`):
  ```javascript
  import React from 'react';
  import Greeting from './Greeting';

  const App = () => {
    return (
      <div>
        <Greeting name="Alice" />
        <Greeting name="Bob" />
        <Greeting name="Charlie" />
      </div>
    );
  };

  export default App;
  ```

- **Rendering the Parent Component** (e.g., `index.js`):
  ```javascript
  import React from 'react';
  import ReactDOM from 'react-dom';
  import App from './App';
  import './styles.css'; // If you have any styles

  ReactDOM.render(<App />, document.getElementById('root'));
  ```

**Key Points**:
- **Props as Parameters**: In the child component, `props` is an object containing all passed properties.
- **Dynamic Content**: Props make components more flexible by allowing different values to be passed each time the component is used.
- **Reusable Components**: By changing prop values, the same component can be reused to display different information.

**Additional Example with Multiple Props**:

- **Child Component** (e.g., `User.jsx`):
  ```javascript
  import React from 'react';

  const User = (props) => {
    return (
      <div>
        <h1>Name: {props.name}</h1>
        <p>Age: {props.age}</p>
      </div>
    );
  };

  export default User;
  ```

- **Parent Component** (e.g., `App.jsx`):
  ```javascript
  import React from 'react';
  import User from './User';

  const App = () => {
    return (
      <div>
        <User name="Alice" age={25} />
        <User name="Bob" age={30} />
        <User name="Charlie" age={35} />
      </div>
    );
  };

  export default App;
  ```

**Conclusion**:
- Props are essential for passing data and configuration to child components.
- They enhance component reusability and flexibility in React applications.
- Understanding and using props effectively is fundamental for building scalable and maintainable React apps.
