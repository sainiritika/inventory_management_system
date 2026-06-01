import { useEffect, useState } from "react";
import api from "../services/api";

export default function Products() {

  const [products, setProducts] = useState([]);

  const [form, setForm] = useState({
    name: "",
    sku: "",
    price: "",
    stock_quantity: ""
  });


  const loadProducts = async () => {
    const res = await api.get("/products");
    setProducts(res.data);
  };

  useEffect(() => {
    loadProducts();
  }, []);


  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

 
  const createProduct = async () => {
    await api.post("/products", {
      ...form,
      price: parseFloat(form.price),
      stock_quantity: parseInt(form.stock_quantity)
    });

    setForm({ name: "", sku: "", price: "", stock_quantity: "" });

    loadProducts();
  };

 
  const deleteProduct = async (id) => {
    await api.delete(`/products/${id}`);
    loadProducts();
  };

  return (
    <div className="container mt-4">

      <h2>Products</h2>

      {/* FORM */}
      <div className="card p-3 mb-3">

        <input name="name" placeholder="Name" value={form.name} onChange={handleChange} />
        <input name="sku" placeholder="SKU" value={form.sku} onChange={handleChange} />
        <input name="price" placeholder="Price" value={form.price} onChange={handleChange} />
        <input name="stock_quantity" placeholder="Stock" value={form.stock_quantity} onChange={handleChange} />

        <button className="btn btn-primary mt-2" onClick={createProduct}>
          Add Product
        </button>

      </div>

      {/* TABLE */}
      <table className="table">

        <thead>
          <tr>
            <th>Name</th>
            <th>SKU</th>
            <th>Price</th>
            <th>Stock</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {products.map(p => (
            <tr key={p.id}>
              <td>{p.name}</td>
              <td>{p.sku}</td>
              <td>{p.price}</td>
              <td>{p.stock_quantity}</td>
              <td>
                <button className="btn btn-danger btn-sm"
                  onClick={() => deleteProduct(p.id)}>
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