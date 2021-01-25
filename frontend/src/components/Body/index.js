import React, { useState } from 'react'
import superagent from 'superagent'

import { If, Then, Else } from '../If'

function Body(props) {
    const [cityName, setCityName] = useState('')
    const [location, setLocation] = useState({
        lat: '47.6038321',
        lng: '-122.3300624',
    })
    const [searching, setSearching] = useState(true)

    const cityNameHandler = e => {
        e.preventDefault()
        setCityName(e.target.value)
    }

    console.log('here', cityName)
    const locationHandler = e => {
        e.preventDefault();
        setSearching(false)
        setLocation({
            lat: '51.5073219',
            lng: '-0.1276474'
        })
        // superagent
        //     .post('http://localhost:5000/lcoation')
        //     .send({ cityName: cityName })
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
                    <img src={`https://api.mapbox.com/styles/v1/mapbox/light-v10/static/${location.lng},${location.lat},14/800x500?access_token=pk.eyJ1IjoiaWJyYWhpbS1hamFybWVoIiwiYSI6ImNra2NldXp4ZzBmbWEzMWxjcTk5c2dwM3YifQ.aOQND81CvGPE6-hBg4kbhQ`} alt="Map of the Edmund Pettus Bridge in Selma, Alabama." />
                </Else>
            </If>
        </main>
    )
}

export default Body

