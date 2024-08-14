// When you message:
//
// Send it like {Type, Username, Password}

async function sendMessage(message) {
    try {
        const response = await fetch('http://127.0.0.1:5000/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });
        
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
        alert("An error occured! " + error);
    }
}

function LoadedNew() {
    // Sounds
    var StartUPSound = new Audio('Start.wav');

    // DIVS
    const WelcomeDIV = document.getElementById("Welcome");
    const HomeDIV = document.getElementById("Home");
    const UnderRatedDIV = document.getElementById("Firefox");

    // Buttons
    var WelcomeDIV_Register = WelcomeDIV.querySelector("#Welcome-Register");
    var WelcomeDIV_Login = WelcomeDIV.querySelector("#Welcome-Login");

    // Button Functions
    WelcomeDIV_Register.addEventListener('click', function() {
        const Username = prompt("Please enter your new username");
        const Password = prompt("Please enter your new password");

        // Sends register request to the server
        const FromServer = sendMessage({"MSG" : "Register", "Username" : Username, "Password" : Password});

        if (FromServer == "AE") {
            alert("Please attempt to create another account. (Already Exists)");
        } else if (FromServer == "Done") {
            alert("You now have an EpiX account! (Sucsess)");
        } else {
            // Display if the server malformed
            alert("The server malformed? (" + FromServer + ")")
        }
    });

    WelcomeDIV_Login.addEventListener('click', function() {
        const Username = prompt("Please enter your username");
        const Password = prompt("Please enter your password");

        // Sends request to server to login.
        const FromServer = sendMessage({"MSG" : "Login", "Username" : Username, "Password" : Password})
    });
    
    // OnStart
    WelcomeDIV.style.display = 'block';
    HomeDIV.style.display = 'none';
    if (UnderRatedDIV) { // Check if UnderRatedDIV exists
        UnderRatedDIV.style.display = 'none';
    }
}

// Ensure script runs after DOM is fully loaded
document.addEventListener('DOMContentLoaded', LoadedNew);
