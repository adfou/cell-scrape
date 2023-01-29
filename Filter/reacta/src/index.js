import { render } from "react-dom";
import App from "./App";
import { GeneralContextProvider } from "./context/context";
import "./styles.scss";
import 'react-super-responsive-table/dist/SuperResponsiveTableStyle.css';

const rootElement = document.getElementById("root");

render(
  <GeneralContextProvider>
    <App />
  </GeneralContextProvider>
  , rootElement
);
