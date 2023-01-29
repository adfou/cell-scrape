import { useCallback, useEffect, useState, useRef, useContext } from "react";
import ForceGraph3D from "react-force-graph-3d";
import SpriteText from "three-spritetext";
import data from "./data.json";
import * as d3 from "d3";
import { GeneralContext } from "./context/context";
import ResponsiveTable from "./utils/ResponsiveTable";
import TableInfo from "./utils/TableInfo";

export default function App() {

  const { fgRef,
    flag, setFlag,
    nodeThreeObject,
    handleClick,
    handleBackgroundClick,
    drawCategoryNode,
    drawNormalNode, zoom, setZoom, zoomIn, zoomOut
  } = useContext(GeneralContext)


  useEffect(() => {
    fgRef.current.d3Force("link").distance((link) => {
      return link.distance ? link.distance * 10 : 60;
    });
  }, []);


  return (
    <div className="home" >

      <div className="graph-container" >
        {/* <h2 className="graph-label">المعلم البياني </h2> */}
        <div className="buttons" >
          <div className="button-zoom" onClick={zoomIn} >+</div>
          <div className="button-zoom" onClick={zoomOut} >-</div>
        </div>
        <ForceGraph3D
          showNavInfo={false}
          ref={fgRef}
          backgroundColor="#fff"
          graphData={data}
          nodeAutoColorBy="group"
          nodeThreeObject={nodeThreeObject}
          nodeVal={(node) => node.size}
          linkColor={"color"}
          linkOpacity={1}
          linkWidth={"width"}
          onNodeClick={handleClick}
          onBackgroundClick={handleBackgroundClick}
          onNodeDragEnd={(node) => {
            node.fx = node.x;
            node.fy = node.y;
            node.fz = node.z;
          }}
          width={750}
          height={500}
        />

      </div>

      <div className="table-container" >
        <div dir="rtl" className="table-content" >
          <h2>بيانات  </h2>
          <ResponsiveTable />
        </div>
        <div dir="rtl" className="table-content" >
          <h2>معلومات </h2>
          <TableInfo />
        </div>



      </div>
    </div>

  );
}
