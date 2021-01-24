import React, { useState } from 'react'
import superagent from 'superagent'

import { If, Then, Else } from '../If'

function Body(props) {
    const [cityName, setCityName] = useState('')
    const [location, setLocation] = useState({
        lat: '47.6038321',
        lng: '-122.3300624',
    })
    const [mapUrl, setMapUrl] = useState('https://maps.google.com/maps?q=47.6038321,-122.3300624&hl=es&z=14&amp;output=embed')
    const [searching, setSearching] = useState(false)

    const cityNameHandler = e => {
        e.preventDefault()
        setCityName(e.target.value)
    }

    console.log('here', cityName)
    const locationHandler = e => {
        e.preventDefault();
        setSearching(false)
        superagent
            .post('http://localhost:5000/lcoation')
            .send({ cityName: cityName })
    }

    return (
        <main>
            <If condition={searching}>
                <Then>
                    <form onSubmit={locationHandler}>
                        <input name='cityName' onChange={cityNameHandler} required placeholder='City Name' />
                        <input type='submit' value='Find' />
                    </form>
                </Then>
                <Else>
                    <iframe className='map'
                        width="60%"
                        height="500"
                        frameBorder="0"
                        scrolling="no"
                        marginHeight="0"
                        marginWidth="0"
                        src={mapUrl}
                    >
                    </iframe>
                </Else>
            </If>
        </main>
    )
}

export default Body

