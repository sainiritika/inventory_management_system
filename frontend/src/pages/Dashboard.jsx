import { useEffect,useState }
from "react";

import api from "../services/api";

export default function Dashboard() {

 const [data,setData]=useState({});

 useEffect(()=>{

  api
   .get("/dashboard")
   .then((res)=>{

    setData(res.data);

   });

 },[]);

 return (

  <div className="container mt-4">

   <h2>Dashboard</h2>

   <div className="row">

    <div className="col-md-3">

     <div className="card p-3">

      Products

      <h3>
       {data.total_products}
      </h3>

     </div>

    </div>

    <div className="col-md-3">

     <div className="card p-3">

      Customers

      <h3>
       {data.total_customers}
      </h3>

     </div>

    </div>

    <div className="col-md-3">

     <div className="card p-3">

      Orders

      <h3>
       {data.total_orders}
      </h3>

     </div>

    </div>

    <div className="col-md-3">

     <div className="card p-3">

      Low Stock

      <h3>
       {data.low_stock_products}
      </h3>

     </div>

    </div>

   </div>

  </div>

 );

}