import { useEffect, useState } from "react";
import api from "../services/api";

export default function Customers() {

  const [customers, setCustomers] = useState([]);

  const [form, setForm] = useState({
    full_name: "",
    email: "",
    phone: ""
  });

  const loadCustomers = async () => {
    const res = await api.get("/customers");
    setCustomers(res.data);
  };

  useEffect(() => {
    loadCustomers();
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const createCustomer = async () => {
    await api.post("/customers", form);

    setForm({ full_name: "", email: "", phone: "" });

    loadCustomers();
  };

  const deleteCustomer = async (id) => {
    await api.delete(`/customers/${id}`);
    loadCustomers();
  };

  return (
    <div className="container mt-4">

      <h2>Customers</h2>

      {/* FORM */}
      <div className="card p-3 mb-3">

        <input name="full_name" placeholder="Name" value={form.full_name} onChange={handleChange} />
        <input name="email" placeholder="Email" value={form.email} onChange={handleChange} />
        <input name="phone" placeholder="Phone" value={form.phone} onChange={handleChange} />

        <button className="btn btn-primary mt-2" onClick={createCustomer}>
          Add Customer
        </button>

      </div>

      {/* TABLE */}
      <table className="table">

        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {customers.map(c => (
            <tr key={c.id}>
              <td>{c.full_name}</td>
              <td>{c.email}</td>
              <td>{c.phone}</td>
              <td>
                <button className="btn btn-danger btn-sm"
                  onClick={() => deleteCustomer(c.id)}>
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