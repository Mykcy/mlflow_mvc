import React, {useState,useEffect} from 'react'
import axios from 'axios';


export default function App() {
  const [data,setData] = useState([{}])
  const FileUpload = () => {
    const [file, setFile] = useState(null);
  
    const handleFileChange = (event) => {
      setFile(event.target.files[0]);
    };
  
    const handleSubmit = async (event) => {
      event.preventDefault();
      const formData = new FormData();
      formData.append('file', file);
  
      try {
        const response = await axios.post('/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        console.log('File uploaded successfully:', response.data);
      } catch (error) {
        console.error('Error uploading file:', error);
      }
    };
  

  useEffect(()=>{
    fetch("/memebers").then(
        res => res.json()

  ).then(

      data => {
          setData(data)
          console.log(data)

      }
  )
},[])
  return (
    <form onSubmit={handleSubmit}>
      <input type="file" onChange={handleFileChange} />
      <button type="submit">Upload</button>
    </form>
  )
}

