
    /*
    async function getData(e) {
        e.preventDefault();
    
        const userInput = $('input[type="text"]').val();
        const apiKey = "f0f861af61e8dbbf1837299ddcc4d380";
        const url = `https://api.openweathermap.org/data/2.5/forecast?q=${userInput}&appid=${apiKey}`;
        
    
        const response = await fetch(url);
        const data = await response.json();
    
        console.log(data);

        $("#temperature").html(data.Temp);
        $("#humidity").html(data.Humid);
        $("#precipation").html(data.Precip);
    }
    
    $("form").on("submit", getData);

    */

    /* Practice */

    const posts = [
        {title: 'Post One', body:'This is post one'},
        {title: 'Post Two', body:'This is post two'}
    ]