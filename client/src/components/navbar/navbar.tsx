import react from 'react';
import './navbar.css';

export default function Navbar() {
    return (
        <div className='navbar'>
            <div className='fakesta-title'>FakeSta</div>
            <div className='nav-items'>
                <div className='premium'>Premium</div>
                <div className='login'>Login</div>
            </div>
        </div>
    )
}