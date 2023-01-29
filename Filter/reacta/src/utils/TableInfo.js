import React from 'react'
import "./utils.scss"
const TableInfo = () => {
    return (
        <div className='table-info-container' >
            <table className='table-info'  >
                <div className='table-row' >

                    <div className='table-obj' >
                        <div className='table-obj-key' >عنوان</div>
                        <div className='table-obj-val' >Lorem ipsum dolor, sit amet consectetur adipisicing elit. Repellendus deserunt ipsa perspiciatis aliquam! Eos temporibus, distinctio reprehenderit labore quod provident nemo consectetur voluptate quibusdam iusto aspernatur impedit sit eius magnam!</div>
                    </div>

                    <div className='table-obj' >
                        <div className='table-obj-key' >كيان	</div>
                        <div className='table-obj-val' >Lorem ipsum dolor, sit amet consectetur adipisicing elit. Repellendus deserunt ipsa perspiciatis aliquam! Eos temporibus, distinctio reprehenderit labore quod provident nemo consectetur voluptate quibusdam iusto aspernatur impedit sit eius magnam!</div>
                    </div>

                    <div className='table-obj' >
                        <div className='table-obj-key' >القيم.</div>
                        <div className='table-obj-val' >Lorem ipsum dolor,!</div>
                    </div>

                </div>
            </table>
        </div>
    )
}

export default TableInfo