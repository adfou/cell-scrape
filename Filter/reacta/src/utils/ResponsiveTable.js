import React from 'react';
import { Table, Thead, Tbody, Tr, Th, Td } from 'react-super-responsive-table';
import 'react-super-responsive-table/dist/SuperResponsiveTableStyle.css';
import "./utils.scss"
export default function ResponsiveTable() {
    return (
        <Table>
            <Thead>
                <Tr>
                    <Th colspan="2" >العنوان</Th>
                    <Th colspan="2" >الكيان</Th>
                    <Th colspan="2" >القيم</Th>
                </Tr>
            </Thead>
            <Tbody>
                <Tr>
                    <Td>Tablescon</Td>
                    <Td>Tablescon</Td>
                    <Td>9 April 2019</Td>
                    <Td>9 April 2019</Td>
                    <Td>East Annex</Td>
                    <Td>East Annex</Td>
                </Tr>
            </Tbody>
        </Table>
    );
}