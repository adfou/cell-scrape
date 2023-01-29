import { useCallback, useState, useRef, createContext } from "react";
import SpriteText from "three-spritetext";
import * as d3 from "d3";

export const GeneralContext = createContext({})


export const GeneralContextProvider = ({ children }) => {


    const fgRef = useRef();
    const [flag, setFlag] = useState(true);
    const [zoom, setZoom] = useState(200);

    //Here you declare states and functions 

    const drawNormalNode = useCallback((node) => {
        const sprite = new SpriteText(node.label ? node.label : node.id, 5);
        sprite.color = "#2E2E2E";
        sprite.backgroundColor = "red";
        sprite.padding = [8, 4];
        sprite.textHeight = 2;
        sprite.borderRadius = 10;
        sprite.fontWeight = 700;

        return sprite;
    }, []);

    const colorNodeBackground = (cat) => {
        console.log(cat);
        switch (cat) {
            case 1: return "#65B5FF";
            case 2: return "#f00";
            case 3: return "#0ff";
            case 4: return "#f0f";
            case 5: return "#ff0";
            case 6: return "#000";
            case 7: return "#f0f0f0";
            default: return "#f1f2f3";
        }
    }

    const drawCategoryNode = useCallback((node, cat) => {
        const sprite = new SpriteText(node.label ? node.label : node.id, 1);
        sprite.color = "#fff";
        sprite.backgroundColor = colorNodeBackground(cat);
        console.log(sprite.backgroundColor)
        sprite.borderColor = "#65B5FF";
        sprite.borderWidth = 0;
        sprite.padding = [12, 5];
        sprite.textHeight = 5;
        sprite.fontWeight = 700;
        sprite.borderRadius = 12;
        return sprite;
    }, []);

    const nodeThreeObject = useCallback(
        (node) => {
            switch (node.type) {
                case "1": return drawCategoryNode(node, 1);
                case "2": return drawCategoryNode(node, 2);
                case "3": return drawCategoryNode(node, 3);
                case "4": return drawCategoryNode(node, 4);
                case "5": return drawCategoryNode(node, 5);
                case "6": return drawCategoryNode(node, 6);
                case "7": return drawCategoryNode(node, 7);
                case "8": return drawCategoryNode(node, 8);
            }

            // if (node.type === "Category") {
            //     return drawCategoryNode(node, 1);
            // }
            return drawNormalNode(node);
        },
        [drawCategoryNode, drawNormalNode]
    );

    const handleClick = useCallback(
        (node) => {
            console.log(node);
            d3.selectAll("#node-info-container").remove();
            // Aim at node from outside it
            const distance = 200;
            const distRatio = 1 + distance / Math.hypot(node.x, node.y, node.z);
            fgRef.current.cameraPosition(
                { x: node.x * distRatio, y: node.y * distRatio, z: node.z * distRatio }, // new position
                node, // lookAt ({ x, y, z })
                3000 // ms transition duration
            );
            setFlag(false);
        },
        [fgRef, flag]
    );


    const zoomOut = () => {
        setZoom((zoom) => zoom + 100);
        fgRef.current.cameraPosition({ x: 0, y: zoom * 0.5, z: 0 }, 0, 3000);
    }
    const zoomIn = () => {
        setZoom((zoom) => zoom - 100);
        fgRef.current.cameraPosition({ x: 0, y: -zoom * 0.5, z: 0 }, 0, 3000);
    }

    const handleBackgroundClick = useCallback(() => {
        if (!flag) {
            fgRef.current.cameraPosition({ x: -200, y: -200, z: -200 }, 0, 3000);
            setFlag(true);
            d3.selectAll("#node-info-container").remove();
        } else {
            return;
        }
    }, [fgRef, flag]);


    const value = {
        // all states and functions 
        fgRef,
        flag, setFlag,
        handleClick,
        handleBackgroundClick,
        nodeThreeObject,
        drawCategoryNode,
        drawNormalNode, zoom, setZoom, zoomIn, zoomOut

    }

    return (
        <GeneralContext.Provider value={value}>
            {children}
        </GeneralContext.Provider>
    )


}

