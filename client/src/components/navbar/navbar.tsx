import react from 'react';
import './navbar.css';

export default function Navbar() {
    return (
        <div className='navbar'>
            <div className='fakesta-title'>FakeSta</div>
            <div className='link-items'>
                <div className='link-item'>Fake Followers</div>
                <div className='link-item'>Unfollow Tracker</div>
                <div className='link-item'>Ex Snooper</div>
                <div className='link-item'>About</div>

            </div>
            <div className='nav-items'>
                <div className='premium'>Premium</div>
                <div className='login'>Login</div>
            </div>
        </div>
    )
}