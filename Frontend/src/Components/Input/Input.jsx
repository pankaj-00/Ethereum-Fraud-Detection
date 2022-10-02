import React, {useState} from 'react'

//CSS Files
import "./input.css"


const Input = (props) => {
  
  const [address, setAddress] = useState("");
  const [fraud, setFraud] = useState(false)
  const data = props.data;

  const handlePrediction = async() =>{
   await fetch("http://127.0.0.1:5000/predict",{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    },
    body: JSON.stringify(address)
  }).then(res=> console.log(res.json())).then(res=>{
    console.log(res)
  })
  }
   
  // console.log(fraud)
    
    return (
    <div>
      <h1>Ethereum Fraud Detection</h1>
      <div>
        <input type="text" placeholder='Address' onChange={(e)=>{ setAddress(JSON.stringify(e.target.value))}} required = "required"/>
        <button onClick={handlePrediction} >Predict</button>
      </div>
      
    </div>
  )
}

export default Input