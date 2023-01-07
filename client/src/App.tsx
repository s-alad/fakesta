import React from 'react';
import './App.css';
import Navbar from './components/navbar/navbar';

function App() {

  const [username, setUsername] = React.useState('');

  function handlePublic() {
    console.log(username)

    fetch(`/fastcompare/${username}`).then(
      (res) => {
        return res.json()
      }).then(
        (data: any) => {
          console.log(data)
        }
    )
  }

  return (
    <>
      <Navbar></Navbar>
      <div className='app'>
        <div className='punchline'>
          <div className='fakesta'>FakeSta</div>
          <div className='info'>
            Find out who doesn't follow you back. Check out who someone started following or unfollowed. And much more!
          </div>
        </div>

        <div className='public'>
          <div className='public-title'>Enter the username of the account you would like to check for people that don't follow back.</div>
          <div className='public-input'>
            <input placeholder='username' onChange={(txt) => setUsername(txt.target.value)}></input>
            <button onClick={handlePublic}>Check!</button>
          </div>
        </div>

        <div className='private'>
          <div className='private-title'>Have a private account? Click here for more instructions</div>
          <div className='private-subtitle'>Don't worry, you won't need to login to your account.</div>
          <button>Private Check</button>
        </div>
      </div>
    </>
  );
}

export default App;
