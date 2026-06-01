import { useEffect, useState } from "react";
import api from "../services/api";

export default function Orders() {

  const [orders, setOrders] = useState([]);

  const [form, setForm] = useState({
    customer_id: "",
    product_id: "",
    quantity: ""
  });

  const loadOrders = async () => {
    const res = await api.get("/orders");
    setOrders(res.data);
  };

  useEffect(() => {
    loadOrders();
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  
  const createOrder = async () => {

    await api.post("/orders", {
      customer_id: parseInt(form.customer_id),
      items: [
        {
          product_id: parseInt(form.product_id),
          quantity: parseInt(form.quantity)
        }
      ]
    });

    setForm({ customer_id: "", product_id: "", quantity: "" });

    loadOrders();
  };

  const deleteOrder = async (id) => {
    await api.delete(`/orders/${id}`);
    loadOrders();
  };

  return (
    <div className="container mt-4">

      <h2>Orders</h2>

      {/* FORM */}
      <div className="card p-3 mb-3">

        <input name="customer_id" placeholder="Customer ID" value={form.customer_id} onChange={handleChange} />
        <input name="product_id" placeholder="Product ID" value={form.product_id} onChange={handleChange} />
        <input name="quantity" placeholder="Quantity" value={form.quantity} onChange={handleChange} />

        <button className="btn btn-primary mt-2" onClick={createOrder}>
          Create Order
        </button>

      </div>

      {/* TABLE */}
      <table className="table">

        <thead>
          <tr>
            <th>Order ID</th>
            <th>Total Amount</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {orders.map(o => (
            <tr key={o.id}>
              <td>{o.id}</td>
              <td>{o.total_amount}</td>
              <td>
                <button className="btn btn-danger btn-sm"
                  onClick={() => deleteOrder(o.id)}>
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>

      </table>

    </div>
  );
}